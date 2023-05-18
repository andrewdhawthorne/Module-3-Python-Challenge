import os
import csv


CSV_PATH = os.path.join('Resources', 'election_data.csv')
CANDIDATE_IDX = 2

total_votes = 0


os.chdir(os.path.dirname(os.path.realpath(__file__)))
with open(CSV_PATH) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_reader)
    #print(f"CSV Header: {csv_header}")
    for row in csv_reader: 
        # print(type(row), row) 
        # Calculate total votes 
        total_votes += 1
        # Calcuatle total votes per candidate 

    # Calculate the percentage per candidate 

    # Identify which candidate had the most votes 

print(total_votes)