#importfile
import os
import csv
pypoll_csv = os.path.join ("..","Resources","election_data.csv")

#setvariables and create lists
votes = 0
candidatelist = []
vote_count = []
csv_reader = ["1", "2"]
percent = []



#openfile
with open(pypoll_csv,'r') as csvfile:
    csv_reader = csv.reader(csvfile,delimiter=",")
    next(csv_reader)
    # print(f"Header:{csv_header}")

#total number of votes
    for row in csv_reader:
        votes = votes + 1
        
        candidate = row[2]
    # for candidate in candidatelist:
        if candidate  in candidatelist: 
            candidate_index = candidatelist.index(candidate)
            vote_count [candidate_index] = vote_count[candidate_index] +1
        else:
            candidatelist.append(candidate)
            vote_count.append (1)

most_votes = vote_count[0]
most_votes_index = 0
for count in range (len(candidatelist)):
    vote_percent = vote_count[count]/votes*100
    percent.append(vote_percent)
    candidate_data = (f"{candidatelist[count]}:{percent[count]}% ({vote_count[count]}")
    print (candidate_data)
    if vote_count[count]> most_votes:
        print(most_votes)
        most_votes_index = count 

winner = candidatelist[most_votes_index]

percent = [round(i, 3) for i in percent]


    

Output = (
    "Election Results"
    f"---------\n"
    f"Total Votes: {votes}"
    f"{candidate_data}"
    f"---------\n"
    f"Winner: {winner}"
    f"---------\n")

print(Output)




with open ('PyPoll.txt','w') as text_file:
    textwriter = text_file.write(Output)
       