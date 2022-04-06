
# Adding dependencies
import csv
import os

# Assing a variable a file to load
file_to_load = os.path.join("resources", "election_results.csv")

# Creating a file to write data
file_to_save = os.path.join("analysis", "election_analysis.txt")

# We can use "with" to open a file without worrying about closing the buffer
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    
    # Print the header row 
    headers = next(file_reader)
    print(headers)

