import os
import csv

csvpath = os.path.join('.','election_data.csv')

with open (csvpath, newline='') as excelfile:
    excelfile = csv.reader(excelfile, delimiter=',')

    next(excelfile)

    totalvotes_lst = []
    candidates_lst =[]
    uniquecandidates_lst =[]
    numvotes_lst = []

    for row in excelfile:
        totalvotes_lst.append(row[0])
        candidates_lst.append(row[2])
        if row[2] not in uniquecandidates_lst:
            uniquecandidates_lst.append(row[2])
    
    print("Election Results")
    print("-------------------------")
    print(f'Total Votes: {len(totalvotes_lst)}')
    print("-------------------------")
    #print(uniquecandidates_lst)
    for i in uniquecandidates_lst:
        print(f'{i} {"{:.3%}".format(candidates_lst.count(i)/len(totalvotes_lst))} ({candidates_lst.count(i)})')
    #another method:
    #for i in range(len(uniquecandidates_lst)):
       #print(candidates_lst.count(uniquecandidates_lst[i]))
    
    for i in uniquecandidates_lst:
        numvotes_lst.append(candidates_lst.count(i))
    
    winner_index = numvotes_lst.index(max(numvotes_lst))
    
    print("-------------------------")
    print(f'Winner: {uniquecandidates_lst[winner_index]}')
    print("-------------------------")