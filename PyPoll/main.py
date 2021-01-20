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

    #for loop to count number of votes and find candidate
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



#print stats
print("Election Results")
print("-----------------")
print(f"Total Votes:{total_votes}")
print("------------------")
print(f"Khan:{str(khanpercent)}% {str(khanvote)}")