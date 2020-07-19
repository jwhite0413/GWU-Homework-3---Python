#importfile
import os
import csv
pybank_csv = os.path.join ("..","Resources","budget_data.csv")

#create lists
months =[]
profits= []

number_of_months = 0
net_profit_loss = 0
previous_month_profit = 0
current_month_profit = 0
profit_changes = 0

#open file and show header rows
with open(pybank_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    csv_header = next(csvfile)
    print(f"Header:{csv_header}")
#Total number of months
    for row in csvreader:
        number_of_months +=1
        profit_changes += (int(row[1]))

#Print Anaylsis
print("Financial Anaylsis")
print("----------")
print (f"Total Months: {number_of_months}")
print (f"Total Profits: {profit_changes}")


 