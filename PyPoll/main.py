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
    total_voter = int

    for row in csv_reader:
        voter.append(row[0])
        candidate.append(row[2])

    total_voter = (len(voter))
    print(total_voter)

    total_khan = candidate.count("Khan")
    print(total_khan)

    total_correy = candidate.count("Correy")
    print(total_correy)

    total_li = candidate.count("Li")
    print(total_li)

    total_otooley = candidate.count("O'Tooley")
    print(total_otooley)

    percent_khan = (total_khan/total_voter)*100
    print(percent_khan)

    percent_correy = (total_correy/total_voter)*100
    print(percent_correy)

    percent_li = (total_li/total_voter)*100
    print(percent_li)
    

    percent_otooley = (total_otooley/total_voter)*100
    print(percent_otooley)

    print("----------------------------")
    print("Election Results")
    print("----------------------------")
    print(f'Total Votes: ', total_voter )
    print("----------------------------")
    print(f'Khan: ' + percent_khan  + total_khan)




