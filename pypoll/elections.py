import csv
import os

file_path = os.path.join("..", "resources", "election_data.csv")
# Create a dictionary to store candidate votes
candidate_votes = {}

# Open the CSV file
with open(file_path, "r") as csv_file:
    # Read the CSV file row by row
    csv_reader = csv.reader(csv_file)
    next(csv_reader)  # Skip the header row

    total_votes = 0  # total vote count

    #loop over the rows in the CSV file
    for row in csv_reader:
        # Get the candidate name
        candidate_name = row[2]

        # Update the candidate's vote count
        if candidate_name in candidate_votes:
            candidate_votes[candidate_name] += 1
        else:
            candidate_votes[candidate_name] = 1

        total_votes += 1  # Increment total vote count

# Initialize variables for winner calculation
winner = ""
winner_votes = 0

# Print Election Results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

# Calculate and print the percentage of votes for each candidate
for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")
    
    # Check if this candidate has more votes than the current winner
    if votes > winner_votes:
        winner = candidate
        winner_votes = votes

print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

