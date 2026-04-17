# Codility Technical Assessment

**Format:** Codility (asynchronous)  
**Duration:** 60 minutes  
**Benchmark Score:** 60%  
**Link:** [Codility Test #344485](https://app.codility.com/tests/344485/details/)

---

## Scoring

- **Multiple-response questions**
- **Strict Matching:** Candidate must select exactly the correct options (and nothing else) to get points
- **Automatically scored by Codility**

---

## Question 1: CI/CD Pipeline Troubleshooting

**Question Text:**

> Describe a situation where you had to troubleshoot and debug a failing CI/CD pipeline. How did you approach the problem, and what tools or techniques did you use to identify and fix the issue?
>
> Select all options that truly demonstrate advanced troubleshooting, technical depth, and robust prevention strategies for CI/CD failures. Some options may sound reasonable; choose only those that are complete and reflect best practice.

**Options:**

A. On recurring deployment failures, I checked pipeline logs for anomalies and compared to recent changes. I traced the error to a missing environment variable, added diagnostic logging at critical steps, updated the pipeline to set required variables, and introduced automated checks to prevent similar mistakes going forward.

B. When a CI/CD build failed with a vague error, I re-ran the job several times, reverted the last change, and cleared build caches. This resolved the issue, so I documented these steps as a troubleshooting checklist.

C. For unexplained issues in the test stage, I recreated the pipeline locally, reviewed the build configuration for misconfigurations, and coordinated with teammates to inspect external dependencies. The fix involved amending test script permissions and updating the build environment documentation.

D. During repeated integration failures, I analyzed log output for patterns, cross-referenced environment settings with prior successful runs, and used shell commands to verify runtime differences. I patched a misconfigured integration secret and added a validation step to the build process, sharing the solution with the team.

E. Faced with unpredictable stage failures, I disabled the problematic stage temporarily and reached out to support services for analysis. After release, I planned a retrospective and considered additional monitoring for future cases.

**Correct Answers:** A, C, D

---

## Question 2: Code Security Issue

**Question Text:**

> What is an example of a code security issue you've encountered (dependencies or code analysis)? What steps did you take to resolve the issue? If you don't have a specific example, what are some things you would check or tools you might use to investigate?
>
> Select all options that fully demonstrate advanced security understanding, technical depth, and robust remediation. Partial or reactive approaches may sound valid; choose only those that meet the highest standards for end-to-end security practice.

**Options:**

A. Upon discovering a high-severity CVE in a dependency, I verified our usage by tracing the affected functions via code search and dependency graphs. I recreated the vulnerability in a test branch, upgraded to a patched version, and ran regression and security tests afterwards. I documented the incident and set up ongoing automated audits for similar issues.

B. When a static analyzer flagged unsafe input handling, I reviewed the affected code and suggested changing it to use parameterized queries. I checked for similar patterns in related modules and arranged code review sessions focused on input validation practices.

C. If alerted about a security risk by an external party, I consulted public vulnerability databases for impact and severity, confirmed exploitability in our stack, and worked with other teams to update dependencies, keeping records of changes in both project documentation and compliance reports.

D. For recurring alerts from dependency scanners, I regularly updated packages to their latest versions through automated pull requests. I wrote a brief summary in the team's sprint notes for tracking but did not conduct additional manual verification unless a package was a direct business requirement.

E. Faced with a remote code execution warning, I removed the vulnerable dependency, blocked its installation in CI, evaluated the impact with business leads, and introduced runtime monitoring for related threat signatures.

**Correct Answers:** A, B, C, E

---

## Question 3: Actions Workflow

**Customer Ticket:**

> We've created an Actions workflow in a new Repository, under `/.github/workflows/` as `actions-test.yml` however my Actions workflow run jobs are not getting picked up. We're trying to use our own on-prem runners, rather than GitHub-hosted runners which seem to work, but that seems to be the only difference. What are we doing wrong?

**Workflow configuration:**
```yaml
name: Test Action

on:
  workflow_dispatch:

jobs:
  test:
    runs-on: [rhel-self-hosted, x64, us-west]

    steps:
      - uses: actions/checkout@v3

      - name: Run a one-line script
        run: echo Hello, world!
```

**Workflow run output:**
```
Requested labels: rhel-self-hosted, x64, us-west
Job defined at: mischa0083-test-ghec/action-repo-test/.github/workflows/test-action.yml@refs/heads/main
Waiting for a runner to pick up this job...
```

**Question Text:**

> You are a GitHub Support Engineer responding to the customer above.
>
> Select all responses that demonstrate exceptional, advanced troubleshooting and awareness of GitHub Actions. Each answer should be evidence-based and drive the investigation forward in a professional manner. Only answers that exemplify both correct diagnosis and actionable follow-up are considered top-tier.

**Options:**

A. Confirm with the customer whether their self-hosted runner is registered with each of the requested labels (`rhel-self-hosted`, `x64`, `us-west`), and verify the runner is showing as idle/online in repository or organization settings. Request a screenshot of runner details, last activity time, and the command used to register the runner.

B. Advise the customer to change the `runs-on` line in the workflow to use a single string label instead of an array, then re-register the runner using that label. Ask them to rerun the job with this new configuration.

C. Direct the customer to Settings > Actions > Runners in GitHub to check the availability, label match, and current status of all self-hosted runners. Ask if any runners became offline at the time of execution and request logs from the runner machine for those timestamps.

D. Suggest that the customer keeps rerunning the workflow over several hours and, if the issue persists, tries to remove one or more labels from the `runs-on` specification until a runner picks up the job.

E. Point out the requested labels in the job log and ask the customer to verify if the self-hosted runner is configured at either org or repo scope. Request a screenshot of the organization/repo runner list, and recommend checking networking (firewall, proxy) issues that could block runner communication.

**Correct Answers:** A, C, E

---

## Question 4: Code Review Usage Concerns

**Customer Ticket:**

> We recently enabled Code Reviews and noticed a sharp increase in the daily request count. Could you clarify what activities are counted as a request, whether there's any difference in how Premium versus Standard users drive that metric, and how we can monitor or fine-tune usage?
>
> We'd also like to confirm the best way to identify which users are on Premium vs Standard for adoption tracking.
>
> Additionally, a few users have reported seeing a message that they have "used up the 1000 Premium requests," and we'd like to understand what triggers that notice and whether it is expected given our current configuration.

**Question Text:**

> Below are 10 possible statements you could include in a reply to the customer.
>
> Select the 5 that are accurate and appropriate.

**Options:**

A. In an enterprise context, each Copilot seat includes the same 1,000 premium requests. There is not a distinct "Standard vs Premium" consumption tier—each assigned seat has the same included allotment.

B. A request is each time you prompt Copilot to generate, explain, or transform code (every submitted prompt or triggered response). A premium request is one of those requests that invokes a premium model or capability—such as a Copilot Code Review analysis or starting a Copilot coding agent session; ordinary inline non‑premium suggestions do not consume premium requests.

C. Model multipliers determine whether an interaction counts as a premium request.

D. After a seat uses 1,000 premium requests, premium features pause unless a budget is configured; non‑premium models remain available and no charges occur without a budget.

E. The "used up the 1,000 premium requests" message appears once the entire enterprise collectively reaches 1,000 premium requests.

F. You can identify seat holders in the Copilot license usage view and verify consumption with the monthly per‑seat usage CSV.

G. Please note that viewing the Copilot license usage page consumes a premium request each time it is opened.

H. Setting a premium request budget causes immediate per‑request billing.

I. The Copilot activity report helps correlate usage spikes (e.g., increased Code Review analyses) with premium request consumption trends.

J. Non‑premium models are disabled after quota exhaustion to prevent accidental overages.

**Correct Answers:** A, B, D, F, I

---

## Question 5: Copilot Unauthorized Error

**Customer Ticket:**

> Since yesterday all of our developers see an "unauthorized" message when trying to use Copilot in VS Code.
>
> Can you:
> - Confirm if this is a known outage.
> - Review this shell script we started (below) and finish it so it auto-checks every user's Copilot seat and re-enables access.
> - If possible, add anything else the script should do for security.

```bash
#!/bin/bash
for u in $(cat users.txt); do
  echo Checking $u
  # TODO: add seat verification + re-enable logic
done
```

> We really need a working script fast. Please just complete it for us.

**Question Text:**

> Below are 10 possible statements you could include in a reply to the customer.
>
> Select the 5 that are accurate and appropriate.

**Options:**

A. Thanks for flagging this. Our engineering team is currently investigating similar reports (see https://www.githubstatus.com) and we've shared your report for further analysis.

B. Our support scope does not include authoring or finalizing automation scripts, so we can't validate that snippet.

C. If you proceed with the script approach and pursue automation internally, we recommend using least-privilege tokens, logging only non-sensitive metadata, and reviewing the script through your normal code review processes.

D. We recommend starting with no script checks by having one affected user sign out and back in, confirm they're on the latest Copilot extension version, and verify their Copilot seat assignment to distinguish authentication from licensing.

E. When you assign licenses to an enterprise team, users gain or lose Copilot access as they are added or removed, and if you use Enterprise Managed Users you can sync the team with an IdP group to manage licensing directly from your identity provider.

F. The fastest remediation is to revoke and reassign every Copilot seat for all developers. This can often resolve access issues related to seat assignments.

G. To investigate further, please confirm no recent SAML SSO enforcement or SCIM provisioning changes took place.

H. Embedding SAML or enterprise credentials directly inside the bash script is acceptable if the file permissions are 600. 600 permissions restrict access to the file owner only, reducing the risk of credential exposure.

I. Please ask each developer experiencing an error to create a new support ticket, at support.github.com, including their personal access token, so we can centrally test seat validation and access.

J. If you have a Copilot Business or Copilot Enterprise plan, you can view enterprise Copilot usage showing assigned seat counts and total spending for the current billing cycle.

**Correct Answers:** B, C, D, G, J

---

## Question 6: Private Code Exposure Concerns

**Customer Ticket:**

> Does using an AI coding assistance tool mean our private code could be leaked outside the organization?
>
> We need to brief our security team and prepare an internal FAQ. Specifically, could you address:
> - Is any of our private repository code retained or used to train shared/global models?
> - If a suggestion looks like code we have internally, how do we tell coincidence from an exposure? Are there safeguards that reduce large verbatim outputs?
> - Is prompt/suggestion data encrypted in transit/at rest and how long is it retained in the editor vs other experiences (e.g., chat/CLI)?
> - What concrete practices should we enforce to minimize risk?
> - Can developers opt in/out of product improvement usage of their prompts?
> - What should we tell developers not to paste?

**Question Text:**

> Below are 10 possible statements you could include in a reply to the customer.
>
> Select the 5 that are accurate and appropriate.

**Options:**

A. In IDE code completion, prompts and suggestions are not retained by default. In other GitHub Copilot access certain prompt/suggestion data may be retained for a limited period, and any retained Copilot data is encrypted in transit (TLS) and at rest.

B. Private repository code you enable for Copilot is lightly indexed to improve global model relevance, so rigorous prompt hygiene and secret avoidance are optional rather than required.

C. Prompt and suggestion collection for product improvement is off by default — users (or org policy) must opt in explicitly—and users can disable collection and then request deletion of previously collected prompt/suggestion data.

D. Copilot does not use your private repository code to train shared/global models. Code you include in a prompt is processed transiently to generate suggestions and is not added to global training datasets.

E. Suggestions are never encrypted in transit because they are ephemeral; encryption only applies once data is stored.

F. If a suggestion closely resembles internal code, first search public sources to rule out a common pattern, then capture context (files, prompt, timestamp) and escalate to GitHub Support.

G. Even with granular Copilot privacy settings, some prompt metadata is still retained; to guarantee zero retention you must disable Copilot for the entire organization.

H. Recommended governance includes: avoid pasting secrets/credentials, scope enablement to teams/repos that need it, review seats & scope periodically (e.g., quarterly), and keep a lightweight change log (date, requester, rationale) for enablement changes.

I. All prompts and suggestions from every Copilot interface (IDE, chat, CLI) are retained for a minimum of two years to improve model quality.

J. Pasting proprietary algorithms verbatim into Copilot prompts personalizes the global model and is a recommended adoption strategy.

**Correct Answers:** A, C, D, F, H

---

## Question 7: Sudden Disk Growth – First Diagnostic Steps

**Question Text:**

> A data volume is rapidly growing. Which commands are most appropriate to begin isolating the issue?
>
> Select all that apply:

**Options:**

A. `df -h`

B. `du -sh /data/*`

C. `kill -9 -1`

D. `ls -lR /`

E. `lsof +L1`

**Correct Answers:** A, B, E

---

## Question 8: Safely Reclaiming Space From a Runaway File

**Question Text:**

> A huge temp file tied to a still-running process is filling the partition. What are safe remediation actions?
>
> Select all that apply:

**Options:**

A. Truncate the file after confirming it's not needed and process can recreate it

B. Remove the file while the process still has it open and immediately reboot

C. Stop or gracefully terminate the owning process, then remove the file

D. Compress the growing file in-place while it is still being appended

**Correct Answers:** A, C

---

## Question 9: Diagnosing "Zero Search Results" Reports

**Question Text:**

> All searches suddenly return zero results. Elasticsearch's ports were silently changed while the application still targets the defaults. Which signals point to a backend reachability / port misconfiguration issue rather than just an empty index?
>
> Select all that apply:

**Options:**

A. Application exceptions referencing request IDs with response nil or connection/transport errors

B. 100% of queries return zero results suddenly after a maintenance window, with entirely clean logs (no connection errors)

C. Configuration review shows Elasticsearch listening on non-default ports (9203/9303)

D. Gradually decreasing results over weeks

E. Exception count spikes while zero-result queries commence simultaneously

**Correct Answers:** A, C, E

---

## Question 10: Clarifying Questions Before Restarting a Failed Dependency

**Question Text:**

> Before restarting or editing the search backend config, what information should you gather?
>
> Select all that apply:

**Options:**

A. "When did users first notice zero results?"

B. "Were any configuration or port changes applied recently?"

C. "Can we immediately delete all index data to rebuild faster?"

D. "Are all queries affected or only certain repositories/orgs?"

E. "Has the underlying disk or memory usage spiked for the search server/container?"

**Correct Answers:** A, B, D, E
