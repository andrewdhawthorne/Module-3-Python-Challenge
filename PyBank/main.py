import pandas
import os
import csv

# declaration and assignation of variables 
dates = []
monthly_total = []
total_months = 0
net_total = 0
greatest_increase = 0
current_month = 0
next_month = 0
greatest_decrease = 0
overall_change = 0

csvpath = os.path.join('Resources', 'budget_data.csv')
print(csvpath)
# open file and split columns 
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)

    print(f"CSV Header: {csv_header}")

    for row in csvreader:
       dates.append(row[0])
       monthly_total.append(row[1])

# find total months 
for i in dates:
    total_months += 1

# find total profits/losses
for i in monthly_total:
    net_total += int(i)

# loop through profits to find greatest increase
for i in monthly_total:
    current_month = int(i)
    next_month = int(next(i))
    monthly_change = next_month - current_month
    overall_change += monthly_change 

#df[difference] = df[next_month] - df[current_month]
    

#average_change = overall_change / total_months    

#print(average_change)

# display results 
#print("Financial Analysis\n")
#print("-------------------\n")
#print(f"Total Months: {total_months}\n")
#print(f"Total: ${net_total}\n")
