import csv
import os

csv_file = os.path.join("Resources", "budget_data.csv")

#count the months, track changes, and dates
total_months = 0
total = 0
changes = []
dates = []

#open CSV file
with open(csv_file, 'r') as file:
    reader = csv.DictReader(file)

    #identify rows
    for row in reader:
        date = row["Date"]
        profit_loss = int(row["Profit/Losses"])

        total_months += 1
        total += profit_loss
        changes.append(profit_loss)
        dates.append(date)

#calculate average, greatest increase and decrease
change_total = sum(changes[i] - changes[i-1] for i in range(1, len(changes)))
average = change_total / (total_months - 1)
greatest_increase = max(changes)
greatest_decrease = min(changes)
greatest_increase_date = dates[changes.index(greatest_increase)]
greatest_decrease_date = dates[changes.index(greatest_decrease)]

#output definition
output = [
    "Financial Analysis",
    "-----------------------",
    f"Total Months: {total_months}",
    f"Total: ${total}",
    f"Average Change: ${average:.2f}",
    f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})",
    f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})",
]

#print
print("\n".join(output))

#export
file_to_output = os.path.join("resources", "analysis", "Financial_Analysis.txt")
with open(file_to_output, "w") as txt_file:
    txt_file.write("\n".join(output))