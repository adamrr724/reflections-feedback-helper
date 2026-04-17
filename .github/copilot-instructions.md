# Reflections & Feedback Workspace - Copilot Instructions

## Purpose

This workspace helps GitHub employees write performance reflections and peer feedback through a guided, interactive process. Copilot pulls real-time data from GitHub and references official guidance from Copilot Spaces.

## First-Time Setup Check

**Before starting any workflow**, check if the ADX integration is set up by verifying the Python virtual environment exists at `tools/.venv/`. If it does NOT exist, set it up for the user:

> "Before we begin, let me set up the ADX integration so I can automatically pull your support metrics (CSAT, tickets, IR Met, escalations, etc.)."

**Step 1: Install dependencies** — Run this directly in the terminal for the user (do NOT ask them to run it themselves):
```bash
cd tools && python3 -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt
```

**Step 2: Azure authentication** — Tell the user:
> "The MCP server needs your **@githubazure.com** credentials to access the ADX clusters. If you've already signed in via `az login` or the VS Code Azure extension with that account, you're all set. Otherwise, I can run `az login` for you — just confirm and sign in with your **@githubazure.com** email (not @github.com) when the browser opens."

If the user confirms they need to authenticate, run `az login` in the terminal for them.

**Step 3: Verify** — After setup, try listing ADX clusters to confirm the connection works. If it fails, refer the user to the troubleshooting section in the README.

If `tools/.venv/` already exists, skip this and proceed directly to the requested workflow.

---

## Required Copilot Spaces

**ALWAYS query these Copilot Spaces for the latest official questions and guidance:**

| Space | URL | Use For |
|-------|-----|---------|
| **IC Reflections FY26** | https://github.com/copilot/spaces/github/998 | Official reflection questions, performance philosophy, GitHub values |
| **Peer & Manager Feedback** | https://github.com/copilot/spaces/github/50 | Official 3-question feedback template, Manager Fundamentals |
| **Support Repository Reference** | https://github.com/copilot/spaces/github/1106 | Support career ladder, level expectations, promotion criteria |

**CRITICAL:** Always pull the latest from these Spaces before starting any workflow.

---

## Guided Reflection Workflow

When a user says **"Help me write my reflection"** or **"Start my reflection"**, follow this interactive process:

### Step 1: Pull Official Guidance
- Query the **IC Reflections FY26** Space to get the latest reflection questions and writing guidance
- Query the **Support Repository Reference** Space for level expectations (if applicable)
- Confirm to the user what questions they'll be answering

### Step 2: Collect Required Info (All Upfront)

Ask all three questions together so data pulls can start immediately:

> "Before I start gathering your data, I need a few things:
> 1. **GitHub handle** — e.g., `adamrr724`
> 2. **Reflection period** — date range (e.g., July 2025 - December 2025)
> 3. **Current level** — Support Engineer II, Support Engineer III, Senior Support Engineer, or Staff Support Engineer"

Once all three are provided, proceed to Step 3 immediately.

### Step 3: Launch Data Pulls in Parallel

**Kick off all automated data gathering simultaneously** using subagents or parallel tool calls. Do NOT wait for one to finish before starting the next.

**In parallel:**

#### 3a. GitHub MCP Pull (subagent)
- Use GitHub MCP to pull all contributions (PRs, reviews, issues, commits) for the period
- Save to `reflection/contributions/github_contributions.md`
- Auto-populate KB/documentation contributions, engineering issues, collaboration activity

#### 3b. ADX Metrics Pull (subagent)
If ADX data is available (via Kusto MCP, Azure CLI, or user-provided query results), use the KQL queries in `reflection/adx_queries.md` to pull:

- **CSAT** — avg score, total surveys, rating breakdown (from `supportv3_ticket_csat_survey_fact`)
- **IR Met / SLA compliance** — percentage and counts (from `supportv3_ticket_fact`)
- **Ticket volume** — tickets solved, avg handle time, avg first response time (from `supportv3_ticket_fact`)
- **Urgent/High-Priority tickets** — breakdown by priority level and `was_urgent`/`is_escalated` flags (from `supportv3_ticket_dim`)
- **Customer tier breakdown** — tickets by offering type: Premium Plus > Premium Standard > Non-Premium (from `supportv3_ticket_dim`)
- **Squad contribution share** — your % of squad's total ticket volume
- **Escalations** — IC issues with severity, EPD SLA compliance, avg response time (from `supportv3_escalations_issue_dim` + `supportv3_escalations_issue_fact`)
- **Team & Region breakdown** — tickets by support team (Enterprise, Technical, Premium, Security & Revenue) and region (AMER, EMEA, APAC)
- **Collaboration footprint** — IC comments, unique issues/repos (from `supportv3_ic_comment_issue_fact`)
- **Zendesk collaboration** — tickets followed/CC'd (from `zendesk.tickets`)
- **Squad comparisons** — anonymous aggregate stats (avg, median, p25, p75) for CSAT, tickets, IR Met, escalations, and urgent/high tickets across your squad
- **Team comparisons** — anonymous aggregate stats by support team
- **Region comparisons** — anonymous aggregate stats by AMER/EMEA/APAC

