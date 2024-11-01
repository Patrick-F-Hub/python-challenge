# Import modules
import csv
import os

# Files to load and output
inputFile = os.path.join("Resources", "election_data.csv")  # Input file path
outputFile = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
totalVotes = 0  # Track the total number of votes cast
candidates = [] # list that holds the candidates in the election
candidateVotes = {} # dictionary that will hold the votes each candidate receives
winningCount = 0 # variable hold the winning count 
winningCandidate = "" # variable to hold winning candidate

# Open the CSV file and process it
with open(inputFile) as electionData:
    csvreader = csv.reader(electionData)

    # Read the header row
    header = next(csvreader)

    # rows will be lists
        # index 0 is the ballot id
        # index 1 is the county
        # index 2 is the candidate choice

    # Loop through each row of the dataset and process it
    for row in csvreader:
        # add on to the total votes
        totalVotes += 1

        # check to see if candidate is in the list of candidates
        if row[2] not in candidates:
            # add candidates if not in the list
            candidates.append(row[2])

            # add the value to the dictionary as well
            # {"key": value }
            # start the count at 1 for the votes
            candidateVotes[row[2]] = 1

        else:
            # the candidate is in the list of candidates
            # add a vote to that candidate's count
            candidateVotes[row[2]] += 1

    voteOutput = ""

    for candidate in candidateVotes:
        # get the vote count and the percentage of votes
        votes = candidateVotes.get(candidate)
        votePct = (float(votes) / float(totalVotes)) * 100.00    
        voteOutput += f"\t{candidate}: {votePct:.2f}% ({votes:,}) \n"
        
        # compare the votes to the winning count
        if votes > winningCount:
            # update the votes to be the new winning count
            winningCount = votes
            # update the winning candidate
            winningCandidate = candidate

winningCandidateOutput = f"\t\tWinner: {winningCandidate}\n-----------------------"

    # Generate and print the winning candidate summary
output = (
    f"Election Results \n"
    f"----------------------- \n"
    f"Total Votes: {totalVotes:,} \n"
    f"----------------------- \n"
    f"{voteOutput} \n"
    f"----------------------- \n"
    f"{winningCandidateOutput}"
)

print(output)
    # Save the winning candidate summary to the text file
with open(outputFile, "w") as textfile:
    textfile.write(output)