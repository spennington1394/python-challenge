import os 
import csv

budget_csv = os.path.join("/Users/kscomputer/Desktop/DataRepository/Python-Challenge/PyBank/Resources/budget_data.csv")

#open and read csv
with open(budget_csv) as csv_file:
    csv_reader= csv.reader(csv_file, delimiter=',')

    csv_header = next(csv_file)
    print(csv_header)

#state variables that need to be set to 0. 

#calculate greatest increase

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
    
        