**Privacy Rule:** Comparative queries must ONLY return **aggregated, anonymous statistics** (averages, medians, percentiles). NEVER include names, handles, or individually identifiable data about other employees. All peer comparisons are group-level only.

**ADX Connection Details:**
| Cluster | Database | Use For |
|---------|----------|---------|
| `gh-analytics.eastus.kusto.windows.net` | `service_cs_analytics` | Ticket metrics, IC issues/PRs, user dim |
| `gh-analytics.eastus.kusto.windows.net` | `zendesk` | Raw Zendesk data (followers, CCs) |
| `dotcomro.eastus2.kusto.windows.net` | `Dotcom` | Dotcom entity data |

**How to use:**
1. Ask the user for their **GitHub handle** to resolve their user ID via `supportv3_user_dim`
2. Use the reflection period dates as `{{START_DATE}}` and `{{END_DATE}}`
3. If a Kusto MCP or CLI is available, run queries automatically and populate `support-metrics.md`
4. If not, tell the user:
   > "I have KQL queries ready to pull your metrics from ADX. You can run them in [Kusto Web Explorer](https://dataexplorer.azure.com/) and paste the results here, or I can fill in what you tell me manually."
5. Populate the ADX-sourced fields in `reflection/contributions/support-metrics.md`

#### 3c. Level Expectations (during parallel pulls)
While data pulls run in the background:
- Query the **Support Repository Reference** Space for expectations at their level
- Keep these expectations in context to inform the reflection draft

#### 3d. While Data Pulls Run — Ask for Additional Context

**Do not wait** for GitHub/ADX pulls to complete. While they run, immediately proceed to gather user input:

> "While I pull your GitHub contributions and ADX metrics, let me ask a few more questions..."

Then ask:
> "What other accomplishments would you like to include? Think about:
> - Training or certifications completed
> - Mentoring or onboarding new team members
> - Cross-team collaborations
> - Process improvements
> - Anything not captured in GitHub or ADX"

If the user provides additional accomplishments, create `reflection/contributions/other_accomplishments.md` and save the responses there.

### Step 4: Present All Gathered Data & Fill Gaps

Once all parallel pulls are complete, present a combined summary:

> **Disclaimer:** Always verify this contribution data before including it in your reflection. Cross-reference against **Zendesk**, **PowerBI**, and **Medallia** for posterity.

Present GitHub contributions + ADX metrics together and ask:
> "Here's everything I gathered: [summary of GitHub PRs/issues + ADX metrics]. Does this look right? Anything to correct or add?"

When presenting contributions, include direct links where available:
- **Zendesk tickets:** `https://github.zendesk.com/agent/tickets/{id}`
- **GitHub issues/PRs:** Full GitHub URL from MCP data
- **IC issues:** Link if available from repository + issue number

Then ask for any **remaining** metrics not yet filled:

1. > "What was your **CSAT** this cycle? (target ≥4.5)"
2. > "What was your **IR Met** percentage? (target ≥95%)"
3. > "How many **tickets did you solve** vs. squad baseline?"
4. > "Any notable **escalations** you filed? (Sev1/Sev2 counts)"

Save responses to `reflection/contributions/support-metrics.md`.

### Step 5: Generate Contributions Summary
- Compile all gathered data into a comprehensive contributions document
- Present it to the user and ask:
> "Here's your contributions summary. Would you like to review and make any edits before I draft your reflection?"

Wait for user confirmation or edits.

### Step 6: Draft the Reflection
- Using the official questions from the Space and all gathered evidence
- Reference the **Support Repository Reference** Space level expectations for their role (Support Engineer II/III/Senior/Staff)
- Frame accomplishments in terms of how they demonstrate performance at or above their level
- Draft answers to each reflection question
- Save to `reflection_draft/reflection_[period].md`
- **Display the full draft directly in the chat window** so the user can review without opening the file
- Tell the user which file the draft was saved to (e.g., "Saved to `reflection_draft/reflection_jul-dec_2025.md`")
- Ask:
> "Here's your draft reflection. Would you like me to revise anything?"

---

## Guided Feedback Workflow

When a user says **"Write feedback for [name]"** or **"Start feedback for [name]"**, follow this interactive process:

### Step 1: Pull Official Template
- Query the **Peer & Manager Feedback** Space for the latest 3-question template
- Confirm the questions to the user

### Step 2: Collect Required Info (Upfront)

Ask:
> "Before I start, I need a few things:
> 1. **Your GitHub handle** — e.g., `adamrr724`
> 2. **[name]'s GitHub handle** — so I can look up collaboration data
> 3. **Feedback period** — date range (e.g., July 2025 - December 2025)"

