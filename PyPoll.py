# The date we need to retrive.
#Add dependencies
from audioop import add
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
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Open the election results and read the file.
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
      # If the candidate does not match any existing candidate, add the 
      # the candidate list.
      if candidate_name not in candidate_options:
         # Add the candidate name tp the candidate list.
            candidate_options.append(candidate_name)  
      #Begin tracking that candidate's vote count.   
            candidate_votes[candidate_name] = 0
      # Add a vote to that candidate's count.
      candidate_votes[candidate_name] += 1
#Save the results to the text file.
with open(file_to_save, "w") as txt_file:
  #After opening the file print the final vote count to the terminal.
   election_results = (
      f"\nElection Results\n"
      f"-------------------------\n"
      f"Total Votes: {total_votes:,}\n"
      f"-------------------------\n")
   
   print(election_results, end="")
   # After printing the final vote count to the terminal save the final vote count to the text file.
   txt_file.write(election_results)

   for candidate_name in candidate_votes:
      #retrive vote count of a candidate.
      votes = candidate_votes[candidate_name]
      #calculate the percentage of votes.
      vote_porcentage = float(votes) / float(total_votes) * 100

      candidate_results = (
           f"{candidate_name}: {vote_porcentage:.1f}% ({votes:,})\n")
      # Print each candidate's voter count and percentage to the terminal.     
      print(candidate_results)
       #  Save the candidate results to our text file.
      txt_file.write(candidate_results)
      # Determine if the votes are greater than the winning count.
      if (votes> winning_count) and (vote_porcentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_porcentage
   # Print the winning candidate's results to the terminal.

   winning_candidate_summary = (
      f"-------------------------\n"
      f"Winner: {winning_candidate}\n"
      f"Winning Vote Count: {winning_count:,}\n"
      f"Winning Percentage: {winning_percentage:.1f}%\n"
      f"-------------------------\n")
   print(winning_candidate_summary)    
     # Save the final vote count to the text file.
   txt_file.write(winning_candidate_summary)

