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
        totalvotes_lst.append(row[0]) #The total number of votes cast
        candidates_lst.append(row[2])
        if row[2] not in uniquecandidates_lst:
            uniquecandidates_lst.append(row[2])
        
    #Print the analysis to the terminal
    print("\nElection Results")
    print("-------------------------")
    print(f'Total Votes: {len(totalvotes_lst)}')
    print("-------------------------")
    #print(uniquecandidates_lst) #A complete list of candidates who received votes
    for i in uniquecandidates_lst:
        print(f'{i} {"{:.3%}".format(candidates_lst.count(i)/len(totalvotes_lst))} ({candidates_lst.count(i)})') #The percentage of votes each candidate won #The total number of votes each candidate won
    #another method:
    #for i in range(len(uniquecandidates_lst)):
       #print(candidates_lst.count(uniquecandidates_lst[i]))
    
    for i in uniquecandidates_lst:
        numvotes_lst.append(candidates_lst.count(i))
    
    winner_index = numvotes_lst.index(max(numvotes_lst))
    
    print("-------------------------")
    print(f'Winner: {uniquecandidates_lst[winner_index]}')
    print("-------------------------")

#Export a text file with the results
with open("Output_PyPoll.txt", "w") as text_file:
    print("Election Results", file = text_file)
    print("-------------------------", file = text_file)
    print(f'Total Votes: {len(totalvotes_lst)}', file = text_file)
    print("-------------------------", file = text_file)
    for i in uniquecandidates_lst:
        print(f'{i} {"{:.3%}".format(candidates_lst.count(i)/len(totalvotes_lst))} ({candidates_lst.count(i)})', file = text_file)
   
    for i in uniquecandidates_lst:
        numvotes_lst.append(candidates_lst.count(i))
    
    winner_index = numvotes_lst.index(max(numvotes_lst))
    
    print("-------------------------", file = text_file)
    print(f'Winner: {uniquecandidates_lst[winner_index]}', file = text_file)
    print("-------------------------", file = text_file)