import os 
import csv

budget_csv = os.path.join("/Users/kscomputer/Desktop/DataRepository/Python-Challenge/PyBank/Resources/budget_data.csv")

#open and read csv
with open(budget_csv) as csv_file:
    csv_reader= csv.reader(csv_file, delimiter=',')

    csv_header = next(csv_file)
    print(csv_header)

#state variables and variables that need to be set to 0. 
months = []
profit_loss_change = []

total_profit_loses = 0
total_months= 0

#establish for loop




#calculate greatest increase
total_months = len(months)

#calculate greatest lose

#calculate average


#print out results
print(f'Financial Analysis')
print('-----------------------')
print('Total Months:' {total_months})
print(f'Total Revenue $', {total_profit_loses})
print(f'Average Revenue $', {average})
print(f'Greatest Increase in Profits'{},{})
print(f'Greatest Decrease in Profits' {},{})