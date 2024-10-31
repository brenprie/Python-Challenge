# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("Analysis", "election_analysis.txt")  # Output file path

# Initialize variables
numVotes = 0  # Total number of votes cast
percentVotes = 0 # Percentage of votes (for a given candidate)

# Define lists and dictionaries
candidates = []  # list to hold the different candidates; candidates are in index 2 from data table 
candidateVoteCounts = {} # dictionary to hold vote counts for each candidate
candidateVotePercentages = {} # dictionary to hold vote percentages for each candidate

# Open the CSV file and process it
with open(file_to_load, "r", encoding="utf-8") as election_data:
    csvreader = csv.reader(election_data)

    # Skip the header row
    header = next(csvreader)

    # Loop through each row of the dataset and process it
    for row in csvreader:

        # Add to the running total number of votes
        numVotes += 1

        # Get the candidate's name from the row
        candidate = row[2] 

        # If the candidate is not already in the candidate list, add them to the list
        if candidate not in candidates:
            candidates.append(candidate)
            # add key-value pair for candidate and start its vote count
            candidateVoteCounts[candidate] = 1 # once candidate appears, add to their vote count 
        else:
            # if the candidate is already in the candidate list, then add to its count in the dictionary
            candidateVoteCounts[candidate] += 1

# Generate output summary
    
    # Add to "output" title and total number of votes
    output = (
        f"\nElection Results\n"
        f"\n--------------------------------------\n"
        f"\nTotal Votes: {numVotes}\n"
        f"\n--------------------------------------\n"
    )

    # Loop through candidates to determine vote percentages, and for each candidate add percentage of votes and vote count to "output"  
    for candidate in candidateVoteCounts:
        # Calculate percentage of votes for each candidate, add to "output"
        percentVotes = (candidateVoteCounts[candidate] / numVotes) * 100
        output += f"\n{candidate}: {percentVotes:.3f}% ({candidateVoteCounts[candidate]})\n"
        # Update the winning candidate if this one has more votes

    # Determine winner (I used max function on dictionary), and add winner to "output"
    winner = max(candidateVoteCounts, key=candidateVoteCounts.get)
    output += (
        f"\n--------------------------------------\n"
        f"\nWinner: {winner}\n"
        f"\n--------------------------------------\n"
        )

# Print output to terminal
print(output)

# Export output to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)




