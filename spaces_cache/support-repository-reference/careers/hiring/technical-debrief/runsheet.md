# Technical Debrief - Interview Run Sheet

**GitHub Values Assessed:** Customer-Obsessed, Ship to Learn, Growth Mindset, Own the Outcome, Better Together

## Scoring Overview

| Score Range | % | Assessment | Recommendation |
|-------------|---|------------|----------------|
| 31-36 | 84-100 | Exceptional | Hire |
| 25-30 | 69-82 | Meets Expectations | Hire |
| 0-24 | <67 | Does Not Meet Expectations | Do Not Hire |

**Total Possible:** 36 points (12 per question × 3 questions)

---

## Debrief Goals (What We Validate)

- **Authenticity:** Does the candidate truly understand their answers and can explain them in their own words and outline next steps?
- **Technical Safety:** Does the candidate avoid risky or destructive actions and show awareness of safe troubleshooting?
- **Practicality:** Are the candidate's steps logical, efficient, and realistic for solving the problem in a real-world setting?

---

## 45-Minute Agenda

| Time | Section |
|------|---------|
| 0–5 min | Set context — "We'll walk through some of the questions in the Technical Assessment done earlier, validate reasoning, and discuss how you arrived at the answer." |
| 5–10 min | Candidate summary — "In 2–3 minutes, summarize your approach to the Technical Assessment. What did you check first, any assumptions, and what resources were used?" |
| 10–40 min | Deep dives (3 × ~10 min each) |
| 40–45 min | Wrap-up & candidate questions |

**After the interview:** ~15 minutes to enter feedback into iCIMS

**Questions covered:**
- C2C: Q1 CI/CD Pipeline
- Worktent: Q5 Unauthorized message when using Copilot in VS Code
- GHES: Q7 Sudden Disk Growth – First Diagnostic Steps

---

## Scoring Rubric

There are 12 points possible for each question (4 criteria × 1–3).

| Criteria | Exceptional (3) | Meets (2) | Needs Improvement (1) |
|----------|-----------------|-----------|----------------------|
| **Understanding & Reasoning** | Explains why choices are correct/incorrect; distinguishes similar signals; restates scenarios in their own words. Proactively explains AI use (research/drafting), validates & adapts outputs, demonstrating real understanding. | Mostly correct explanations; minor gaps; recovers with hints. AI used reasonably; some adaptation; can defend answers at a practical level. | Cannot defend choices; confused concepts; memorized phrasing. Verbatim AI use without understanding; cannot explain trade-offs or next steps. |
| **Diagnostic Methodology & Next Steps** | Sequenced plan; verification loops; minimal-risk first steps; clear exit criteria; adapts to new info. | Reasonable steps; some specifics (commands/logs); partial validation loop. | Vague/non-sequenced; no validation; jumps to fixes. |
| **Safety & Risk Awareness** | Spots unsafe actions immediately; conservative posture; good expectation setting. | Generally safe; minor lapses corrected when prompted. | Defends unsafe actions; misses significant risk. |
| **Communication & Customer Skills** | Clear, empathetic, structured; references docs appropriately; avoids firm time promises. | Mostly clear; workable structure; minor tone gaps. | Hard to follow; over-promises; misses key guidance. |

---

## Q1: CI/CD Pipeline Troubleshooting (~10 min)

**Context:** Candidate selected options about troubleshooting failing CI/CD pipelines. Correct answers demonstrated systematic diagnosis, root cause analysis, and prevention strategies.

**Correct Answers:** A, C, D

### Probing Questions

**1. "Walk me through the option(s) you selected. Why did you choose them over the others?"**
- Targets: Understanding & Reasoning
- Good answer: Explains systematic troubleshooting—checking logs, identifying root cause, coordinating with team, adding prevention. Recognizes weaker options just retry without diagnosis or disable instead of fix.

**2. "If you encountered a vague error message, what's your step-by-step approach to isolate the root cause?"**
- Targets: Diagnostic Methodology & Next Steps
- Good answer: "First check logs, then compare recent changes. Add diagnostic logging at key steps. Try to reproduce locally. Narrow down by disabling parts of the pipeline until I find the failing component."

