# Onboarding Support Engineers

This onboarding guide is for managers and assigned "buddies" of newly hired team members to provide an overview of what to do with a new hire. Feel free to break out of this guide whenever you think it's necessary and improve it afterwards.

## Buddy Checklist

- [ ] Add the new hire's account to some teams on GitHub.com. The most important teams are handled through [entitlements](https://github.com/github/entitlements), but you will also want to add the new hire to their team. If you don't have access, please ask a team maintainer to add them:
  - [Support Teams](https://github.com/orgs/github/teams/support/teams)
  - [Enterprise Support](https://github.com/orgs/github/teams/enterprise-support/teams)
  - [Security and Revenue Support](https://github.com/orgs/github/teams/support-security-revenue)
  - [Technical Support](https://github.com/orgs/github/teams/support-technical)
  - [CRE APAC](https://github.com/orgs/github/teams/cre-apac)
  - [CRE EMEA](https://github.com/orgs/github/teams/cre-emea)
  - [CRE AMER](https://github.com/orgs/github/teams/cre-na)

- [ ] Set up access to Zendesk
  - [ ] Run `.zd user_list refresh` to refresh Zendesk chatops user list
  - [ ] Run `.zd user_list [username]` to check the user has been added to the Zendesk chatops user list
  - [ ] Check the status of the user's onboarding items using  `.es onboard USERNAME`
  - [ ] Open an [Agent Change Request issue](https://github.com/github/zendesk/issues/new?assignees=&labels=Admin%3AAgent+Change+Request%2C+Instance%3ASupport&template=Add+or+Modify+Agent+in+Zendesk.md&title=Agent+Change+Request%3A+%5BName+of+agent%5D) in github/zendesk to promote to a full agent
   

## Remote onboarding

- Week 1: Company wide orientation program via the [github/onboarding](https://github.com/github/onboarding) repository
- Week 2: Revenue and CRE onboarding program via the [github/revenue-onboarding](https://github.com/github/revenue-onboarding) repository
- Week 3: Enterprise, Technical Support onboarding program via the [github/onboarder-next](https://github.com/github/onboarder-next) repository
- Week 3: Security and Revenue Support onboarding program via the [github/srs-onboarding](https://github.com/github/srs-onboarding/tree/main) repository

Of course, these weeks are just the start, it takes months to get fully up to speed on the Support team. Nobody should feel as though they have to know everything, just because the first onboarding weeks are up!

## Enterprise, Technical and Security and Revenue Support new hires

We use [onboarder-next](https://github.com/github/onboarder-next) for Enterprise and Technical and [github/srs-onboarding](https://github.com/github/srs-onboarding/tree/main) for Security and Revenue to manage all of the activities a new hire (and their buddy) need to complete in their first three weeks (and beyond).

For Enterprise and Technical you will use [onboarder-next](https://github.com/github/onboarder-next) to create a repository for the new hire under the [ghe.io/new-hires](https://ghe.io/new-hires/) organization. The resulting repository includes a Milestone for specific weeks (weeks 1, 2, 4, 8, 12 and 20) and an Issue for each activity.

For Security and Revenue you will use [github/srs-onboarding](https://github.com/github/srs-onboarding/tree/main) to create a repository with the relevant issues based on the new hires squad assignment.

In preparation for onboarding (especially if you haven't onboarded someone before), you'll want to setup the relevant repository under your own GitHub.com account to become familar with the content. These are exactly the same steps you have to do for the new hire, so this is good preparation.

Before onboarding week 1 begins, read through the activities listed in these issues and make sure you know how to do each one, or ask for help if you don't (or if you don't have access to something).

For Enterprise and Technical Support the issues are generated from the YAML files in the [onboarder-next/data](https://github.com/github/onboarder-next/tree/master/data) folder.

## Week 1

During GitHub onboarding, a new Support Engineer will spend a lot of time going through the general onboarding procedures, like getting their laptop set up and talking with other teams to learn how GitHub works; this is detailed in [onboarding overview](https://github-hr.zendesk.com/hc/en-us/articles/8447156815380-Onboarding-at-GitHub) on GitHubber which you should read.
During the first few days, there won't be much time to tackle the Support specific activities, but feel free to try to fit in as many Support related things into the first week as possible - without overwhelming your new teammate, of course.

### Day 1

The first day of onboarding is pretty tight and new hires will start setting up their new laptops. 

### Day 2

Day 2 can feel like Day 1. There are still a lot of meetings scheduled for your new hire and lots of information to digest. So, keep things simple and have them look in their new personal onboarding repository at some of the things you're going to spend more time on over the next couple of weeks. 

### Day 3

This will likely be the first full day you'll have with the new team member. It's time to meet for some serious business, start looking at GitHub Enterprise and how we run support here at GitHub. There may still be some meetings scheduled for your new hire throughout the day, so don't stress out if you don't get far through the list.

### Day 4

Week 1 can be overwhelming for both the new hire as well as the buddy. For Enterprise and Technical Support, If you don't get through all the activities in their new personal onboarding repository milestone for week 1, you can tackle these at the start of week 2.

## Week 2

Week 2 will be focused on Revenue onboarding, but there should be much more time to look at GitHub Enterprise and Support than week 1. There'll be little to no meetings scheduled for your new colleague, allowing you to pair on tickets and utilities we use to get the job done.

For Enterprise and Technical Support start this week by addressing any activities that didn't get completed in the milestone for week 1.

# Onboarding new Enterprise Support hires into the on-call rotation

When both the buddy and the new hire agree it's time, new people should be onboarded into the urgent queue. Typically this will start at around three months in, but could be sooner or later depending on how comfortable the new team member is with taking on the challenge. Your manager will be part of this discussion too.

To prepare for inclusion into the urgent queue, they should:

- Review our documentation on [urgent tickets](../ticket-processes/urgents.md).
- Read all incoming urgent tickets for a while before joining. A good practice technique is to read the initial request and write a response before reading how the on-call engineer responded.
- Take an active role when there's an urgent ticket in progress. For example, they might help out by doing code dives, searching for previous related tickets, or related GitHub issues.
- Ensure they're properly set up in [PagerDuty](../tools/pagerduty.md) and run a test page.
- Once they have spent some time working on urgent tickets during the week, they can go into the weekend rotation as well.

If you've got any concerns, talk to your team or manager.
