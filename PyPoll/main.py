import os 
import csv



election_csv = os.path.join("/Users/kscomputer/Desktop/DataRepository/Python-Challenge/PyPoll/Resources/election_data.csv" )

#open and read csv
with open(election_csv) as csv_file:
    csv_reader= csv.reader(csv_file, delimiter=',')

    csv_header = next(csv_file)
    print(csv_header)

    voter = []
    candidate = []

    for row in csv_reader:
        voter.append(row[0])
        candidate.append(row[2])

    total_voter = (len(voter))
    print(total_voter)

    total_khan = candidate.count("Khan")
    print(total_khan)