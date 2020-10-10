import os 
import csv

budget_csv = os.path.join("/Users/kscomputer/Desktop/DataRepository/Python-Challenge/PyBank/Resources/budget_data.csv")
financial_output = os.path.join("/Users/kscomputer/Desktop/DataRepository/Python-Challenge/PyBank/Resources/financial_output.txt")


with open(budget_csv) as csv_file:
    csv_reader= csv.reader(csv_file, delimiter=',')

    csv_header = next(csv_file)
    

    month = []
    total_revenue = []
    net_change = []

    greatest_increase = 0
    great_decrease = 0
    total_of_revenue = 0 
     
    for row in csv_reader:
        month.append(row[0])
        total_revenue.append(row[1])
   
    total_month = (len(month))
    
    revenue = [int (i) for i in total_revenue]
    total_of_revenue = (sum(revenue))
    
    startpt = revenue[0]

    for i in revenue:
        net_change.append((float(revenue[revenue.index(i)] - startpt)))     
        startpt = i
    
    p_l_change = (sum(net_change)/85)
   

    greatest_increase = max(net_change)
    greatest_decrease = min(net_change)
    greatest_increase_month = month[net_change.index(greatest_increase)]
    greatest_decrease_month = month[net_change.index(greatest_decrease)]


output = (
"----------------------------\n"
"Financial Analysis\n"
"----------------------------\n"
f"Total Month: {total_month}\n"
f"Total: ${total_of_revenue}\n"
f"Average Change: {p_l_change}\n"
f"Greatest Increase in Profits: {greatest_increase_month} ({greatest_increase})\n"
f"Greatest Decrease in Profits: {greatest_decrease_month} ({greatest_decrease})\n"

)    

with open(financial_output, "w") as txt_file:
    txt_file.write(output)

    

    

    
    

    

    

   

    



    



    



