#import os and csv modules
import os
import csv

#create arrays
votes = []
candidates = []


#find election data csv
electiondata_csv = os.path.join("Resources","election_data.csv")

#open and read election data csv
with open(electiondata_csv,'r',newline='') as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=",")

    #identify header
    csv_header = next(csv_file)

    #set variables
    num_votes = 0
    khanvote = 0
    correyvote = 0
    livote = 0
    otooleyvote = 0
    khanpercent = 0.00
    correypercent = 0.00
    lipercent = 0.00
    otooleypercent = 0.00

    #for loop to count number of votes, candidates, candidates votes, candidates %, and calculcate winner
    for row in csv_reader:
        votes.append(row[0])

        #calculate total number of votes for each candidate
        if (row[2] =="Khan"):
            khanvote = khanvote + 1
        elif (row[2] =="Correy"):
            correyvote = correyvote + 1
        elif (row[2] == "Li"):
            livote = livote + 1
        elif(row[2] == "O'Tooley"):
            otooleyvote = otooleyvote + 1

        #calculate total votes
        total_votes = int(len(votes))

        #calculcate percent
        khanpercent = round(khanvote/total_votes*100)
        correypercent = round(correyvote/total_votes*100)
        lipercent = round(livote/total_votes*100)
        otooleypercent = round(otooleyvote/total_votes*100)

        #calculate winner
        find_winner = max(khanvote,correyvote,livote,otooleyvote)
        if (find_winner == khanvote):
            winner = "Khan"
        elif (find_winner == correyvote):
            winner = "Correy"
        elif (find_winner == livote):
            winner = "Li"
        elif (find_winner == otooleyvote):
            winner = "Otooley"

#

#print summary
print("Election Results")
print("------------------")
print(f"Total Votes:{total_votes}")
print("------------------")
print(f"Khan:{str(khanpercent)}% ({str(khanvote)})")
print(f"Correy: {str(correypercent)}% ({str(correyvote)})")
print(f"Li: {str(lipercent)}% ({str(livote)})")
print(f"Otooley: {str(otooleypercent)}% ({str(otooleyvote)})")
print("------------------")
print(f"Winner: {winner}")