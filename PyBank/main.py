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


    #set months and total profit/loss to zero
    num_months = 0
    total_profit_loss = 0

    #for loop to for count of months and total profit/loss
    for row in csv_reader:
        date.append(row[0])
        profit_loss.append(int(row[1]))
        num_months +=1
        total_profit_loss = sum(profit_loss)
        

#calculate avg change
average_change = (total_profit_loss)/(num_months)



#print stats
print("Financial Analysis")
print("------------------")
print("Total Months:"+ str(num_months))
print("Total:"+ str(total_profit_loss))
print("Average Change:"+str(average_change))

