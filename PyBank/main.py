import os
import csv
# Set path for file
pybank_csvpath = "C:/Users/tayeb/Anaconda3/envs/PythonData/Resources/budget_data.csv"
# Open the CSV
curr_mth = prev_mth = last_mth = 0
rownum = 0
avgChng = []
with open(pybank_csvpath, newline="") as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',') 	
	csvheader = next(csvfile)
	tot_mth = len(csvfile.readlines())
	file = open('C:/Data Science Bootcamp/Data Science Boot Camp/PYTHON_RT/budget_analysis_out.txt', 'w')
	print (f"Total months: {tot_mth}")
	file.write(f"Total months: {tot_mth}" + '\n')
	csvfile.seek(0)
	csvheader = next(csvfile)
	total = 0
	for row in csvreader:
		total += round(float(row[1]))
		if rownum == 0:
			curr_mth = float(row[1])
			prev_mth = float(row[1])
		elif rownum == tot_mth + 1:
			last_mth = float(row[1])
		else:
			avgChng.append((row[0],float(row[1]) - prev_mth))
			prev_mth = float(row[1])
		rownum += 1
print(f"Total amount: {total}")
file.write(f"Total amount: {total}" + '\n')
max_avgChng = max(avgChng, key=lambda item: item[1])
min_avgChng = min(avgChng, key=lambda item: item[1])
avgChng_tot = round(sum(x[1] for x in avgChng)/ (tot_mth -1),2)
csvfile.close()
print(f"Average Change: {avgChng_tot}")
print(f"Greatest Increase in Profits: {max_avgChng[0]} (${round(max_avgChng[1])})")
print(f"Greatest Decrease in Profits: {min_avgChng[0]} (${round(min_avgChng[1])})")
file.write(f"Average Change: {avgChng_tot}" + '\n')
file.write(f"Greatest Increase in Profits: {max_avgChng[0]} (${round(max_avgChng[1])})" + '\n')
file.write(f"Greatest Decrease in Profits: {min_avgChng[0]} (${round(min_avgChng[1])})" + '\n')
file.close()
