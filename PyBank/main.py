#importfile
import os
import csv
pybank_csv = os.path.join ("..","Resources","budget_data.csv")

#create lists and set variables
months =[]
profits= []
revenue_change_list =[]

greatest_increase = ["",0]
greatest_decrease = ["",99999999]

number_of_months = 0
total_profits = 0
net_profit_loss = 0
previous_revenue = 0
revenue_change = 0
average_change = 0



#open file and show header rows
with open(pybank_csv, 'r',) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    csv_header = next(csvreader)
    print(f"Header:{csv_header}")
#Total number of months and total profits
    for row in csvreader:
        number_of_months +=1
        total_profits += (int(row[1]))
        #Calculate change
        revenue_change = (int(row[1])) - previous_revenue
        previous_revenue = (int(row[1]))
        months += [row[0]]
        #total the greatest increases and greatest decreases
        revenue_change_list.append(revenue_change)

        average_change = round(sum(revenue_change_list)/ number_of_months,2)
        #determine greatest increase using logic statement
        if (revenue_change > greatest_increase[1]):
            greatest_increase[1] = revenue_change
            greatest_increase[0] = row [0]
        if (revenue_change < greatest_decrease[1]):
            greatest_decrease[1] = revenue_change
            greatest_decrease [0] = row [0]  




#Print Anaylsis with variable to store for output

Output = (

f"Financial Anaylsis\n"
f"----------\n"
f"Total Months: {number_of_months}\n"
f"Total Profits: ${total_profits}\n"
f"Average Revenue Change: ${average_change}\n"
f"Greatest Increase: {greatest_increase}\n"
f"Greatest Decrease: {greatest_decrease}\n")

print (Output)

with open ('PyBank.txt','w') as text_file:
    textwriter = text_file.write(Output)
