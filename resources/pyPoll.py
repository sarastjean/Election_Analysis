# The data we need to retrieve
# 1. The total number of votes to cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.
# Assign a variable for the file to load and the path.
#file_to_load = 'Resources/election_results.csv'
#Open the election results and read the file
#with open(file_to_load) as election_data:
    # To Do: Perform Analysis
 #   print(election_data)
# Close the file
#election_data.close()

#add our dependencies
import csv
import os
# Assign a variable to load a file from a path
file_to_load = os.path.join("Resources/election_results.csv")
#Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")
#Open the election results and read the file
with open(file_to_load) as election_data:
    # To do: read and analyze the data here
    #Read the file object with the reader function
    file_reader = csv.reader(election_data)
    # Read and print the header row
    headers=next(file_reader)
    print(headers)

#file_to_save = os.path.join("analysis", "election_analysis.txt")
#with open(file_to_save, "w") as txt_file:
 #   txt_file.write("Counties in the Election\n------------------\nArapahoe\nDenver\nJefferson")


