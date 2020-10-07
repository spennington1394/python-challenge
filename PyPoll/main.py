import os 
import csv

election_csv = os.path.join("..", "Resources", "election_data.csv")

#open and read csv
with open(election_csv) as csv_file:
    csv_reader= csv.reader(csv_file, delimiter=',')

    csv_header = next(csv_file)