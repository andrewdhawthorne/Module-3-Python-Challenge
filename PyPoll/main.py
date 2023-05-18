import os
import csv

csv_path = os.path.join('Resources', 'election_data.csv')
candidate_name = row[2] 
candidate_list = []
candidate_vote_count = {}

total_votes = 0


os.chdir(os.path.dirname(os.path.realpath(__file__)))
with open(csv_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_reader)
    #print(f"CSV Header: {csv_header}")
    for row in csv_reader: 
        # print(type(row), row) 
        # Calculate total votes 
        total_votes += 1
        # Calcuatle total votes per candidate 
candidate_vote_count[candidate_name] = candidate_vote_count[candidate_name] + 1
    # Calculate the percentage per candidate 
candidate_vote_count[candidate_name] = 1
    # Identify which candidate had the most votes 
print(candidate_vote_count)
print(total_votes)