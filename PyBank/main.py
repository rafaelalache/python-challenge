# Modules
import os
import csv

# Set path for file
csvpath = os.path.join("resources", "budget_data.csv")

months = []
pl_changes = []

total_months = 0
net_profit = 0
previous_month = 0
current_month = 0
pl_change = 0


# Open the CSV
with open(csvpath, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    #first_row = next(csvreader)
    print(f"Header: {csv_header}")
    #previous_value = first_row



    # Loop through looking for the video
    for row in csvreader:
        total_months += 1
        net_profit += int(row[1])

        if total_months == 1:
            previous_month = current_month

        else:
            pl_change = current_month - previous_month

            months.append(row[0])

            pl_changes.append(pl_change)

            previous_month = current_month

     #sum and average of the changes in "Profit/Losses" over the entire period
    sum_profit_loss = sum(pl_changes)
    average_profit_loss = round(sum_profit_loss/(total_months - 1), 2)




print(total_months)
print(net_profit)
print(pl_changes)
print(average_profit_loss)
print(sum_profit_loss)

# will resubmit later


# keep track of difference in a list
# look for homework with an empty list and adding as you loop
# conditionals
# print outputs 




    