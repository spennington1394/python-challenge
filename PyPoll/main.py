import os 
import csv



election_csv = os.path.join("/Users/kscomputer/Desktop/DataRepository/Python-Challenge/PyPoll/Resources/election_data.csv" )
poll_output = os.path.join("/Users/kscomputer/Desktop/DataRepository/Python-Challenge/PyPoll/Resources/poll_to_out.txt")


with open(election_csv) as csv_file:
    csv_reader= csv.reader(csv_file, delimiter=',')

    csv_header = next(csv_file)
    
    voter = []
    candidate = []
    total_voter = int

    for row in csv_reader:
        voter.append(row[0])
        candidate.append(row[2])

    total_voter = (len(voter))

    total_khan = candidate.count("Khan")

    total_correy = candidate.count("Correy")

    total_li = candidate.count("Li")
    
    total_otooley = candidate.count("O'Tooley")

    percent_khan = round((total_khan/total_voter)*100)
    
    percent_correy = round((total_correy/total_voter)*100)
    
    percent_li = round((total_li/total_voter)*100)
    
    percent_otooley = round((total_otooley/total_voter)*100)


output = (

    "----------------------------\n"
    "Election Results\n"
    "----------------------------\n"
    f"Total Votes: {total_voter}\n"
    "----------------------------\n"
    f"Khan: {percent_khan} % {total_khan}\n"
    f"Correy: {percent_correy} %  {total_correy}\n"
    f"Li: {percent_li} % {total_correy}\n"
    f"O'Tooley: {percent_otooley} % {total_otooley}\n"
    "----------------------------\n"
        "Winner: Khan\n"
    "----------------------------"
)

with open(poll_output, "w") as txt_file:
    txt_file.write(output)