**3. "One option mentioned 'clearing caches and retrying.' When is that appropriate vs. when could it mask the real issue?"**
- Targets: Safety & Risk Awareness, Understanding & Reasoning
- Good answer: "Cache clearing is valid for known cache corruption issues. But if you don't understand why it failed, you're just hiding the problem—it'll come back. Always diagnose first."

**4. "How would you communicate progress to stakeholders while you're still troubleshooting?"**
- Targets: Communication & Customer Skills
- Good answer: "Acknowledge receipt, share what I'm investigating. Keep them informed without overpromising."

**5. "After fixing the issue, what would you do to prevent it from recurring?"**
- Targets: Diagnostic Methodology, Safety & Risk Awareness
- Good answer: "Add validation checks to the pipeline, document the fix, share with the team, consider monitoring/alerting for early detection."

---

## Q5: Copilot Unauthorized Error (~10 min)

**Context:** Customer reports all developers see "unauthorized" in VS Code. They asked us to confirm outage status, complete their automation script, and add security recommendations.

**Correct Answers:** B, C, D, G, J

### Probing Questions

**1. "The customer asked us to finish their script. Walk me through what you selected and why."**
- Targets: Understanding & Reasoning, Communication & Customer Skills
- Good answer: "I'd politely explain scripting is outside support scope, but offer guidance—recommend least-privilege tokens, code review, logging non-sensitive data. Still helpful without writing it for them."

**2. "Why is it important to start with manual troubleshooting before automation? What specific steps would you recommend?"**
- Targets: Diagnostic Methodology & Next Steps
- Good answer: "Manual checks isolate the issue first. Have one user sign out/in, check extension version, verify seat assignment. This tells us if it's auth, licensing, or something else before automating blindly."

**3. "How would you distinguish between an authentication issue and a licensing issue based on the 'unauthorized' error?"**
- Targets: Understanding & Reasoning, Diagnostic Methodology
- Good answer: "Auth issues relate to SAML/SSO, tokens, session expiry. Licensing is about seat assignment. I'd ask about recent SAML/SCIM changes, check if org-wide or user-specific, and verify seats in admin console."

**4. "One incorrect option suggested telling the customer there's a known outage. Why is that problematic?"**
- Targets: Communication & Customer Skills, Understanding & Reasoning
- Good answer: "The status page showed Copilot operational. Claiming an outage when there isn't one is inaccurate and damages trust. Always verify before stating."

**5. "If they proceed with building automation internally, what security practices would you advise?"**
- Targets: Safety & Risk Awareness
- Good answer: "Use least-privilege tokens, never store credentials in scripts, use secret managers, log only non-sensitive metadata, and run it through normal code review."

---

## Q7: GHES Disk Growth Diagnostics (~10 min)

**Context:** Data volume rapidly growing. Candidate selected diagnostic commands.

**Correct Answers:** A, B, E

### Probing Questions

**1. "Explain what each command you selected does and what information it gives you."**
- Targets: Understanding & Reasoning
- Good answer: "`df -h` shows filesystem usage overview. `du -sh /data/*` shows which directories are consuming space. `lsof +L1` finds deleted files still held open by processes—common cause of phantom disk usage."

**2. "One of the options was `kill -9 -1`. What does that command do and when would it be appropriate to use?"**
- Targets: Safety & Risk Awareness, Understanding & Reasoning
- Good answer: "That kills all processes the user can signal—could crash the system. It's destructive without any diagnosis. Never appropriate as a first step in troubleshooting."

**3. "What's the 'deleted-but-open file' scenario and how would you detect it?"**
- Targets: Understanding & Reasoning, Diagnostic Methodology
- Good answer: "When a file is deleted but a process still has it open, the space isn't freed until the process releases it. `df` shows full but `du` totals don't match. `lsof +L1` finds these orphaned file handles."

**4. "Once you've identified a runaway log file, walk me through how you'd safely resolve it."**
- Targets: Diagnostic Methodology & Next Steps, Safety & Risk Awareness
- Good answer: "Truncate rather than delete if process is still running—keeps the file handle valid. Or gracefully restart the process, then remove the file. Check log rotation config to prevent recurrence."

**5. "If this were a customer-reported issue, what would you ask them before running any commands, and how would you set expectations?"**
- Targets: Communication & Customer Skills
- Good answer: "Ask when it started, any recent changes, what's impacted. Acknowledge the issue, explain I'm investigating. Preserve logs before making changes."

---