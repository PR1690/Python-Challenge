import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")
Total_Months=[]
Total_net=[]
profit_difference = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header=next(csvreader)
    for rows in csvreader:
        Total_Months.append(rows[0])
        Total_net.append(int(rows[1]))
    
    for j in range(len(Total_net)-1):
        profit_difference.append(Total_net[j+1]-Total_net[j])

max_profit_change = max(profit_difference)
min_profit_change = min(profit_difference)

max_increase_profit_month = profit_difference.index(max(profit_difference))+1
min_decrease_profit_month = profit_difference.index(min(profit_difference))+1

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(Total_Months)}")
print(f"Total: ${sum(Total_net)}")
print(f"Average Change: ${round(sum(profit_difference)/len(profit_difference),2)}")
print(f"Greatest Increase in Profits: {Total_Months[max_increase_profit_month]} (${(str(max_profit_change))})")
print(f"Greatest Decrease in Profits: {Total_Months[min_decrease_profit_month]} (${(str(min_profit_change))})")

f = open("final-analysis.txt","w")
f.write("Financial Analysis")
f.write("\n")
f.write("----------------------------")
f.write("\n")
f.write(f"Total Months: {len(Total_Months)}")
f.write("\n")
f.write(f"Total: ${sum(Total_net)}")
f.write("\n")
f.write(f"Average Change: ${round(sum(profit_difference)/len(profit_difference),2)}")
f.write("\n")
f.write(f"Greatest Increase in Profits: {Total_Months[max_increase_profit_month]} (${(str(max_profit_change))})")
f.write("\n")
f.write(f"Greatest Decrease in Profits: {Total_Months[min_decrease_profit_month]} (${(str(min_profit_change))})")

    

