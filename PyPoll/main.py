# Import necessary modules
import csv
import os

# Files to load and output
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("Analysis", "election_analysis.txt")  # Output file path

# Initialize variables
totalVotes = 0  # total number of votes cast across all candidates
voteOutput = "" # variable that holds candidates, their percentage of votes, and their vote counts
winningCount = 0 # variable to hold winning vote count

# Define lists and dictionaries
candidates = []  # list to hold the different candidates; candidates are index 2
candidateVotes = {} # dictionary to hold vote counts for each candidate

# Read and process the CSV file
with open(file_to_load, "r", encoding="utf-8") as electionData:
    # Create csv reader
    csvreader = csv.reader(electionData)

    # skip the header row, so can proceed to dataset
    header = next(csvreader)

    # Loop through each row of the dataset and process it
    for row in csvreader:

        # Add to the running total number of votes
        totalVotes += 1

        # Get the candidate's name from the row
        # this could be skipped, with "row[2]" replacing "candidate" below, but this step increases logical transparency
        candidate = row[2] 

        # If the candidate is not already in the candidate list:
        if candidate not in candidates:
            # add candidate to list of candidates
            candidates.append(candidate)
            # add candidate (key) and vote (value) to dictionary; start candidate's vote count here
            candidateVotes[candidate] = 1  
        # if the candidate is already in the candidate list: 
        else:
            # add to candidate's count in the dictionary
            candidateVotes[candidate] += 1

    # Loop through candidates. For each candidate, determine vote percentage; output vote percentage and vote count to output variable  
    for candidate in candidateVotes:
        # Calculate candidate's percentage of total votes
        PercentVote = (candidateVotes[candidate] / totalVotes) * 100
        # Add candidate's percentage of votes, as well as vote count in parens, to vote output variable
        voteOutput += f"\n{candidate}: {PercentVote:.3f}% ({candidateVotes[candidate]})\n"

        # Compare vote count to winning count to determine winner
        # NOTE: I include the loop method here for education purposes, but I employ a more succint method to find the winner below
        # if candidateVotes[candidate] > winningCount:
            # update winning vote count
        #   winningCount = candidateVotes[candidate]
            # update winning candidate
        #   winner = candidate

    # Determine winner - my preferred method: using max function on dictionary
    winner = max(candidateVotes, key=candidateVotes.get)
    
# Generate output variable to hold outputs; output variable will be a string
# NOTE: the below could be provided in a single string without concatinations, but I prefer the long form in this instance to illustrate the technique
    
    # Add to "output": title
    output = (
        f"\nElection Results\n"
        f"\n--------------------------------------\n"
        )
    # Add to "output": total number of votes
    output += (
        f"\nTotal Votes: {totalVotes}\n" # could use {totalVotes:,} to introduce commas in long numbers
        f"\n--------------------------------------\n"
        )
    # Add to "output": vote output variable
    output += (
         f"{voteOutput}"
         f"\n--------------------------------------\n"
        )
    # Add to "output": winner
    output += (
        f"\nWinner: {winner}\n"
        f"\n--------------------------------------\n"
        )

# Display output to terminal
print(output)

# Export output to text file
with open(file_to_output, "w") as textFile:
    textFile.write(output)




