## Comparison Metrics Report in Power BI
**Purpose of report:** Show individual metrics compared to the group of people defined by the slicers at the top of the report. Managers will see their direct reports compared to global squad averages. ICs will see their own data compared to global squad averages.

[https://aka.ms/cs_analytics](https://aka.ms/cs_analytics)  
Pathway to report: _Support -> Support Management -> Comparison Metric Report_

- login with your `<github_handle>@githubazure.com` credentials

### Filtering your data
This report pulls from both Zendesk and Workday data, and some of the selections can be counter-intuitive. It is important to be very clear about what you have chosen before you worry about the results you are seeing. As you select various slicers, the report will limit the options available in other slicers. The order in which you select things does matter.

![Screenshot1](https://github.com/github/support/assets/120742707/b6e84706-511c-4573-a87f-d063a2c13715)

#### Workday Slicers:
- Manager Name (this doesn't do much, PBI limits you to your own data if you're an IC, or your direct reports if you're a manager.)
- Employee Title - Position in the Job Info section of an employee profile
- Squad Assigned 1 - Primary Support Squad
- Squad Assigned 2 - Secondary Support Squad

#### Zendesk Slicers
- Assignee Name - Current person assigned to ticket
- Team - Support entitlement of the ticket. IMPORTANT: if you are in Enterprise Support, select `Enterprise`, `Premium Plus` _and_ `Premium Standard`. Otherwise the group data will be wrong.
- Squad - As dictated by the category of the ticket
- Region Name - As indicated on the ticket
- Month - based on the open date of the ticket

#### Reset button
The reset button is your friend. When you’ve clicked on too many things and gotten lost, or have any doubts about the data you're seeing, click this to start over.<br>
![Screenshot2](https://github.com/github/support/assets/120742707/347502cd-f767-409d-bd40-6707723a504e)


### Recommended settings for _ICs_ looking at their results compared to their squad
These settings should generally work, but it is still a good idea to "sanity check" the results you get, as the numbers could be skewed if any of the slicers are set up incorrectly, or there's a master data problem.

- Select the support 'Team' such as Enterprise or Technical to restrict the group to tickets assigned to a specific support entitlement. If you need to select multiple items, hold down the `Command` key on a Mac, or `Ctrl` on a Windows machine. 
- Select the `Squad Assigned` of the person whose results you want to see. If you change squads, this only reflects current state, so your numbers may look odd for a few months as you'll be comparing work you did in your last squad to the averages of your current squad. 
- Select yourself as the `Assignee Name` in order to see results. If your name is not there, then one of the settings above is excluding them. If the Workday setting for `Primary Support Squad` is incorrect, you will need to have this corrected before you can proceed.

### Recommended settings for _Managers_ looking at individual results compared to their squad
This is written from a manager perspective, ICs won't see much here. These settings should generally work, but it is still a good idea to "sanity check" the results you get, as the numbers could be skewed if they are combined with contractor results.

- Select the support 'Team' such as Enterprise or Technical to restrict the group to tickets assigned to a specific support entitlement.  If you need to select multiple items, hold down the `Command` key on a Mac, or `Ctrl` on a Windows machine. IMPORTANT: if you are looking at data for Enterprise Support, select `Enterprise`, `Premium Plus` _and_ `Premium Standard`. Otherwise the group data will be wrong.
- Select the `Squad Assigned` of the person whose results you want to see.
- Select the `Assignee Name` of the person whose results you want to see. If their name is not on the list, then one of the settings above is excluding them. If the Workday setting for `Primary Support Squad` is incorrect, you will need to have this corrected before you can proceed.
- Take a look at the `Employee title` slicer to see if there are roles you would not expect to see in the group, such as contractors, or members of another team. This is mostly useful for troubleshooting troublesome data.
 
**Important:** Review the numbers you are seeing for the group, and make sure they make logical sense according to what you know about the squad and team in general, and confirm your settings before reviewing the data with your ICs.

### Examples of how the filters work
#### Team
Limits to tickets assigned to the support entitlement, not an HR org structure. If someone works a ticket outside their normal team, which is fairly common, they will show up on reports for that support entitlement. Starting off with the `Team` is a quick way to limit the other variables available to you. The number of tickets you might not count for an individual is usually minimal. <br>
![team](https://github.com/github/support/assets/120742707/da962c52-eecf-4f3f-b943-32ee8ed0685b)

#### Employee Title
If you select `Employee Title`, the results will only compare the assignee to other people with the same title. Once you select an `Assignee`, the only selection you see will be the Assignee's role, but the system will still remember if you selected multiple values for the group comparison. This is useful for figuring out which roles worked tickets in group before you select a person, so it’s also good for troubleshooting if your results seem off. Please note that this is a business controlled field, not something HR really uses, so there can be a lot of variations in these values. <br>
![title](https://github.com/github/support/assets/120742707/7170d5f6-3d08-40c8-a303-aec45bd542d3)<br>

#### Squad Assigned
If you select Squad Assigned, the `Assignee` field will show people assigned to that squad, less any filters applied in the top row and `Employee Title`.<br>
![squad_assigned](https://github.com/github/support/assets/120742707/50288c64-1595-4fb7-b9ab-b9925af5ea96)

