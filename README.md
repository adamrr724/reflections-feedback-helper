# GitHub Reflections & Feedback Workspace

A guided workspace for writing performance reflections and peer feedback. Copilot walks you through the entire process—pulling your GitHub contributions, prompting for metrics, and drafting your responses.

---

## Quick Start

Clones the repository locally and then open Visual Studio:

```bash
git clone https://github.com/adamrr724/reflections-feedback-helper.git
cd reflections-feedback-helper
code .
```

Open this repo on your local computer using VS Code, start a Copilot chat window inside the repo, and then just say: **"Start my reflection"** or **"Write feedback for [name]"**

---

## Prerequisites

- **VS Code** with **GitHub Copilot** extension installed and signed in
- **GitHub account** with access to your repositories

That's it! MCP configuration is included and loads automatically.

---

## How It Works

### For Reflections

Just say: **"Start my reflection"**

Copilot will guide you through:

1. **📋 Pull official questions** — Gets the latest from the IC Reflections FY26 Space
2. **📅 Ask for your reflection period** — e.g., "July 2025 - December 2025"
3. **🔄 Pull your GitHub contributions** — PRs, reviews, issues, docs automatically gathered
4. **📊 Prompt for support metrics** — CSAT, IR Met, tickets, escalations (one at a time)
5. **✨ Ask for other accomplishments** — Training, mentoring, cross-team work
6. **📝 Show contributions summary** — Review and edit before drafting
7. **✍️ Draft your reflection** — Answers each official question with your evidence
8. **🔍 Review and revise** — Make changes until you're satisfied

### For Peer Feedback

Just say: **"Write feedback for [name]"**

Copilot will guide you through:

1. **📋 Pull official template** — Gets the 3-question format from Peer & Manager Feedback Space
2. **💬 Prompt for details** — Projects together, strengths, growth areas
3. **📝 Review your notes** — Confirm before drafting
4. **✍️ Draft feedback** — Formatted to the official template
5. **🔍 Revise as needed**

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
.vscode/
  mcp.json                 # Auto-configures GitHub MCP
.github/
  copilot-instructions.md  # Defines the guided workflows
reflection/
  contributions/
    github_contributions.md      # Auto-generated
    support-metrics.md           # Prompted from you
    list_of_other_accomplishments.md
reflection_draft/          # Generated reflection drafts
feedback/
  recipients/
    recipient_template.md  # Template for new recipients
    [name].md              # Your notes per person
feedback_draft/            # Generated feedback drafts
```

---

## Quick Commands

| Say This | Copilot Does |
|----------|--------------|
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

Then start a new reflection—Copilot will pull fresh data and check for updated questions.

---

## Tips

- **Just start talking** — Say "Start my reflection" and follow the prompts
- **Be specific with examples** — Copilot will ask follow-up questions if needed
- **Review before submitting** — Always personalize AI-generated content
- **One thing at a time** — The workflow handles complexity for you

---

**Questions?** Just ask Copilot: *"How do I use this workspace?"*
