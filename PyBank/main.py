import os
import csv

csvpath = os.path.join('.','budget_data.csv')

with open (csvpath, newline='') as excelfile:
    excelfile = csv.reader(excelfile, delimiter=',')

    next(excelfile)
        
    uniquemonths = []
    total=0
    date_lst = []
    profloss_lst = []
    change_lst = []

    #The total number of months included in the dataset
    for row in excelfile:
        if row[0] not in uniquemonths:
            uniquemonths.append(row[0])
        
        #The net total amount of "Profit/Losses" over the entire period
        total = total+int(row[1])

        date_lst.append(row[0])
        profloss_lst.append(row[1])   

    #The average of the changes in "Profit/Losses" over the entire period

    for i in range(len(profloss_lst)-1):
        change_lst.append(int(profloss_lst[i+1]) - int(profloss_lst[i]))
    
    # The greatest increase in profits (date and amount) over the entire period
    # The greatest decrease in losses (date and amount) over the entire period
    
    max_index = change_lst.index(max(change_lst))
    min_index = change_lst.index(min(change_lst))

    #Final output - Print the analysis to the terminal
    print("\nFinancial Analysis")
    print("-------------------------")
    print(f'Total Months: {len(uniquemonths)}')
    print(f'Total: ${total}')
    print(f'Average Change: $ {round(sum(change_lst)/len(change_lst), 2)}')
    print(f'Greatest Increase in Profits: {date_lst[max_index+1]} $ {change_lst[max_index]}')
    print(f'Greatest Decrease in Profits: {date_lst[min_index+1]} $ {change_lst[min_index]}')

#print the analysis to the terminal
with open("Output_PyBank.txt", "w") as text_file:
    print("Financial Analysis", file = text_file)
    print("-------------------------", file = text_file)
    print(f'Total Months: {len(uniquemonths)}', file = text_file)
    print(f'Total: ${total}', file = text_file)
    print(f'Average Change: $ {round(sum(change_lst)/len(change_lst), 2)}', file = text_file)
    print(f'Greatest Increase in Profits: {date_lst[max_index+1]} $ {change_lst[max_index]}', file = text_file)
    print(f'Greatest Decrease in Profits: {date_lst[min_index+1]} $ {change_lst[min_index]}', file = text_file)