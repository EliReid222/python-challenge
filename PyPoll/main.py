import pandas as pd
import os

#find CSV file
csv_file = os.path.join("Resources", "election_data.csv")

#read CSV and count total votes
election_df = pd.read_csv(csv_file)
total_votes = election_df.shape[0]

#ballot count
votes_per_candidate = election_df.groupby("Candidate").size()

#percentage of votes
percentage_votes = (votes_per_candidate / total_votes) * 100

#winner winner
winner = votes_per_candidate.idxmax()

#ottput define
output = [
    "Election Results",
    "-------------------------",
    f"Total Votes: {total_votes}",
    "-------------------------",
]

#append
for candidate, votes in votes_per_candidate.items():
    output.append(f"{candidate}: {percentage_votes[candidate]:.3f}% ({votes})")

output.extend([
    "-------------------------",
    f"Winner: {winner}",
    "-------------------------",
])

#print the output
for line in output:
    print(line)

#export
file_to_output = os.path.join("resources", "analysis", "election_results.txt")
with open(file_to_output, "w") as txt_file:
    txt_file.write("\n".join(output))
