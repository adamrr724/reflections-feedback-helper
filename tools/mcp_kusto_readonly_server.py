#!/usr/bin/env python3
"""
Read-only Azure Data Explorer (Kusto) MCP Server.

Exposes KQL query capabilities via the Model Context Protocol.
Authenticates using Azure Default credentials (browser/device code flow).

Usage (stdio transport):
    python3 tools/mcp_kusto_readonly_server.py
"""

import json
import os
from typing import Any

from azure.identity import DefaultAzureCredential, InteractiveBrowserCredential
from azure.kusto.data import KustoClient, KustoConnectionStringBuilder
from mcp.server.fastmcp import FastMCP

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

CLUSTERS = {
    "gh-analytics": {
        "url": "https://gh-analytics.eastus.kusto.windows.net",
        "databases": ["service_cs_analytics", "zendesk"],
    },
    "dotcomro": {
        "url": "https://dotcomro.eastus2.kusto.windows.net",
        "databases": ["Dotcom"],
    },
}

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

_clients: dict[str, KustoClient] = {}


def _get_credential():
    """Get Azure credential, preferring default then falling back to browser."""
    try:
        cred = DefaultAzureCredential()
        # Test the credential
        cred.get_token("https://kusto.kusto.windows.net/.default")
        return cred
    except Exception:
        return InteractiveBrowserCredential()


def _get_client(cluster_url: str) -> KustoClient:
    """Get or create a cached KustoClient for the given cluster URL."""
    if cluster_url not in _clients:
        credential = _get_credential()
        kcsb = KustoConnectionStringBuilder.with_azure_token_credential(
            cluster_url, credential
        )
        _clients[cluster_url] = KustoClient(kcsb)
    return _clients[cluster_url]


def _resolve_cluster(cluster_or_alias: str) -> str:
    """Resolve a cluster alias or URL to the full cluster URL."""
    if cluster_or_alias in CLUSTERS:
        return CLUSTERS[cluster_or_alias]["url"]
    if cluster_or_alias.startswith("https://"):
        return cluster_or_alias
    # Try partial match
    for alias, info in CLUSTERS.items():
        if cluster_or_alias in alias or cluster_or_alias in info["url"]:
            return info["url"]
    raise ValueError(
        f"Unknown cluster: {cluster_or_alias}. "
        f"Available: {list(CLUSTERS.keys())}"
    )


def _format_results(response) -> list[dict[str, Any]]:
    """Convert Kusto response to a list of dicts."""
    rows = []
    for table in response.primary_results:
        columns = [col.column_name for col in table.columns]
        for row in table.rows:
            rows.append(dict(zip(columns, [_serialize(v) for v in row])))
    return rows


def _serialize(value: Any) -> Any:
    """Make values JSON-serializable."""
    if hasattr(value, "isoformat"):
        return value.isoformat()
    if isinstance(value, (dict, list)):
        return value
    return value


# ---------------------------------------------------------------------------
# MCP Server
# ---------------------------------------------------------------------------

mcp = FastMCP(
    "azure-data-explorer",
    instructions=(
        "Read-only Azure Data Explorer (Kusto) MCP server. "
        "Use this to query support metrics, ticket data, CSAT scores, "
        "IC issues, and collaboration data from ADX clusters."
    ),
)


@mcp.tool()
def kusto_query(
    query: str,
    database: str,
    cluster: str = "gh-analytics",
) -> str:
    """Execute a read-only KQL query against Azure Data Explorer.

    Args:
        query: The KQL query to execute. Must be read-only (no .set, .append, .drop, etc.)
        database: The database name (e.g. 'service_cs_analytics', 'zendesk', 'Dotcom')
        cluster: Cluster alias ('gh-analytics', 'dotcomro') or full URL

    Returns:
        JSON string with query results as a list of row objects.
    """
    # Safety: block mutation commands
    dangerous = [".set", ".append", ".drop", ".delete", ".purge", ".replace",
                 ".create", ".alter", ".rename", ".move", ".attach", ".detach",
                 ".ingest"]
    query_lower = query.strip().lower()
    for cmd in dangerous:
        if cmd in query_lower:
            return json.dumps({
                "error": f"Mutation command '{cmd}' is not allowed. This server is read-only."
            })

    try:
        cluster_url = _resolve_cluster(cluster)
        client = _get_client(cluster_url)
        response = client.execute(database, query)
        results = _format_results(response)
        return json.dumps({
            "row_count": len(results),
            "results": results,
        }, indent=2, default=str)
    except Exception as e:
        return json.dumps({"error": str(e)})


@mcp.tool()
def kusto_list_clusters() -> str:
    """List the available ADX clusters and their databases.

    Returns:
        JSON with cluster aliases, URLs, and database names.
    """
    return json.dumps(CLUSTERS, indent=2)


@mcp.tool()
def kusto_describe_table(
    table_name: str,
    database: str = "service_cs_analytics",
    cluster: str = "gh-analytics",
) -> str:
    """Get the schema of a table in ADX.

    Args:
        table_name: Name of the table to describe
        database: Database name
        cluster: Cluster alias or URL

    Returns:
        JSON with column names, types, and docstrings.
    """
    query = f".show table {table_name} schema as json"
    try:
        cluster_url = _resolve_cluster(cluster)
        client = _get_client(cluster_url)
        response = client.execute(database, query)
        results = _format_results(response)
        return json.dumps(results, indent=2, default=str)
    except Exception as e:
        return json.dumps({"error": str(e)})


@mcp.tool()
def kusto_list_tables(
    database: str = "service_cs_analytics",
    cluster: str = "gh-analytics",
) -> str:
    """List all tables in a database.

    Args:
        database: Database name
        cluster: Cluster alias or URL

    Returns:
        JSON list of table names.
    """
    query = ".show tables | project TableName"
    try:
        cluster_url = _resolve_cluster(cluster)
        client = _get_client(cluster_url)
        response = client.execute(database, query)
        results = _format_results(response)
        return json.dumps(results, indent=2, default=str)
    except Exception as e:
        return json.dumps({"error": str(e)})


@mcp.tool()
def kusto_sample_table(
    table_name: str,
    database: str = "service_cs_analytics",
    cluster: str = "gh-analytics",
    row_count: int = 5,
) -> str:
    """Get a sample of rows from a table.

    Args:
        table_name: Name of the table to sample
        database: Database name
        cluster: Cluster alias or URL
        row_count: Number of sample rows (max 20)

    Returns:
        JSON with sample rows.
    """
    row_count = min(row_count, 20)
    query = f"{table_name} | take {row_count}"
    try:
        cluster_url = _resolve_cluster(cluster)
        client = _get_client(cluster_url)
        response = client.execute(database, query)
        results = _format_results(response)
        return json.dumps({
            "table": table_name,
            "row_count": len(results),
            "results": results,
        }, indent=2, default=str)
    except Exception as e:
        return json.dumps({"error": str(e)})


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    mcp.run(transport="stdio")
