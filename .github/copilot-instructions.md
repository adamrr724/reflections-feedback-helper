# Reflections & Feedback Workspace - Copilot Instructions

## Purpose

This workspace helps GitHub employees write performance reflections and peer feedback through a guided, interactive process. Copilot pulls real-time data from GitHub and references official guidance from Copilot Spaces.

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

### Step 2: Ask for Reflection Period and Level
Prompt the user:
> "What date range is this reflection for? (e.g., July 2025 - December 2025)"

Once provided:
- Use GitHub MCP to pull all contributions (PRs, reviews, issues, commits) for that period
- Save the contributions to `reflection/contributions/github_contributions.md`
- Tell the user what was found (e.g., "I found 23 PRs, 45 code reviews, and 12 issues")

Then ask for their level:
> "What is your current level? (Support Engineer II, Support Engineer III, Senior Support Engineer, or Staff Support Engineer)"

Once provided:
- Query the **Support Repository Reference** Space for the expectations at that level
- Keep these expectations in context to inform the reflection draft

### Step 3: Auto-Fill What's Available
From the GitHub data, automatically populate:
- KB/documentation contributions (PRs to docs repos)
- Engineering issues/escalations filed
- Collaboration activity (reviews, comments)

Create `reflection/contributions/support-metrics.md` from the template at `reflection/support-metrics_template.md` and populate with any data that can be inferred from GitHub.

### Step 4: Prompt for Support Metrics
Before prompting, tell the user:
> "You can find your support metrics in **PowerBI under the Support Metrics dashboards**, or work with your manager to get accurate numbers."

Then ask for each metric one at a time:

1. > "What was your **CSAT** this cycle? (target ≥4.5)"
2. > "What was your **IR Met** percentage? (target ≥95%)"
3. > "How many **tickets did you solve** vs. squad baseline?"
4. > "Any notable **escalations** you filed? (Sev1/Sev2 counts)"

Save responses to `reflection/contributions/support-metrics.md`.

### Step 5: Prompt for Other Accomplishments
Ask:
> "What other accomplishments would you like to include? Think about:
> - Training or certifications completed
> - Mentoring or onboarding new team members
> - Cross-team collaborations
> - Process improvements
> - Anything not captured in GitHub"

If the user provides additional accomplishments, create `reflection/contributions/other_accomplishments.md` and save the responses there. If the user has nothing to add, skip file creation and proceed to the next step.

### Step 6: Generate Contributions Summary
- Compile all gathered data into a comprehensive contributions document
- Present it to the user and ask:
> "Here's your contributions summary. Would you like to review and make any edits before I draft your reflection?"

Wait for user confirmation or edits.

### Step 7: Draft the Reflection
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

### Step 2: Create or Check Recipient File
- Check if `feedback/recipients/[name].md` exists
- If not, create it from the template

### Step 3: Prompt for Feedback Details
Ask the user for each piece of information:

1. > "What projects did you work on with **[name]**?"
2. > "What did **[name]** do really well? Can you give a specific example?"
3. > "What's one thing **[name]** could focus on to improve? Any specific situation?"
4. > "Anything else you'd like to mention about working with **[name]**?"

Save responses to `feedback/recipients/[name].md`.

### Step 4: Review Before Drafting
Present the gathered notes and ask:
> "Here's what I have for [name]'s feedback. Would you like to add or change anything before I draft the final version?"

Wait for user confirmation or edits.

### Step 5: Draft the Feedback
- Format answers using the official 3-question template
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
