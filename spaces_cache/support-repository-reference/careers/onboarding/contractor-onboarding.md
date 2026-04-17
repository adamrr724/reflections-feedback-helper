## Contractor Onboarding 

**Before day 1**

- Mail Yubikeys to each contractor immediately
- Email the contractor team and prompt each one to create a GitHub account. 
  - Make sure the handle is less than 21 characters, as Slack has username length constraints. 
- Open an issue in procurement to kick off the process on GitHub's end ([Example](https://github.com/github/procurement/issues/3966))
  - Expect this to take 3-5 days minimum

**Access**
1. In `entitlements`, add the contractors to their expected team, [like so](https://github.com/github/entitlements/pull/23085/files)
2. If Yubikeys haven't yet arrived, you can add contractors to a short term bypass list, [seen here](https://github.com/github/entitlements/pull/24697/files)
3. Prompt your contractors to replace their primary email for GitHub with their new GitHub email
4. Make sure your team has access to GitHub. This _should_ happen automatically, have the team check email for an invite, otherwise IT will need to assist. This likely influences Slack invites.

- For access to the Hub, use PR's for [internal-apps-access](https://github.com/github/entitlements/pull/23912/files) 
- For access to Biztools, open a PR [here](https://github.com/github/entitlements/blob/master/ldap/pizza_teams/devtools-contractors.txt), and [a request](https://github.com/github/security-iam/issues/3514) in `security-iam`.
- For Looker access, look [here](https://github.com/github/entitlements/pull/24879/files)
- For Edutools, look [here](https://github.com/github/entitlements/pull/24859/files)
- For Zendesk, open an issue [here](https://github.com/github/zendesk/issues/new?assignees=&labels=Admin%3AAgent+Change+Request%2C+Instance%3ASupport&template=Add+or+Modify+Agent+in+Zendesk.md&title=Agent+Change+Request%3A+%5BName+of+agent%5D).

**Risks**
- Make sure that the assigned manager to the contractors is available to approve entitlement PR's quickly. 
  - If the direct manager isn't available, but the skip level manager has given approval, update the PR with the `needs-human-review` label.
- Consider how granular your team access needs to be overall. 
  - If all contractors for your team can have the same access perpetually, you should instead add the team to each entitlement above, and in the future only worry about one entitlement PR -- adding new contractors to the team.


  
