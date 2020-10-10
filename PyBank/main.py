import os 
import csv

budget_csv = os.path.join("/Users/kscomputer/Desktop/DataRepository/Python-Challenge/PyBank/Resources/budget_data.csv")
financial_output = os.path.join("/Users/kscomputer/Desktop/DataRepository/Python-Challenge/PyBank/Resources/financial_output.txt")

#open and read csv
with open(budget_csv) as csv_file:
    csv_reader= csv.reader(csv_file, delimiter=',')

    csv_header = next(csv_file)
    print(csv_header)

    month = []
    total_revenue = []
    net_change = []

    greatest_increase = 0
    great_decrease = 0
     
    
    

    #in for loop append the two lists created above
    for row in csv_reader:
        month.append(row[0])
        total_revenue.append(row[1])
    #find the length of month to give us the total_month
    total_month = (len(month))
    print(total_month)

    #take string list and change to integers using a comprehensive list 
    revenue = [int (i) for i in total_revenue]
    print(sum(revenue))

    #function to help calculate average change

    startpt = revenue[0]

    for i in revenue:
        net_change.append((float(revenue[revenue.index(i)] - startpt)))     
        startpt = i
    
    #calculating average change over the complete csv file
    p_l_change = (sum(net_change)/85)
    print(p_l_change)

    #assigning value to greatest increase/decrease and corresponding month & year
    greatest_increase = max(net_change)
    greatest_decrease = min(net_change)
    greatest_increase_month = month[net_change.index(greatest_increase)]
    print(greatest_increase_month)
    greatest_decrease_month = month[net_change.index(greatest_decrease)]
    print(greatest_decrease_month)

output = (
"----------------------------\n"
"Financial Analysis\n"
"----------------------------\n"
f"Total Month: {total_month}\n"
f"Average Change: {p_l_change}\n"
f"Greatest Increase in Profits: {greatest_increase_month} {greatest_increase}\n"
f"Greatest Decrease in Profits: {greatest_decrease_month} {greatest_decrease}\n"

)    

with open(financial_output, "w") as txt_file:
    txt_file.write(output)

    

    

    
    

    

    

   

    



    



    



