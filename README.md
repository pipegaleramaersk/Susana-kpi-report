# DEI Diversity Metrics report

- KPI 1: Percentage of teams with less than 30% representation of a gender within the team. Gender is limited to 'Female' and 'Male'.
- KPI 2: Percentage of teams with more than 30% representation of on a certain nationality within the team.

- Ruled out: every employee that do not report to a CEO-3 UID and every employee with +2 Job Levels distance with their manager.
  

# Metodology details

- Please note that given the current Workday structure leaders are not included in the KPIs of the teams that they lead (e.g. Pete Jaworski do not count in the KPIs of PD&A team, but he does for Shalini Nataraj's team)
  
- Teams with more less than 5 people are included in the analysis. Meaning that we can find, for example, 100% Male teams in Teams of only 2 males - and they are part of the KPI. Removing them would imply cutting by more than half the number of teams for the analysis (252 out of 419 teams have less than 5 members)

- Some Job levels are not accurate (e.g. managers with Job Level 0). In cases that the difference of the Job Level of the UID with the manager is negative because of this, it is assumed that the job distance is less than 2 and therefore keep in the KPI analysis. Example: An employee has a JL 4, her Manager has a JL 0, I assumed that the distance is not more than 2 job levels and keep them for analysis. 

- 415 Teams were considered for the Gender analysis, as there are 4 teams with all their members missing gender or being unknown.

- 407 Teams were considered for the Nationality KPI, as for 12 teams their most representative in percentage terms Nationality was 'Unknown'.

# Data details

- Raw Workday/Point dataset: 64,960 employees (filter details below).
- Processed dataset after filtering out everyone that do not report to CEO-3+, and removing employees with +2 Job Levels distance with their manager: 2159 employees
- Teams in Point is determined as "Organizational Unit Title".
- 419 Teams are left with the above restrictions in those 2159 employees.



# Data Source details

Point Power BI filter details:

- Data source: Azure Analysis Services (Point)
- Data extraction date: 05/10/2022 - 17:01:15
- Employee Unique ID: is not black
- Employment Status: Active
- Organisation Level 01 Title: APMM CEO
- Organisation Level 02 Title: A.P.Moller Maersk
- Year: 2022
- Report Month: 2022, September
