#import os and csv modules
import os
import csv

#create lists
date = []
profit_loss = []

#find budget data from resouces folder
budgetdata_csv = os.path.join("Resources","budget_data.csv")

#open and read budget data csv
with open(budgetdata_csv,'r',newline='') as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=",")

    #read header rows first
    csv_header = next(csv_file)

    #count the number of months
    num_months = 0
    for row in csv_file:
        date.append(row[0])
        num_months +=1

#greatest increase and decrease
    total_profit_loss = 0

#total profit loss
    for n in profit_loss:
        total_profit_loss += int(n)
    


#print stats
print("Financial Analysis")
print("------------------")
print("Total Months:"+ str(num_months))
print("Total Revenue:"+ str(total_profit_loss))
