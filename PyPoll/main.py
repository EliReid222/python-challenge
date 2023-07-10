import csv
import os

#find CSV file
csv_file = os.path.join("Resources", "election_data.csv")

#count total votes
total_votes = 0
votes_per_candidate = {}

#open CSV file
with open(csv_file, 'r') as file:
    reader = csv.reader(file)
    header = next(reader)  

    #identify the rows
    for row in reader:
        candidate = row[2] 
        total_votes += 1
        votes_per_candidate[candidate] = votes_per_candidate.get(candidate, 0) + 1

#calculate percentage of votes
percentage_votes = {}
for candidate, votes in votes_per_candidate.items():
    percentage = (votes / total_votes) * 100
    percentage_votes[candidate] = percentage

#winner winner
winner_votes = 0
winner = ""

for candidate, votes in votes_per_candidate.items():
    if votes > winner_votes:
        winner_votes = votes
        winner = candidate


#output definition
output = [
    "Election Results",
    "-------------------------",
    f"Total Votes: {total_votes}",
    "-------------------------",
]

#results
for candidate, votes in votes_per_candidate.items():
    percentage = percentage_votes[candidate]
    output.append(f"{candidate}: {percentage:.3f}% ({votes})")

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