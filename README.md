# GitHub Reflections & Feedback Workspace

A guided workspace for writing performance reflections and peer feedback. Copilot walks you through the entire process — pulling your GitHub contributions, querying ADX for support metrics, and drafting your responses.

---

## Quick Start

### 1. Clone and Open in VS Code

```bash
git clone https://github.com/adamrr724/reflections-feedback-helper.git
```

Then open the `reflections-feedback-helper` folder in VS Code using whichever option works for you:

- **VS Code menu:** `File` → `Open Folder…` and pick the cloned directory
- **Drag & drop:** drag the `reflections-feedback-helper` folder onto the VS Code app icon or window
- **Terminal (only if you have the `code` command installed):** `cd reflections-feedback-helper && code .`
  - Don't have `code` yet? In VS Code, open the Command Palette (`Cmd+Shift+P` / `Ctrl+Shift+P`) and run **Shell Command: Install 'code' command in PATH**

### 2. Say "Let's get started" in Copilot Chat

That's it. Copilot will:

1. **Set up the ADX integration** — creates the Python environment and installs dependencies automatically
2. **Check your Azure auth** — if you need to sign in, it'll run `az login` for you (sign in with your **@githubazure.com** email when the browser opens)
3. **Verify both MCP connections** (ADX + GitHub) — if something isn't working, it'll offer to troubleshoot or let you skip and continue manually
4. **Ask what you'd like to do** — start a reflection, write peer feedback, or just pull contributions

> **Recommended models:** Claude Opus 4.7, Claude Opus 4.6, or Claude Sonnet 4.6

### That's the whole setup. Everything below is reference material.

---

## What It Does

### Reflection Workflow

Say: **"Start my reflection"**

Copilot will:

1. **Pull official questions** from the IC Reflections FY26 Copilot Space
2. **Ask for your info** — GitHub handle, reflection period, current level (all upfront)
3. **Launch parallel data pulls:**
   - **GitHub MCP** — PRs, reviews, issues, commits for the period
   - **ADX metrics** — CSAT, tickets solved, IR Met, handle time, escalations, priority breakdown, customer tier, squad contribution, and anonymous squad/team/region comparisons
   - **While those run** — asks you about additional accomplishments (mentoring, training, process improvements, etc.)
4. **Present everything gathered** with links to Zendesk tickets, GitHub issues/PRs, and IC issues — ask you to verify and fill any gaps
5. **Generate a contributions summary** for your review
6. **Draft your reflection** framed against your level expectations, saved to `reflection_draft/`

### Peer Feedback Workflow

Say: **"Write feedback for [name]"**

Copilot will:

1. **Pull the official 3-question template** from the Peer & Manager Feedback Copilot Space
2. **Ask for your info** — your handle, peer's handle, feedback period (all upfront)
3. **Launch parallel collaboration lookups:**
   - **ADX ticket collaboration** — finds Zendesk tickets where you both made updates (internal notes, replies), with ticket subjects, priority, premium/urgent flags, and direct Zendesk links
   - **ADX IC issue collaboration** — finds IC issues where you both commented, with repository breakdown
   - **GitHub collaboration** — shared PRs, reviews, issues
   - **While those run** — asks about projects together, strengths, growth areas
4. **Present collaboration examples** with links — you choose which to include
5. **Draft feedback** using the official template, weaving in the evidence you selected

---

## ADX Data Available

When the ADX integration is set up, Copilot can automatically pull:

| Category | Metrics |
|----------|---------|
| **Core** | CSAT (avg + breakdown), IR Met %, tickets solved, handle time, first response time |
| **High-Impact** | Urgent/high-priority tickets, customer tier breakdown (Premium Plus > Premium Standard > Non-Premium), squad contribution %, escalations with severity + EPD SLA |
| **Breakdown** | Tickets by team (Enterprise, Premium, Technical, Security & Revenue), tickets by region (AMER, EMEA, APAC) |
| **Collaboration** | IC issues filed by repo, IC comments, Zendesk followers/CCs |
| **Comparisons** | Anonymous squad/team/region aggregates (avg, median, P25, P75) for CSAT, tickets, IR Met, escalations, urgent/high tickets |
| **Peer Feedback** | Shared Zendesk tickets (with subjects and links), shared IC issues, shared GitHub activity |

