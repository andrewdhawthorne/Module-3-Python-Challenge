import os
import csv

# declaration and assignation of variables 
dates = []
monthly_total = []
total_months = 0
net_total = 0
greatest_increase = 0
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
       monthly_total.append(int(row[1]))

       if int(row[1]) > greatest_increase:
           greatest_increase = int(row[1])
    
# find total months 
for i in dates:
    total_months += 1

# find total profits/losses
for i in monthly_total:
    net_total += int(i)

#print(monthly_total)
#print(total_months)

start_total = int(monthly_total[0])
end_total = int(monthly_total[-1])
overall_change = end_total - start_total

#print(overall_change)

average_change = overall_change/(total_months -1)
average_change = round(average_change, 2)

#print(average_change)

monthly_changes_list = []
month_1 = int(monthly_total[0])
month_2 = 0
monthly_change = 0
greatest_increase_date = ""
greatest_decrease_date = ""

for i in monthly_total:
    month_2 = int(i)
    monthly_change = month_2 - month_1
    month_1 = month_2
    monthly_changes_list.append(monthly_change)

greatest_increase = max(monthly_changes_list)
greatest_decrease = min(monthly_changes_list)

for i in range(1, len(monthly_changes_list)): 
    if monthly_changes_list[i] == greatest_increase:
        greatest_increase_date = dates[i]
    elif monthly_changes_list[i] == greatest_decrease:
        greatest_decrease_date = dates[i]


# display results 
print("Financial Analysis\n")
print("-------------------\n")
print(f"Total Months: {total_months}\n")
print(f"Total: ${net_total}\n")
print(f"Average Change: ${average_change}\n")
print(f"Greatest Increase in Profits: {greatest_increase_date} ${max(monthly_changes_list)}\n")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} ${min(monthly_changes_list)}\n")
