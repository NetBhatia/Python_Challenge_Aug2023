# Import the os module
import os
# Module for reading CSV files
import csv

# File path to read the csv file from:
csvpath = os.path.join('..','Resources', 'election_data.csv')

# File path to write the summary into:
output_path = os.path.join("..", "Analysis", "Analysis.txt")

# Open and Read CSV file
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')

    # Set initial value for count of votes:
    votes_count = 0

    # Set candidate names list:
    candidate_names = []

    # Create candidate with votes count dictionary:
    candidate_votescount = {}

    # Set initial values for remaining variables for winner details:
    winner_name = ""
    winner_votecount = 0
    votes_won_percentage = 0
    
    # Skip the header
    csv_header = next(csvreader)

    # Loop through the csv file
    for row in csvreader:
        # Get total votes count:
        votes_count = votes_count + 1

        # Get candidate name from the csv file:
        candidate_name = row[2]

        # Create list of all candidates that are available in csv file and their vote counts:
        if candidate_name not in candidate_names:
            candidate_names.append(candidate_name)
            candidate_votescount[candidate_name] = 0
        
        candidate_votescount[candidate_name] += 1

# Write details to the terminal and text file. 
with open(output_path, "w") as txt: 
   
    # Print the total votes count to the terminal. 
    election_results = (
        f"\nElection Results\n\n"
        f"------------------------------------\n\n"
        f"Total Votes: {votes_count:,}\n\n"
        f"------------------------------------\n\n")
    
    print(election_results, end="")
   
    #Save the final vote count to the text file. 
    txt.write(election_results)


    # Calculate percentage of votes each candidate won and identify winner:

    for candidate in candidate_votescount:
        votescount = candidate_votescount[candidate]
        votes_percentage = float(votescount) / float(votes_count) * 100
        candidate_outcome = (f"{candidate}: {votes_percentage:.3f}% ({votescount:,})\n\n")
        
        # Write details to the terminal and into the output file:
        print(candidate_outcome)
        txt.write(candidate_outcome)


        if (votescount > winner_votecount) and (votes_percentage > votes_won_percentage):
            winner_votecount = votescount
            votes_won_percentage = votes_percentage
            winner_name = candidate

    # Create winner information summary:
    winner_summary = (
        f"------------------------------------\n\n"
        f"Winner: {winner_name}\n"
        f"Winning Percentage: {votes_won_percentage:.3f}%\n\n"
        f"------------------------------------\n")
    print(winner_summary)
    txt.write(winner_summary)


    
