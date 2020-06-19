#add our dependencies
import csv
import os
# Assign a variable to load a file from a path
file_to_load = os.path.join("Resources/election_results.csv")
#Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Initialize a total vote counter
total_votes=0

#Candidate Options and candidate votes
candidate_options = []
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row
    headers=next(file_reader)
    #Print each row in the CSV file
    for row in file_reader:
        #2. Add to the total vote count
        total_votes += 1
        #Get the candidate name from each row
        candidate_name=row[2]

        #If the candidate does not match any existing candidate....
        if candidate_name not in candidate_options:
            # Add it to the list of candidate
            candidate_options.append(candidate_name)
            #Begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0
        #Add a vote to that candidate's count
        candidate_votes[candidate_name] +=1

#Determine the percentage of votes for each candidate by looping through 
#1. Iterate through the candidate list
for candidate in candidate_votes:
    #2. Retrieve vote count of a candidate
    votes = candidate_votes[candidate]
    #3. Calculate the percentage of votes
    vote_percentage = float(votes) / float(total_votes) * 100

    #4. Print the candidate name, vote count and percentage of votes
    # votes to the terminal
    print(f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")

    #Determine winning vote count and candidaate
    #Determine if the votes is greater than the winning count
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_candidate = candidate
        winning_percentage = vote_percentage

winning_candidate_summary = (
    f"-----------------------\n"
    f"Winner: {winning_candidate}\n#"
    f"winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"------------------------\n")
print(winning_candidate_summary)



