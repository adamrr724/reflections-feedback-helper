# ADX Query Templates for Support Reflections

> **Important:** These queries provide directional data to supplement your reflection.
> Always cross-reference results against the official **PowerBI Support Metrics dashboards**
> for accuracy before including numbers in your reflection.

---

## How to Use This File

1. Replace `{{HANDLE}}` with your GitHub handle (e.g., `adamrr724`)
2. Replace `{{START_DATE}}` and `{{END_DATE}}` with your reflection period (e.g., `2025-07-01` and `2025-12-31`)
3. For collaboration queries, replace `{{MONTHS_ARRAY}}` with comma-separated months in `MM-YYYY` format
4. For peer feedback queries (Section 7), replace `{{PEER_HANDLE}}` with the peer's GitHub handle
5. Run queries via the MCP integration (automatic) or in [Kusto Web Explorer](https://dataexplorer.azure.com/) (manual)
6. All queries use cluster `gh-analytics.eastus.kusto.windows.net`, database `service_cs_analytics` unless noted

---

## Privacy Rules

> **CRITICAL:** Comparative queries return only **aggregated, anonymous statistics** (averages, medians, percentiles).
> **Never** include names, handles, or individually identifiable data about other employees
> in reflections or any output. All peer comparisons are group-level only.

---

# Section 1: Your Individual Metrics

## 1.1 Resolve Your Handle to IDs

Looks up your Zendesk and Dotcom IDs, title, and squad assignment. These IDs are used by all other queries.

```kql
supportv3_user_dim
| where user_handle == "{{HANDLE}}"
| project zendesk_user_id, dotcom_id, name, user_handle, employee_title,
          current_assigned_squad_1, current_assigned_squad_2,
          is_in_support_team, is_in_support_squad
```

---

## 1.2 Your CSAT Score

Your average experience CSAT, total survey count, and rating breakdown. **Target:** ≥ 4.5

```kql
let zendesk_id = toscalar(
    supportv3_user_dim | where user_handle == "{{HANDLE}}" | project zendesk_user_id
);
supportv3_ticket_csat_survey_fact
| where zendesk_user_id == zendesk_id
| where response_at between (datetime({{START_DATE}}) .. datetime({{END_DATE}}))
| summarize
    avg_experience_csat = round(avg(experience_csat), 2),
    avg_engineer_csat = round(avg(engineer_csat), 2),
    total_surveys = count(),
    csat_5_count = countif(experience_csat == 5),
    csat_4_count = countif(experience_csat == 4),
    csat_3_count = countif(experience_csat == 3),
    csat_below_3 = countif(experience_csat < 3)
```

---

## 1.3 Your Ticket Volume & Handle Time

Total solved tickets, average/median handle time, and average first response time.

```kql
let zendesk_id = toscalar(
    supportv3_user_dim | where user_handle == "{{HANDLE}}" | project zendesk_user_id
);
supportv3_ticket_fact
| where assignee_zendesk_id == zendesk_id
| where solved_at between (datetime({{START_DATE}}) .. datetime({{END_DATE}}))
| summarize
    tickets_solved = count(),
    avg_handle_time_hrs = round(avg(todecimal(handle_time_hours)), 2),
    median_handle_time_hrs = round(percentile(todecimal(handle_time_hours), 50), 2),
    avg_first_response_min = round(avg(reply_time_initial_response), 2)
```

---

## 1.4 Your IR Met (Initial Response SLA)

Initial response SLA compliance rate. **Target:** ≥ 95%

```kql
let zendesk_id = toscalar(
    supportv3_user_dim | where user_handle == "{{HANDLE}}" | project zendesk_user_id
);
supportv3_ticket_fact
| join kind=inner supportv3_ticket_dim on ticket_id
| where assignee_zendesk_id == zendesk_id
| where created_at between (datetime({{START_DATE}}) .. datetime({{END_DATE}}))
| where is_initial_response_eligible == true
| summarize
    total_ir_eligible = count(),
    ir_met_count = countif(met_initial_response == true),
    ir_breached_count = countif(met_initial_response == false),
    ir_met_pct = round(100.0 * countif(met_initial_response == true) / count(), 2)
```

---

# Section 2: High-Impact Contributions (Manager/Director Priorities)

> **These are the metrics managers and directors focus on most.** They demonstrate
> your impact on the highest-value work: urgent tickets, premium customers,
> escalations, and squad contribution share.

## 2.1 Your Urgent & High-Priority Ticket Contributions

Breaks down your tickets by priority level and flags urgent/escalated tickets. Urgent and high-priority tickets
carry outsized weight in performance reviews.

```kql
let zendesk_id = toscalar(
    supportv3_user_dim | where user_handle == "{{HANDLE}}" | project zendesk_user_id
);
supportv3_ticket_fact
| join kind=inner supportv3_ticket_dim on ticket_id
| where assignee_zendesk_id == zendesk_id
| where solved_at between (datetime({{START_DATE}}) .. datetime({{END_DATE}}))
| summarize
    total_tickets = count(),
    urgent_priority = countif(current_priority == "urgent"),
    high_priority = countif(current_priority == "high"),
    normal_priority = countif(current_priority == "normal"),
    low_priority = countif(current_priority == "low"),
    was_urgent_flag = countif(was_urgent == true),
    escalated_tickets = countif(is_escalated == true)
```

---

## 2.2 Your Tickets by Customer Tier

Breaks down your solved tickets by customer offering type. Customer tiers in order of importance:
**Premium Plus > Premium Standard > Non-Premium (Enterprise/Free)**

```kql
let zendesk_id = toscalar(
    supportv3_user_dim | where user_handle == "{{HANDLE}}" | project zendesk_user_id
);
supportv3_ticket_fact
| join kind=inner supportv3_ticket_dim on ticket_id
| where assignee_zendesk_id == zendesk_id
| where solved_at between (datetime({{START_DATE}}) .. datetime({{END_DATE}}))
| summarize tickets_solved = count() by offering_type
| order by tickets_solved desc
```

---

## 2.3 Your Tickets by Customer Tier AND Priority

Cross-references customer tier with priority to highlight your highest-impact work
(e.g., urgent Premium Plus tickets).

```kql
let zendesk_id = toscalar(
    supportv3_user_dim | where user_handle == "{{HANDLE}}" | project zendesk_user_id
);
supportv3_ticket_fact
| join kind=inner supportv3_ticket_dim on ticket_id
| where assignee_zendesk_id == zendesk_id
| where solved_at between (datetime({{START_DATE}}) .. datetime({{END_DATE}}))
| summarize tickets_solved = count() by offering_type, current_priority
| order by offering_type asc, tickets_solved desc
```

---

## 2.4 Your Squad Contribution Share

Shows what percentage of your squad's total ticket volume you handled. Demonstrates your
relative contribution within the squad.

```kql
let my_zendesk_id = toscalar(
    supportv3_user_dim | where user_handle == "{{HANDLE}}" | project zendesk_user_id
);
let my_squad = toscalar(
    supportv3_user_dim | where user_handle == "{{HANDLE}}" | project current_assigned_squad_1
);
let squad_members = supportv3_user_dim
    | where current_assigned_squad_1 == my_squad and is_in_support_squad == true
    | project zendesk_user_id;
supportv3_ticket_fact
| where assignee_zendesk_id in (squad_members)
| where solved_at between (datetime({{START_DATE}}) .. datetime({{END_DATE}}))
| summarize
    squad_total_tickets = count(),
    your_tickets = countif(assignee_zendesk_id == my_zendesk_id),
    squad_member_count = dcount(assignee_zendesk_id)
| extend
    your_pct_of_squad = round(100.0 * your_tickets / squad_total_tickets, 2),
    expected_even_share_pct = round(100.0 / squad_member_count, 2)
```

---

## 2.5 Your Escalations (Detailed)

Full escalation breakdown with severity, EPD SLA compliance, and average response time.
Filing quality escalations (especially sev1/sev2) demonstrates strong product intuition.

```kql
let dotcom_id = toscalar(
    supportv3_user_dim | where user_handle == "{{HANDLE}}" | project dotcom_id
);
supportv3_ic_issue_fact
| where user_dotcom_id == dotcom_id
| where issue_created_at between (datetime({{START_DATE}}) .. datetime({{END_DATE}}))
| join kind=inner supportv3_escalations_issue_dim on issue_id
| join kind=inner supportv3_escalations_issue_fact on issue_id
| summarize
    total_escalations = count(),
    sla_met = countif(is_sla_met == true),
    sla_breached = countif(is_sla_met == false),
    avg_epd_response_hrs = round(avg(sla_met_in_minutes) / 60.0, 2)
    by severity
| order by severity asc
```

---

## 2.6 Your IC Issues by Severity (Including Non-Escalation Issues)

All IC issues you opened, broken down by escalation severity where available.

```kql
let dotcom_id = toscalar(
    supportv3_user_dim | where user_handle == "{{HANDLE}}" | project dotcom_id
);
supportv3_ic_issue_fact
| where user_dotcom_id == dotcom_id
| where issue_created_at between (datetime({{START_DATE}}) .. datetime({{END_DATE}}))
| join kind=leftouter supportv3_escalations_issue_dim on issue_id
| summarize total_issues = count() by severity
| order by total_issues desc
```

---

## 2.7 Your Tickets by Team

Shows how your solved tickets distribute across support teams (Enterprise, Premium, Security & Revenue, Technical).

```kql
let zendesk_id = toscalar(
    supportv3_user_dim | where user_handle == "{{HANDLE}}" | project zendesk_user_id
);
supportv3_ticket_fact
| where assignee_zendesk_id == zendesk_id
| where solved_at between (datetime({{START_DATE}}) .. datetime({{END_DATE}}))
| join kind=inner supportv3_team_dim on team_id
| summarize tickets_solved = count() by team, grouped_team
| order by tickets_solved desc
```

---

## 2.8 Your Tickets by Region

Shows how your solved tickets distribute across AMER, EMEA, and APAC.

```kql
let zendesk_id = toscalar(
    supportv3_user_dim | where user_handle == "{{HANDLE}}" | project zendesk_user_id
);
supportv3_ticket_fact
| where assignee_zendesk_id == zendesk_id
| where solved_at between (datetime({{START_DATE}}) .. datetime({{END_DATE}}))
| join kind=inner supportv3_region_dim on region_id
| summarize tickets_solved = count() by region
| order by tickets_solved desc
```

---

# Section 3: Collaboration & Engineering Contributions

## 3.1 Your IC Issues by Repository

Shows which repositories you filed issues against and how many.

```kql
let dotcom_id = toscalar(
    supportv3_user_dim | where user_handle == "{{HANDLE}}" | project dotcom_id
);
supportv3_ic_issue_fact
| where user_dotcom_id == dotcom_id
| where issue_created_at between (datetime({{START_DATE}}) .. datetime({{END_DATE}}))
| join kind=inner supportv3_ic_repo_dim on repository_id
| summarize issue_count = count() by repository_name
| order by issue_count desc
```

---

## 3.2 Your Collaboration Footprint (Issue Comments)

Measures your IC comment activity — total comments, unique issues, and unique repos you engaged with.

> `comment_created_month` uses `MM-YYYY` format (e.g., `"07-2025"`).
> Build `{{MONTHS_ARRAY}}` as: `"07-2025","08-2025","09-2025","10-2025","11-2025","12-2025"`

```kql
let dotcom_id = toscalar(
    supportv3_user_dim | where user_handle == "{{HANDLE}}" | project dotcom_id
);
let valid_months = dynamic([{{MONTHS_ARRAY}}]);
supportv3_ic_comment_issue_fact
| where hubber_dotcom_id == dotcom_id
| where comment_created_month in (valid_months)
| summarize
    total_comments = count(),
    unique_issues_commented = dcount(issue_id),
    unique_repos_commented = dcount(repository_id)
```

---

## 3.3 Zendesk Collaboration (Followers/CCs)

Counts tickets where you were added as a follower or collaborator (helping other agents).

> Uses database `zendesk`. Requires your Zendesk user ID from query 1.1.

```kql
// Database: zendesk
tickets
| where updated_at between (datetime({{START_DATE}}) .. datetime({{END_DATE}}))
| where follower_ids has "{{USER_ZENDESK_ID}}" or collaborator_ids has "{{USER_ZENDESK_ID}}"
| summarize
    tickets_followed = count(),
    unique_assignees_helped = dcount(assignee_id)
```

---

# Section 4: Squad Comparisons (Anonymous)

> Compares your metrics against your **squad's aggregate averages**.
> No individual names or handles are included — only group-level statistics.

## 4.1 Squad CSAT Comparison

Your squad's average CSAT alongside percentile distribution.

```kql
let my_squad = toscalar(
    supportv3_user_dim | where user_handle == "{{HANDLE}}" | project current_assigned_squad_1
);
let squad_members = supportv3_user_dim
    | where current_assigned_squad_1 == my_squad and is_in_support_squad == true
    | project zendesk_user_id;
supportv3_ticket_csat_survey_fact
| where zendesk_user_id in (squad_members)
| where response_at between (datetime({{START_DATE}}) .. datetime({{END_DATE}}))
| summarize avg_csat = round(avg(experience_csat), 2) by zendesk_user_id
| summarize
    squad_avg_csat = round(avg(avg_csat), 2),
    squad_median_csat = round(percentile(avg_csat, 50), 2),
    squad_p25_csat = round(percentile(avg_csat, 25), 2),
    squad_p75_csat = round(percentile(avg_csat, 75), 2),
    squad_member_count = count()
```

---

## 4.2 Squad Ticket Volume Comparison

Squad's average, median, and percentile distribution of tickets solved per person.

```kql
let my_squad = toscalar(
    supportv3_user_dim | where user_handle == "{{HANDLE}}" | project current_assigned_squad_1
);
let squad_members = supportv3_user_dim
    | where current_assigned_squad_1 == my_squad and is_in_support_squad == true
    | project zendesk_user_id;
supportv3_ticket_fact
| where assignee_zendesk_id in (squad_members)
| where solved_at between (datetime({{START_DATE}}) .. datetime({{END_DATE}}))
| summarize tickets_solved = count(), avg_handle_time = round(avg(todecimal(handle_time_hours)), 2) by assignee_zendesk_id
| summarize
    squad_avg_tickets = round(avg(tickets_solved), 0),
    squad_median_tickets = round(percentile(tickets_solved, 50), 0),
    squad_p25_tickets = round(percentile(tickets_solved, 25), 0),
    squad_p75_tickets = round(percentile(tickets_solved, 75), 0),
    squad_avg_handle_time_hrs = round(avg(avg_handle_time), 2),
    squad_median_handle_time_hrs = round(percentile(avg_handle_time, 50), 2),
    squad_member_count = count()
```

---

## 4.3 Squad IR Met Comparison

Squad-wide IR Met percentage and per-person distribution.

```kql
let my_squad = toscalar(
    supportv3_user_dim | where user_handle == "{{HANDLE}}" | project current_assigned_squad_1
);
let squad_members = supportv3_user_dim
    | where current_assigned_squad_1 == my_squad and is_in_support_squad == true
    | project zendesk_user_id;
supportv3_ticket_fact
| join kind=inner supportv3_ticket_dim on ticket_id
| where assignee_zendesk_id in (squad_members)
| where created_at between (datetime({{START_DATE}}) .. datetime({{END_DATE}}))
| where is_initial_response_eligible == true
| summarize ir_met_pct = round(100.0 * countif(met_initial_response == true) / count(), 2) by assignee_zendesk_id
| summarize
    squad_avg_ir_met = round(avg(ir_met_pct), 2),
    squad_median_ir_met = round(percentile(ir_met_pct, 50), 2),
    squad_p25_ir_met = round(percentile(ir_met_pct, 25), 2),
    squad_p75_ir_met = round(percentile(ir_met_pct, 75), 2),
    squad_member_count = count()
```

---

## 4.4 Squad Escalation Comparison

Squad's average IC issues opened per person.

```kql
let my_squad = toscalar(
    supportv3_user_dim | where user_handle == "{{HANDLE}}" | project current_assigned_squad_1
);
let squad_members = supportv3_user_dim
    | where current_assigned_squad_1 == my_squad and is_in_support_squad == true
    | project dotcom_id;
supportv3_ic_issue_fact
| where user_dotcom_id in (squad_members)
| where issue_created_at between (datetime({{START_DATE}}) .. datetime({{END_DATE}}))
| summarize issues_filed = count() by user_dotcom_id
| summarize
    squad_avg_issues = round(avg(issues_filed), 1),
    squad_median_issues = round(percentile(issues_filed, 50), 0),
    squad_p75_issues = round(percentile(issues_filed, 75), 0),
    squad_member_count = count()
```

---

## 4.5 Squad Urgent/High-Priority Comparison

Squad's distribution of urgent and high-priority tickets per person.

```kql
let my_squad = toscalar(
    supportv3_user_dim | where user_handle == "{{HANDLE}}" | project current_assigned_squad_1
);
let squad_members = supportv3_user_dim
    | where current_assigned_squad_1 == my_squad and is_in_support_squad == true
    | project zendesk_user_id;
supportv3_ticket_fact
| join kind=inner supportv3_ticket_dim on ticket_id
| where assignee_zendesk_id in (squad_members)
| where solved_at between (datetime({{START_DATE}}) .. datetime({{END_DATE}}))
| summarize
    urgent_high = countif(current_priority in ("urgent", "high")),
    escalated = countif(is_escalated == true)
    by assignee_zendesk_id
| summarize
    squad_avg_urgent_high = round(avg(urgent_high), 1),
    squad_median_urgent_high = round(percentile(urgent_high, 50), 0),
    squad_p75_urgent_high = round(percentile(urgent_high, 75), 0),
    squad_avg_escalated = round(avg(escalated), 1),
    squad_member_count = count()
```

---

# Section 5: Team Comparisons (Anonymous)

> Compares metrics against the broader **team** (Enterprise, Security & Revenue, Technical, Premium).
> Only aggregate statistics — no individual data.

## 5.1 Team CSAT Comparison

Average CSAT across all agents by team.

```kql
supportv3_ticket_csat_survey_fact
| where response_at between (datetime({{START_DATE}}) .. datetime({{END_DATE}}))
| join kind=inner (
    supportv3_ticket_fact | project ticket_id, team_id
) on ticket_id
| join kind=inner supportv3_team_dim on team_id
| where is_support_team == true
| summarize
    team_avg_csat = round(avg(experience_csat), 2),
    team_total_surveys = count()
    by team, grouped_team
| order by team asc
```

---

## 5.2 Team Ticket Volume Comparison

Per-agent ticket averages by team.

```kql
supportv3_ticket_fact
| where solved_at between (datetime({{START_DATE}}) .. datetime({{END_DATE}}))
| join kind=inner supportv3_team_dim on team_id
| where is_support_team == true
| summarize tickets = count() by assignee_zendesk_id, team, grouped_team
| summarize
    team_avg_tickets_per_agent = round(avg(tickets), 0),
    team_median_tickets_per_agent = round(percentile(tickets, 50), 0),
    team_total_tickets = sum(tickets),
    team_agent_count = dcount(assignee_zendesk_id)
    by team, grouped_team
| order by team asc
```

---

## 5.3 Team IR Met Comparison

IR Met percentage by team.

```kql
supportv3_ticket_fact
| join kind=inner supportv3_ticket_dim on ticket_id
| join kind=inner supportv3_team_dim on team_id
| where is_support_team == true
| where created_at between (datetime({{START_DATE}}) .. datetime({{END_DATE}}))
| where is_initial_response_eligible == true
| summarize
    team_ir_met_pct = round(100.0 * countif(met_initial_response == true) / count(), 2),
    team_ir_eligible = count()
    by team, grouped_team
| order by team asc
```

---

# Section 6: Region Comparisons (Anonymous)

> Shows how metrics vary across **AMER, EMEA, and APAC**.
> Useful for context if you handle tickets across time zones.

## 6.1 Region CSAT Comparison

```kql
supportv3_ticket_csat_survey_fact
| where response_at between (datetime({{START_DATE}}) .. datetime({{END_DATE}}))
| join kind=inner (
    supportv3_ticket_fact | project ticket_id, region_id
) on ticket_id
| join kind=inner supportv3_region_dim on region_id
| summarize
    region_avg_csat = round(avg(experience_csat), 2),
    region_total_surveys = count()
    by region
| order by region asc
```

---

## 6.2 Region Ticket Volume Comparison

```kql
supportv3_ticket_fact
| where solved_at between (datetime({{START_DATE}}) .. datetime({{END_DATE}}))
| join kind=inner supportv3_region_dim on region_id
| summarize tickets = count() by assignee_zendesk_id, region
| summarize
    region_avg_tickets_per_agent = round(avg(tickets), 0),
    region_median_tickets_per_agent = round(percentile(tickets, 50), 0),
    region_total_tickets = sum(tickets),
    region_agent_count = dcount(assignee_zendesk_id)
    by region
| order by region asc
```

---

## 6.3 Region IR Met Comparison

```kql
supportv3_ticket_fact
| join kind=inner supportv3_ticket_dim on ticket_id
| join kind=inner supportv3_region_dim on region_id
| where created_at between (datetime({{START_DATE}}) .. datetime({{END_DATE}}))
| where is_initial_response_eligible == true
| summarize
    region_ir_met_pct = round(100.0 * countif(met_initial_response == true) / count(), 2),
    region_ir_eligible = count()
    by region
| order by region asc
```

---

# Section 7: Peer Feedback — Collaboration Lookups

> These queries find **shared activity between you and a peer** to inform peer feedback.
> Replace `{{HANDLE}}` with your handle and `{{PEER_HANDLE}}` with the peer's handle.
> Resolve both users' IDs via query 1.1 first.

## 7.1 Shared Zendesk Tickets — Summary

Finds tickets where **both users made updates** (internal notes, public replies, reassignments)
via `zendesk.ticket_events`. Returns counts and update breakdown.

> **Database: `zendesk`** — Requires both users' zendesk_user_ids from query 1.1.

```kql
// Database: zendesk
let my_zid = tolong({{MY_ZENDESK_ID}});
let peer_zid = tolong({{PEER_ZENDESK_ID}});
let my_tickets = ticket_events
    | where created_at between (datetime({{START_DATE}}) .. datetime({{END_DATE}}))
    | where updater_id == my_zid
    | distinct ticket_id;
let peer_tickets = ticket_events
    | where created_at between (datetime({{START_DATE}}) .. datetime({{END_DATE}}))
    | where updater_id == peer_zid
    | distinct ticket_id;
let shared = my_tickets | join kind=inner peer_tickets on ticket_id | project ticket_id;
ticket_events
| where ticket_id in (shared)
| where updater_id in (my_zid, peer_zid)
| where created_at between (datetime({{START_DATE}}) .. datetime({{END_DATE}}))
| summarize
    shared_tickets = dcount(ticket_id),
    your_updates_on_shared = countif(updater_id == my_zid),
    peer_updates_on_shared = countif(updater_id == peer_zid)
```

---

## 7.2 Shared Zendesk Tickets — Detail with Subjects

Pulls the actual ticket subjects, priority, assignee direction, and flags (premium, urgent, escalated)
for shared tickets. This is the most useful query for identifying strong collaboration examples.

> **Database: `zendesk`** — Run this after 7.1 to get actionable ticket-level detail.

```kql
// Database: zendesk
let my_zid = tolong({{MY_ZENDESK_ID}});
let peer_zid = tolong({{PEER_ZENDESK_ID}});
let my_tickets = ticket_events
    | where created_at between (datetime({{START_DATE}}) .. datetime({{END_DATE}}))
    | where updater_id == my_zid
    | distinct ticket_id;
let peer_tickets = ticket_events
    | where created_at between (datetime({{START_DATE}}) .. datetime({{END_DATE}}))
    | where updater_id == peer_zid
    | distinct ticket_id;
let shared_ids = my_tickets | join kind=inner peer_tickets on ticket_id | project ticket_id;
tickets
| where id in (shared_ids)
| extend who_was_assignee = case(
    assignee_id == my_zid, "you",
    assignee_id == peer_zid, "peer",
    "other"
)
| extend ticket_link = strcat("https://github.zendesk.com/agent/tickets/", tostring(id))
| project id, subject, priority, status, who_was_assignee, created_at, ticket_link,
    is_premium = tags has "premium_support",
    is_premium_plus = tags has "premium_plus",
    has_escalation = tags has "ghsidecar-escalation-opened",
    was_urgent = tags has "urgent_ticket"
| order by created_at desc
```

**How to read the results:**
- `who_was_assignee = "you"` → Your ticket, peer helped (peer provided insight/collaboration)
- `who_was_assignee = "peer"` → Peer's ticket, you helped (you provided insight/collaboration)
- `who_was_assignee = "other"` → Third-party assignee, both of you contributed
- `ticket_link` → Direct link to the ticket in Zendesk Agent view

**High-value collaboration signals:** Look for tickets that are `is_premium_plus`, `was_urgent`,
`has_escalation`, or `priority = "high"` — these show impactful teamwork on critical work.

---

## 7.3 Shared IC Issues (Both Commented)

Finds IC issues where **both users left comments** during the period, with repository breakdown.

```kql
let my_dotcom_id = toscalar(
    supportv3_user_dim | where user_handle == "{{HANDLE}}" | project dotcom_id
);
let peer_dotcom_id = toscalar(
    supportv3_user_dim | where user_handle == "{{PEER_HANDLE}}" | project dotcom_id
);
let valid_months = dynamic([{{MONTHS_ARRAY}}]);
let my_issues = supportv3_ic_comment_issue_fact
    | where hubber_dotcom_id == my_dotcom_id and comment_created_month in (valid_months)
    | distinct issue_id;
let peer_issues = supportv3_ic_comment_issue_fact
    | where hubber_dotcom_id == peer_dotcom_id and comment_created_month in (valid_months)
    | distinct issue_id;
my_issues
| join kind=inner peer_issues on issue_id
| join kind=inner supportv3_ic_issue_fact on issue_id
| join kind=leftouter supportv3_ic_repo_dim on repository_id
| summarize
    shared_issues = dcount(issue_id),
    shared_repos = make_set(repository_name)
```

---

## 7.4 Shared IC Issues — Repo Breakdown

Same as 7.3 but grouped by repository for more detail.

```kql
let my_dotcom_id = toscalar(
    supportv3_user_dim | where user_handle == "{{HANDLE}}" | project dotcom_id
);
let peer_dotcom_id = toscalar(
    supportv3_user_dim | where user_handle == "{{PEER_HANDLE}}" | project dotcom_id
);
let valid_months = dynamic([{{MONTHS_ARRAY}}]);
let my_issues = supportv3_ic_comment_issue_fact
    | where hubber_dotcom_id == my_dotcom_id and comment_created_month in (valid_months)
    | distinct issue_id;
let peer_issues = supportv3_ic_comment_issue_fact
    | where hubber_dotcom_id == peer_dotcom_id and comment_created_month in (valid_months)
    | distinct issue_id;
my_issues
| join kind=inner peer_issues on issue_id
| join kind=inner supportv3_ic_issue_fact on issue_id
| join kind=leftouter supportv3_ic_repo_dim on repository_id
| summarize shared_issues = dcount(issue_id) by repository_name
| order by shared_issues desc
```

---

# Section 8: Reference

## Customer Tier Importance (Highest → Lowest)
1. **Premium Plus** — Top-tier paid support customers
2. **Premium Standard** — Paid support customers
3. **Non-Premium (Enterprise)** — Enterprise Cloud/Server customers without premium support
4. **Non-Premium (Other)** — Free/Pro plan users

## Ticket Priority Levels
| Priority | Significance |
|----------|-------------|
| **Urgent** | Critical customer-impacting issues; highest visibility |
| **High** | Important issues needing fast resolution |
| **Normal** | Standard support tickets |
| **Low** | Minor issues or informational requests |

## Support Teams
| Team | Grouped Team |
|------|-------------|
| Enterprise | Enterprise |
| Technical | Technical |
| Security & Revenue Support | Security & Revenue Support |
| Premium Standard | Premium |
| Premium Plus | Premium |

## Regions
| Region | Description |
|--------|-------------|
| AMER | Americas (UTC 16:00–23:59) |
| EMEA | Europe, Middle East, Africa (UTC 08:00–15:59) |
| APAC | Asia Pacific (UTC 00:00–07:59) |

## Support Squads
Access, Account Security, BIA, Billing, C2C, Compliance, Ecosystem, Infrastructure, Security Incident Response, Worktent

---

# Running These Queries

## Option A: MCP Integration (Automated)
If the `azure-data-explorer` MCP server is configured, Copilot runs these
queries automatically during the reflection workflow and populates `support-metrics.md`.

## Option B: Kusto Web Explorer (Manual)
1. Go to [Kusto Web Explorer](https://dataexplorer.azure.com/)
2. Connect to cluster: `gh-analytics.eastus.kusto.windows.net`
3. Select database: `service_cs_analytics` (or `zendesk` for query 3.3)
4. Paste the query, replace `{{placeholders}}`, and run

## Option C: Azure CLI
```bash
az kusto query --cluster "gh-analytics.eastus.kusto.windows.net" \
  --database "service_cs_analytics" \
  --query "YOUR_KQL_QUERY_HERE"
```

---

> **Reminder:** Always verify ADX numbers against the **PowerBI Support Metrics dashboards** before finalizing your reflection.
