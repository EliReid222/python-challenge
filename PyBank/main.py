import pandas as pd
import os

csv_file = os.path.join("Resources", "budget_data.csv")

#read CSV file, count the months, and calculate the total $$
budget_df = pd.read_csv(csv_file)
total_months = budget_df.shape[0]
total = budget_df["Profit/Losses"].sum()

#calculations of max, min, average, greatest increase, and decrease
budget_df["Change"] = budget_df["Profit/Losses"].diff()
average = budget_df["Change"].mean()
greatest_increase = budget_df["Change"].max()
greatest_decrease = budget_df["Change"].min()
greatest_increase_date = budget_df.loc[budget_df["Change"] == greatest_increase, "Date"].item()
greatest_decrease_date = budget_df.loc[budget_df["Change"] == greatest_decrease, "Date"].item()

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