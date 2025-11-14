# GitHub Reflections & Feedback Workspace

A structured workspace for managing your GitHub performance reflections and peer feedback using AI assistance and GitHub MCP (Model Context Protocol) integration.

---

## � Quick Start

### Clone This Repository

```bash
git clone https://github.com/adamrr724/reflections-feedback-helper.git
cd reflections-feedback-helper
```

Or if you prefer SSH:

```bash
git clone git@github.com:adamrr724/reflections-feedback-helper.git
cd reflections-feedback-helper
```

Then open the folder in VS Code:

```bash
code .
```

---

## �📋 Table of Contents

- [Quick Start](#quick-start)
- [Prerequisites](#prerequisites)
- [Setup & Configuration](#setup--configuration)
- [Writing Your Reflection](#writing-your-reflection)
- [Providing Peer Feedback](#providing-peer-feedback)
- [Workspace Structure](#workspace-structure)
- [Tips & Best Practices](#tips--best-practices)

---

## Prerequisites

- **VS Code** (latest version)
- **GitHub Copilot subscription** (individual, business, or enterprise)
- **GitHub Copilot extension** installed in VS Code
- **Authenticated GitHub Copilot** - You must be signed into GitHub Copilot in VS Code
- **MCP support** - Built into VS Code when Copilot is installed
- **GitHub account** with access to your contributions and activity

### Quick Check: Is Copilot Ready?

1. Open VS Code
2. Look for the GitHub Copilot icon in the bottom right status bar
3. Click it and ensure you're signed in
4. If not installed, search for "GitHub Copilot" in the Extensions marketplace and install it
5. Authenticate with your GitHub account when prompted

---

## Setup & Configuration

### 1. Configure GitHub MCP

GitHub MCP allows you to pull your contributions data, access GitHub Copilot Spaces, and integrate GitHub data into your workflow.

> **Note:** MCP support is built into VS Code when you have GitHub Copilot installed. You just need to configure which MCP servers to use.

#### Option A: One-Click Installation (Easiest)

Click this link to automatically install and configure GitHub MCP:

**[Install GitHub MCP Server](https://insiders.vscode.dev/redirect/mcp/install?name=github&config=%7B%22type%22%3A%20%22http%22%2C%22url%22%3A%20%22https%3A%2F%2Fapi.githubcopilot.com%2Fmcp%2F%22%7D)**

This will automatically add the GitHub MCP server to your VS Code configuration.

#### Option B: Manual Configuration

Create or update `~/Library/Application Support/Code/User/mcp.json`:

```json
{
  "servers": {
    "github": {
      "type": "http",
      "url": "https://api.githubcopilot.com/mcp/",
      "headers": {
        "X-MCP-Toolsets": "default,copilot_spaces,copilot"
      }
    }
  }
}
```

This configuration:
- Connects to the GitHub MCP server
- Enables default tools, Copilot Spaces, and Copilot features
- Uses your existing GitHub Copilot authentication automatically

#### Workspace Configuration

This repo includes a workspace-level `mcp.json` that ensures the GitHub MCP server is configured with the necessary toolsets (`copilot_spaces`) when you open this workspace. Your user-level configuration will still apply globally across all VS Code projects.

### 2. Verify MCP is Working

After creating the MCP configuration file, restart VS Code. MCP should automatically connect to the GitHub server.

To verify it's working, open this workspace and check:
- GitHub Copilot is active (bottom right corner)
- No MCP connection errors in the Output panel (View → Output → GitHub Copilot)

### 3. Authentication

No additional authentication needed! The GitHub MCP server uses your existing GitHub Copilot authentication automatically. As long as you're signed into GitHub Copilot in VS Code, the MCP tools will work.

### 4. Verify Setup

Ask GitHub Copilot: "Can you list my GitHub Copilot Spaces?" 

If the setup is working, you should see available spaces including:
- **Reflection** - Official GitHub reflection guidance
- **Peer & Manager Feedback** - Official GitHub feedback templates

---

## Writing Your Reflection

### Step 1: Gather Your GitHub Contributions

Ask Copilot to pull your GitHub contributions for your reflection period:

```
"Pull my GitHub contributions from [START_MONTH] to [END_MONTH] [YEAR]"
```

**Example:** "Pull my GitHub contributions from October to November 2024"

> **Note:** Specify the time window that matches your reflection period (typically 6 months for H1 or H2 reflections).

This will create a file in `reflection/contributions/` with your:
- Merged pull requests
- Code reviews
- Issues created/resolved
- Repository contributions
- Documentation updates

### Step 2: Document Additional Accomplishments

Fill out these files in `reflection/contributions/`:

**`support-metrics.md`** (For Support Engineers)
- Fill in your CSAT score (target ≥4.5)
- Fill in your IR Met percentage (target ≥95%)
- Document tickets solved and complexity vs squad baseline
- Track escalations filed (break down by Sev1/Sev2/Other)
- Note collaboration, documentation, and training contributions
- Reference `support-expectations.md` for level-specific metric weights

**`sparkle_tracking.md`**
- Track internal recognition (Sparkles, kudos)
- Note positive feedback received

**`list_of_other_accomplishments.md`**
- Non-GitHub accomplishments
- Training sessions delivered
- Cross-team collaborations
- Process improvements
- Mentoring activities
- Security initiatives

### Step 3: Draft Your Reflection

Ask Copilot to help you draft your reflection:

```
"Help me draft my FY26 reflection using the official GitHub reflection questions"
```

Copilot will use:
- Your contributions data
- Official reflection questions from the **Reflection** Copilot Space
- GitHub's performance philosophy
- Your documented accomplishments

Your draft will be saved in `reflection_draft/my_reflection_draft.md`

### Step 4: Review and Refine

The draft will answer the three official FY26 questions:
1. **What results did you deliver, and how did you do it?**
   - Quantified impact with metrics
   - AI leverage examples
   - Security contributions
   - Culture alignment

2. **Reflect on recent challenges - what did you learn and how did you apply a growth mindset?**
   - Specific challenge described
   - Actions taken with growth mindset
   - How it shaped future approach

3. **What are your goals for the upcoming period?**
   - 3-5 SMART goals
   - Business outcome focus
   - Security and scalability alignment

### Reference Files

- `reflection/reflection-questions.md` - Official FY26 reflection questions
- `reflection/performance-philosophy.md` - GitHub's performance framework
- `reflection/reflection-experience-guide.md` - Comprehensive reflection guide
- `reflection/contributions_template.md` - Template for organizing contributions

---

## Providing Peer Feedback

### Step 1: Create Notes File

Copy the template for your recipient:

```bash
cp feedback/recipient_template.md feedback/recipients/[name]_notes.md
```

### Step 2: Gather Your Thoughts

Fill out the template with:
- **What they did really well** - Specific examples with impact
- **Most important area to focus on** - Constructive feedback with context
- **Projects you worked on together** - Collaboration examples
- **Other notes** - Additional observations

### Step 3: Generate Final Feedback

Ask Copilot to help draft the final feedback:

```
"Using my notes in [name]_notes.md, write peer feedback for [name] using the official GitHub feedback template"
```

Copilot will use:
- Your notes and examples
- Official 3-question peer feedback format from the **Peer & Manager Feedback** Copilot Space
- GitHub Values and Manager Fundamentals for framing
- Appropriate tone and structure

### Step 4: Review and Submit

Your final feedback will be structured as:

1. **What they did really well (with clear example)**
2. **Most important thing to focus on (with clear example)**
3. **Anything else to share**

The feedback will be:
- Specific and actionable
- Grounded in GitHub Values
- Professional and supportive
- Impact-focused

### Reference Files

- `feedback/feedback-questions.md` - Official peer feedback template
- `feedback/HR-feedback-page.md` - Feedback guidance and best practices
- `feedback/recipient_template.md` - Template for organizing notes

---

## Workspace Structure

```
.
├── .copilot-instructions.md          # AI workspace guidance
├── .gitignore                         # Keeps personal data private
├── mcp.json                           # Workspace MCP configuration
├── README.md                          # This file
│
├── feedback/
│   ├── HR-feedback-page.md           # Official feedback guidance
│   ├── feedback-questions.md         # 3-question peer template
│   ├── recipient_template.md         # Template for organizing notes
│   └── recipients/                   # Your feedback notes (gitignored)
│       └── recipient_template.md     # Only this template is tracked
│
└── reflection/
    ├── contributions/                 # Your contributions (gitignored)
    │   ├── issue_docs_sparkle_tracking.md
    │   ├── list_of_other_accomplishments.md
    │   └── my_contributions_oct_nov_2025.md
    │
    ├── contributions_template.md      # Template for contributions
    ├── performance-philosophy.md      # GitHub's performance framework
    ├── reflection-experience-guide.md # Comprehensive guide
    ├── reflection-questions.md        # Official FY26 questions
    │
    └── reflection_draft/              # Your drafts (gitignored)
        └── my_reflection_draft.md
```

---

## Tips & Best Practices

### For Reflections

✅ **Do:**
- Pull contributions data early and review for accuracy
- Document accomplishments as they happen (don't wait!)
- Use specific metrics and measurable outcomes
- Highlight AI usage, security focus, and culture alignment
- Reference GitHub Values in your examples
- Set SMART goals that align with team/org priorities

❌ **Don't:**
- Leave it to the last minute
- Use vague language ("worked on several projects")
- Forget to quantify impact
- Skip the "how" - behaviors matter as much as results

### For Feedback

✅ **Do:**
- Gather examples throughout the review period
- Be specific with concrete situations
- Balance strengths with growth areas
- Frame feedback constructively and supportively
- Ground observations in GitHub Values
- Focus on impact and actionable suggestions

❌ **Don't:**
- Provide vague feedback ("great team player")
- Only focus on negatives
- Share feedback without specific examples
- Make it personal - focus on behaviors and impact

### Using AI Assistance

- **Always review and validate** AI-generated content
- Use AI to organize thoughts, not replace them
- Ensure examples are accurate and specific
- Add personal voice and authenticity
- Human judgment is essential

### Privacy & Git

Personal files are gitignored:
- `feedback/recipients/*` (except template)
- `reflection/contributions/*`
- `reflection_draft/*`

This keeps your sensitive work private while maintaining useful templates and official guidance in version control.

---

## Getting Help

- Ask Copilot: "Help me with my reflection" or "Help me write feedback for [name]"
- Reference the **Reflection** Copilot Space for official guidance
- Reference the **Peer & Manager Feedback** Copilot Space for feedback templates
- Review HR documentation in the `feedback/` and `reflection/` folders

---

## Official Resources

- [GitHub HR Zendesk - Reflections](https://github-hr.zendesk.com/)
- [GitHub Values & Leadership Principles](https://github.com/github/handbook)
- [Manager Fundamentals: Model-Coach-Care](https://github.com/github/handbook)
- GitHub Copilot Spaces:
  - `github/Reflection`
  - `github/Peer & Manager Feedback`

---

**Last Updated:** November 2025  
**FY26 Reflection Cycle**
