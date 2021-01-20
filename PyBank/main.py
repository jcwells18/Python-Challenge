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
    #set first row
    first_row = next(csv_reader)
    #set previous row
    prev_row = int((first_row[1]))


    #set months and total profit/loss to zero and the change
    num_months = 0
    total_profit_loss = 0
    profit_loss_dif = 0
    #hold the profit loss change
    profit_difs = []
    max_dif = [0,num_months]
    min_dif = [0,num_months]


    #for loop to for count of months and total profit/loss
    for row in csv_reader:
        date.append(row[0])
        profit_loss.append(int(row[1]))
        #calculate totol month count
        num_months +=1
        #calculate total profit/loss
        total_profit_loss = sum(profit_loss)
        #calculate changes between each row
        current_row = int(row[1])
        profit_dif = (current_row-prev_row)
        profit_difs.append(profit_dif)
        prev_row = int(row[1])
        profit_loss_dif +=profit_dif

        #calculate max increase
        if profit_dif > max_dif[1]:
            max_dif[0] = str(row[0])
            max_dif[1] = profit_dif
        
        #calculate max decrease
        if profit_dif < min_dif[1]:
            min_dif[0] = str(row[0])
            min_dif[1] = profit_dif

        #calculate average change
        average_change = round((profit_loss_dif)/(num_months))

#output to txt
output_file = os.path.join('Analysis','financialanalysis.txt')
with open(output_file,"w",newline="") as datafile:
    write = csv.writer(datafile)
    write.writerows([
                        ["Financial Analysis"],
                        ["------------------"],
                        ["Total Months:"+ str(num_months)],
                        ["Total:"+ str(total_profit_loss)],
                        ["Average Change:"+str(average_change)],
                        ["Greatest increase in profits: "+str(max_dif[0])+" ($"+str(max_dif[1])+")"],
                        ["Greatest decrease in profits: "+str(min_dif[0])+" ($"+str(min_dif[1])+")"]
    ])


#print summary
print("Financial Analysis")
print("------------------")
print("Total Months:"+ str(num_months))
print("Total:"+"$"+str(total_profit_loss))
print("Average Change: "+"$"+str(average_change))
print("Greatest increase in profits: "+str(max_dif[0])+" ($"+str(max_dif[1])+")")
print("Greatest decrease in profits: "+str(min_dif[0])+" ($"+str(min_dif[1])+")")