> **Privacy:** Comparative queries only return aggregated, anonymous statistics. No names or handles of other employees are ever included.

All KQL queries are documented in [`reflection/adx_queries.md`](reflection/adx_queries.md) — you can also run them manually in [Kusto Web Explorer](https://dataexplorer.azure.com/).

---

## ADX Authentication Troubleshooting

The MCP server tries credentials in this order:

1. **DefaultAzureCredential** — picks up existing Azure CLI sessions, VS Code Azure extension tokens, managed identity, etc.
2. **InteractiveBrowserCredential** — opens a browser window if nothing else works

**Common issues:**

| Problem | Fix |
|---------|-----|
| Browser opens but login fails | Make sure you're signing in with your **@githubazure.com** email, not @github.com |
| "No credential could be found" | Run `az login` in terminal with your @githubazure.com account, or let the browser flow complete |
| Timeout on first query | The first query takes longer because it establishes the connection. Subsequent queries are faster (clients are cached) |
| Permission denied on cluster | Verify you have access to `gh-analytics.eastus.kusto.windows.net` — ask your manager if unsure |

---

## Copilot Spaces Used

| Space | What It Provides |
|-------|------------------|
| [IC Reflections FY26](https://github.com/copilot/spaces/github/998) | Reflection questions, performance philosophy, GitHub values |
| [Peer & Manager Feedback](https://github.com/copilot/spaces/github/50) | 3-question feedback template, Manager Fundamentals |
| [Support Repository Reference](https://github.com/copilot/spaces/github/1106) | Career ladder, level expectations, promotion criteria |

---

## Workspace Structure

```
.github/
  copilot-instructions.md        # Defines the guided workflows
.vscode/
  mcp.json                       # MCP server configuration (GitHub + ADX)
tools/
  mcp_kusto_readonly_server.py   # Custom read-only Kusto MCP server
  requirements.txt               # Python dependencies for ADX server
reflection/
  adx_queries.md                 # All KQL query templates (documented)
  contributions_template.md      # Template for GitHub contributions
  support-metrics_template.md    # Template for support metrics
  contributions/
    github_contributions.md      # Auto-generated from GitHub MCP
    support-metrics.md           # Populated from ADX + manual input
    other_accomplishments.md     # Created if you have additional items
reflection_draft/                # Generated reflection drafts
feedback/
  recipients/
    recipient_template.md        # Template for new recipients
    [name].md                    # Your notes per person
feedback_draft/                  # Generated feedback drafts
```

---

## Quick Commands

| Say This | Copilot Does |
|----------|--------------|
| "Let's get started" | Set up ADX, verify connections, ask what you'd like to do |
| "Start my reflection" | Full guided reflection workflow |
| "Write feedback for [name]" | Full guided feedback workflow |
| "Pull my contributions from July to December 2025" | Just pull GitHub data |
| "Start fresh for next cycle" | Archive and reset for new period |

---

## Starting a New Cycle

Say: **"Start fresh for next cycle"**

Or manually:
```bash
mkdir -p reflection_draft/archive/FY26-H1
mv reflection_draft/*.md reflection_draft/archive/FY26-H1/
```

Then start a new reflection — Copilot will pull fresh data and check for updated questions.

---

## Tips

- **Just say "let's get started"** — Copilot handles all setup and walks you through everything
- **No terminal commands needed** — Copilot runs everything for you (venv, pip, az login)
- **Verify your numbers** — Always cross-reference ADX data against Zendesk, PowerBI, and Medallia
- **ADX is optional** — If the MCP server isn't working, Copilot will ask you for metrics manually
- **Review before submitting** — Always personalize AI-generated content
- **Links are included** — Zendesk ticket links and GitHub URLs are provided where available
