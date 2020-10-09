import os 
import csv

budget_csv = os.path.join("/Users/kscomputer/Desktop/DataRepository/Python-Challenge/PyBank/Resources/budget_data.csv")

#open and read csv
with open(budget_csv) as csv_file:
    csv_reader= csv.reader(csv_file, delimiter=',')

    csv_header = next(csv_file)
    print(csv_header)

    month = []
    total_revenue = []
    net_change = []


    ac = 0
    greatest_increase = 0
    
    

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

    def average_change(startpt , currentpt):
        startpt = revenue[0]
        for i in revenue:
            print(i)
            net_change.append((float(revenue[i] -startpt)))
            startpt = revenue[i - 1]

    average = average_change

    

   

    



    



    



