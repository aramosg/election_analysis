# Election_Analysis
Module 3 - Python and PyPoll

## Project Overview
A Colorado Board of Election employee has given us the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidate who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winned of the election based on popular vote.

## Resources
- Data Source: election_results.csv
- Software: Python 3.9, Visual Studio Code, 1.66.0

## Summary
The analysis of the election shows that:

### Total votes in the election
- There were 369,711 votes cast in the election.

### The Counties

Counties were votes were cast:
1. County Denver: 82.8% (306,055)
2. County Jefferson: 10.5% (38,855)
3. County Arapahoe: 6.7% (24,801)

- Largest County Turnout: **Denver**

### The Candidates
- The candidates were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane

- The candidate results are as follows:
    - Charles Casper Stockham received 23.0% of the vote, that is 85,213 votes.
    - Diana DeGette received 73.8% of the vote, that is 272,892 votes.
    - Raymon Anthony Doane received 3.1%  of the vote, that is 11,606 votes.

- The **winner** of the election was:
    - Candidate **Diana DeGette**, who received **73.8%** of the vote, with **272,892 votes**.

## Election-Audit Summary
Although this script is powerful enough to hande a medium size election, some changes may be needed to be able to handle a national election. The following list is a proposal of modifications to enable this script to handle bigger elections:

### 1 - Standardization and expansion of required information
Although the current data entry (CSV file) is enough to handle one state, it may not be the case for a national election. We need to expand the details provided. We may want to fields such as State, ZIP code, or region ID to be able to differentiate between states, regions, and counties. If we limit ourselved to "County name", we may encounter duplicates when dealing with a national election. 

### 2 - Optimized reports
Currently, the script is creating a txt file as a final report. This report includes the list of candidates and the amount of votes for each of them. Also, the report includes the county with the largest share of votes. Although this works for a few counties, a report like this for a national election is not practical. The suggestion is to produce a CSV file, containing relevant data as columns. This way, the data can be exported into Excel and create some reports (graphs, dahsboards) depicting the whole story about the election. Of course, we can print a highlights summary, describing the winners. But, for general statistics, voting share, and percentages, a CSV file tobe exported into Excel may be a better idea.

### 3 - PDF reports
A PDF report containing the details may not be friendly enough as a CSV file.  But, creating a PDF with the highlights can be very useful. The main purpose of the PDF report will be to convey the highlights of the election: winners, counties/states with the biggest share of votes, and so on. Creating the CSV file, together with a PDF report like the one we are describing can be a good idea. 

### 4 - Database connectivity
Our Python script can be enabled to connect to a remote database, read election data and perform the same analysis. The final report can also be inserted into the database. This will allow us to be more efficient when handling the data. Also, having access to a database can enable us to store historic data more easily. 

## Conclusion
As we explore during this module, creating a Python script to analyze data is relatively easy. This, combined with a well defined and structured data source, makes reading data and performing basic analysis an effortless task. When designing software, it us always a good practice to write software which is scalable, that means, code that can be easily modified or extended to perform more complex tasks. And that is precisely what we have done for this challenge. This script is a good start. This is the foundation for implementing richer features that will allow us to produce analysis with bigger data sets or perform largest calculations. 