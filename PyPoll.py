
# Adding dependencies
import csv
import os

# Assing a variable a file to load
file_to_load = os.path.join("resources", "election_results.csv")

# Creating a file to write data
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Variable to store the total number of votes in the election
total_votes = 0

# List to store the different candidates in the election
candidate_options = []

# Dictionary to store the number of votes for each candidate
candidate_votes = {}

# Winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# We can use "with" to open a file without worrying about closing the buffer
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    
    # Print the header row - skipping headers
    headers = next(file_reader)

    for row in file_reader:
        total_votes += 1
        candidate_name = row[2]
        
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0 # This initialized the count for the candidate
        
        candidate_votes[candidate_name] += 1 # this incrases in one unit the vout count for the candidate

    with open(file_to_save, "w") as txt_file:

        # Print the final vote count to the terminal
        election_results = (
            f"\nElection Results\n"
            f"-----------------------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-----------------------------------------\n"
        )
        print(election_results, end="")

        #Save the finel vote count to the text file
        txt_file.write(election_results)
    
        # Calculating the percentage of votes for each candidate
        for candidate_name in candidate_votes:
            # Retrieve the vote count
            votes = candidate_votes[candidate_name]

            # Calculating the percentage of votes
            vote_percentage = float(votes) / float(total_votes) * 100

            # Printing candidate name and his/her percentage
            candidate_results = f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n"
            print(candidate_results)
            txt_file.write(candidate_results)

            # Determine winning vote count and candidate
            # Determine if the votes is greater than the winning count
            if(votes > winning_count) and (vote_percentage > winning_percentage):
                winning_count = votes
                winning_percentage = vote_percentage
                winning_candidate = candidate_name

        # print(f"Total votes: {total_votes}")
        # print(f"Candidate options: {candidate_options}")
        # print(f"Candidate votes: {candidate_votes}")
        winning_candidate_summary = (
            f"-----------------------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"-----------------------------------------\n"
        )
        print(winning_candidate_summary)
        txt_file.write(winning_candidate_summary)