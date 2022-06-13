# The date we need to retrive.
# 3. The percentange of votes each candidate won
# 4. The total number of votes each candidate won
# 5. the winner of the election based on pupular vote.
#Add dependencies
import csv
from email import header
from email.header import Header
from tkinter import N
from wsgiref import headers
dir(csv)
import os
dir(os)

#Assing a variable to save the file to the path.
file_to_load = os.path.join("Resources", "election_results.csv")
#Assing a vaiablr to save the file to the path.
file_to_save = os.path.join("Resources", "election_results.txt")

#initialize a total vote counter
total_votes = 0
# Candidate options and candidate votes
candidate_options = []
# Declare the empty dictionary.
candidate_votes = {}

with open(file_to_load) as election_data:
     # To do: read and analyze the data here.
   file_reader = csv.reader(election_data)
     # Read and print the header row.
   headers = next(file_reader)
      #print each row in the CSV file.
   for row in file_reader:
         #Add to the total vote count.
      total_votes += 1
      #print the candidate name from each row.
      candidate_name = row[2]
      # Winning Candidate and Winning Count Tracker
      winning_candidate = ""
      wining_count = 0
      wining_percentage = 0
# If the candidate does not match any existing candidate....
      if candidate_name not in candidate_options:
         # Add the candidate name tp the candidate list.
            candidate_options.append(candidate_name)  
      #Begin tracking that candidate's vote count.   
            candidate_votes[candidate_name] = 0
      # Add a vote to that candidate's count.
      candidate_votes[candidate_name] += 1
# Determine the percentage of votes for each candidate by looping through the counts.
   #Interate through the candidate list.
for candidate_name in candidate_votes:
      #retrive vote count of a candidate.
      votes = candidate_votes[candidate_name]
      #calculate the percentage of votes.
      vote_porcentage = float(votes) / float(total_votes) * 100

       #  To do: print out each candidate's name, vote count, and percentage of
    # votes to the terminal.

# Determine if the votes are greater than the winning count.
      if (votes> wining_count) and (vote_porcentage > wining_percentage):
   # If true then set winning_count = votes and winnning_percent =
   # vote percentage
            wining_count = votes
            wining_percentage = vote_porcentage
            winning_candidate = candidate_name

   # And, set the winning_candidate equal to the candidate's name.

      print(f"{candidate_name}: {vote_porcentage:.1f}% ({votes:,})\n")

wining_candidate_summary = (
      f"-------------------------\n"
      f"Winner: {winning_candidate}\n"
      f"Winning Vote Count: {wining_count:,}\n"
      f"Winning Percentage: {wining_percentage:.1f}%\n"
      f"-------------------------\n")
print(wining_candidate_summary)




