import os
import csv

# declaration and assignation of variables 
dates = []
monthly_total = []
total_months = 0
# net_total = 0
# greatest_increase = 0
# current_month = 0
# next_month = 0
# greatest_decrease = 0
# overall_change = 0

csvpath = os.path.join('Resources', 'budget_data.csv')
print(csvpath)
# open file and split columns 
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)
    changes_list = []
    first_row = next(csvreader)
    # print(first_row) => ['date', '1']
    # prev_profit = int(first_row[1])
    print(f"CSV Header: {csv_header}")
    # total = int(first_row[1])...



    for row in csvreader:
       # calculate the change using the prev_profit
       # append that to your list
       cur_date = row[0]
       cur_profit = int(row[1])
        #  row = ['Jan-10','1088983']
       dates.append(row[0])
       monthly_total.append(int(row[1]))
    # chonges_list now equals [1, -2, 3]
    # avg_change = sum(changes_list) / len(changes_list)
# find total months 
for i in dates:
    total_months += 1

# loop through profits to find greatest increase
for i in monthly_total:
    current_month = int(i)
    next_month = int(next(i))
    monthly_change = next_month - current_month
    overall_change += monthly_change   

#average_change = overall_change / total_months    

#print(average_change)


# find total profits/losses
# for i in monthly_total:
    # net_total += int(i)



# display results 
#print("Financial Analysis\n")
#print("-------------------\n")
print(f"Total Months: {total_months}\n")
#print(f"Total: ${net_total}\n")