Once all three are provided, proceed to Step 3 immediately.

### Step 3: Launch Collaboration Lookups in Parallel

**Kick off all data gathering simultaneously.** Do NOT wait for one to finish before starting the next.

**In parallel:**

#### 3a. ADX Ticket Collaboration (subagent)
Use the Kusto MCP to find shared ticket activity between the two users:
1. Resolve both users' `zendesk_user_id` and `dotcom_id` via `supportv3_user_dim`
2. Query `zendesk.ticket_events` to find tickets where **both users made updates** (internal notes, public replies, reassignments) during the feedback period
3. Query `supportv3_ic_comment_issue_fact` to find **IC issues where both users commented** during the period, with repository breakdown
4. Summarize: shared ticket count, shared IC issue count, repos in common

#### 3b. GitHub Collaboration (subagent)
Use the GitHub MCP to find shared GitHub activity:
1. Search for **PRs authored by one and reviewed by the other** (both directions)
2. Search for **issues where both users commented**
3. Search for **shared repository contributions** (commits, PRs)
4. Summarize: shared PRs/reviews, shared issues, repos in common

#### 3c. While Data Pulls Run — Ask for Feedback Details

**Do not wait** for ADX/GitHub pulls to complete. While they run, immediately ask:

1. > "While I pull your collaboration data with **[name]**, let me ask some questions..."
2. > "What projects did you work on with **[name]**?"
3. > "What did **[name]** do really well? Can you give a specific example?"
4. > "What's one thing **[name]** could focus on to improve? Any specific situation?"
5. > "Anything else you'd like to mention about working with **[name]**?"

Save responses to `feedback/recipients/[name].md`.

### Step 4: Present Collaboration Data & Review

Once all parallel pulls are complete, present the collaboration summary:

> "Here's what I found about your collaboration with **[name]**:
> - **Shared Zendesk tickets:** [count] tickets where you both made updates
> - **Shared IC issues:** [count] issues where you both commented ([repos])
> - **GitHub activity:** [PRs reviewed, shared issues, etc.]
>
> **Notable examples:**
> - [Ticket subject] ([link](https://github.zendesk.com/agent/tickets/ID)) — [priority], [premium/urgent flags], [who was assignee]
> - [Ticket subject] ([link](https://github.zendesk.com/agent/tickets/ID)) — [context]
>
> Would you like to reference any of these in your feedback? I can weave specific collaboration examples into the draft."

**Important:** Always include clickable Zendesk links (`https://github.zendesk.com/agent/tickets/{id}`) and GitHub issue/PR links when presenting collaboration data. Prioritize showing high-priority, urgent, Premium Plus, and escalated tickets as examples.

Then present the gathered notes alongside the collaboration data and ask:
> "Here's everything I have for [name]'s feedback. Would you like to add or change anything before I draft the final version?"

Wait for user confirmation or edits.

### Step 5: Draft the Feedback
- Format answers using the official 3-question template
- Where the user opted in, incorporate collaboration data as concrete evidence
- Save to `feedback_draft/[name].md`
- **Display the full draft directly in the chat window** so the user can review without opening the file
- Tell the user which file the draft was saved to (e.g., "Saved to `feedback_draft/vance.md`")
- Ask if revisions are needed

---

## Workspace Structure

```
reflection/
  contributions_template.md      # Template for GitHub contributions
  support-metrics_template.md    # Template for support metrics
  contributions/
    github_contributions.md      # Auto-generated from MCP
    support-metrics.md           # Created from template, filled by user
    other_accomplishments.md     # Created only if user has additional items
reflection_draft/                # Generated reflection drafts
feedback/
  recipients/
    recipient_template.md        # Template for new recipients
    [name].md                    # Notes per person
feedback_draft/                  # Generated feedback drafts
```

---

## Writing Guidelines

- **Be specific** — Use concrete examples with metrics
- **Performance = Impact** — Focus on outcomes, not activity
- **Write naturally** — Conversational, not corporate
- **Use paragraphs** — Avoid excessive bullet points in final output
- **Quantify** — Numbers make impact tangible

---

## Quick Commands

| User Says | Copilot Does |
|-----------|--------------|
| "Get started" / "Let's get started" | Run First-Time Setup Check, then ask what they'd like to do |
| "Start my reflection" | Run guided reflection workflow |
| "Write feedback for [name]" | Run guided feedback workflow |
| "Pull my contributions from [dates]" | MCP pull only, save to contributions folder |
| "Start fresh for next cycle" | Archive current work, clear contribution files |

---

## Cycle Reset Process

When starting a new reflection cycle:
1. Move current drafts to `reflection_draft/archive/[cycle]/`
2. Delete `reflection/contributions/support-metrics.md` and `reflection/contributions/other_accomplishments.md` (if exists)
3. Clear `reflection/contributions/github_contributions.md` content
4. Pull fresh contributions for new date range
5. Query Spaces for any updated questions/guidance
