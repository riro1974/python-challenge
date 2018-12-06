import os
import csv
# Set path for file
pybank_csvpath = "C:/Data Science Bootcamp/Data Science Boot Camp/PYTHON_RT/election_data.csv"
# Open the CSV
curr_mth = prev_mth = last_mth = 0
with open(pybank_csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')  
    csvheader = next(csvfile)
    tot_vote = len(csvfile.readlines())
    csvfile.seek(0)
    csvheader = next(csvfile)
    mylist = Counter()
    for row in csvreader:
      mylist[row[2]] += 1
    max_vote = max(mylist, key=mylist.get)
    print("Election Results")   
    print("------------------------------")
    print (f"Total Votes: {tot_vote}")
    print("------------------------------")
    file = open('C:/Data Science Bootcamp/Data Science Boot Camp/PYTHON_RT/election_analysis_out.txt', 'w')
    file.write("Election Results" + '\n')   
    file.write("------------------------------" + '\n')
    file.write(f"Total Votes: {tot_vote}" + '\n')
    file.write("------------------------------" + '\n')
    for i in mylist:
            avg_vote = "{:.3%}".format(float(mylist[i] / tot_vote))
            print(f"{i}: {avg_vote} ({mylist[i]})")
            file.write(f"{i}: {avg_vote} ({mylist[i]})" + '\n')
csvfile.close()
print("------------------------------")
print(f"Winner: {max_vote}")
file.write("------------------------------" + '\n')
file.write(f"Winner: {max_vote}")
file.close()

