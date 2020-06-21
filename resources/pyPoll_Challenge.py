#add our dependencies
import csv
import os
# Assign a variable to load a file from a path
file_to_load = os.path.join("Resources/election_results.csv")
#Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Initialize a total vote counter
total_votes = 0

#Create a list for the counties / create dictionary for county votes
county_options = []
county_votes = {}

# Largest County Tracker
largest_county = ""
largest_count= 0
largest_percentage = 0

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

    #Loop through county names; if county name has not been recorded, add to list
    for row in file_reader:
        total_votes += 1
        county_name = row[1]
        if county_name not in county_options:
            county_options.append(county_name)
            county_votes[county_name] = 0
        county_votes[county_name] +=1

        candidate_name=row[2]
        #If the candidate does not match any existing candidate....
        if candidate_name not in candidate_options:
            # Add it to the list of candidate
            candidate_options.append(candidate_name)
            #Begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0
        #Add a vote to that candidate's count
        candidate_votes[candidate_name] +=1

#Save the results to our text file
with open(file_to_save, "w") as txt_file:
    #Print the final vote count to the terminal
    election_results = (
        f"\nElection Results\n"
        f"---------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"----------------------\n")
    print(election_results, end="")
    txt_file.write(election_results)

    county_results = f"\nCounty Votes:\n"

    #print county results
    for county in county_votes:
        votes = county_votes[county]
        vote_percentage = float(votes) / float(total_votes) * 100
        county_results = county_results + f"{county}:{vote_percentage:.1f}% ({votes:,})\n"
        print(county_results, end="")
        if(votes > largest_count):
            largest_count = votes
            largest_county = county
    txt_file.write(county_results)
        
    largest_county_summary = (
        f"---------------------------\n"
        f"Largest County Turnout: {largest_county}\n"
        f"----------------------------\n")
    print(largest_county_summary)
    txt_file.write(largest_county_summary)

    for candidate in candidate_votes:
        #Retrieve vote count of a candidate
        votes = candidate_votes[candidate]
        #3. Calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate}:{vote_percentage:.1f}% ({votes:,})\n")

        #Print each candidate's voter count and percentage to the terminal
        print(candidate_results)
        txt_file.write(candidate_results)
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
    #save the winning candidate's results to the text file
    txt_file.write(winning_candidate_summary) 


