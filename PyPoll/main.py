#import os and csv modules
import os
import csv

#create arrays
votes = []
candidates = []
candidate = []

#find election data csv
electiondata_csv = os.path.join("Resources","election_data.csv")

#open and read election data csv
with open(electiondata_csv,'r',newline='') as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=",")

    #identify header
    csv_header = next(csv_file)

    #set number of votes to zero
    num_votes = 0

    #for loop to count number of votes
    for row in csv_reader:
        votes.append(row[0])
        candidate.append(row[2])


#calculate total votes
total_votes = int(len(votes))



#print stats
print("Election Results")
print("-----------------")
print(f"Total Votes:{total_votes}")
print("------------------")
