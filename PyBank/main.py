import csv
import os

# Data file, output file
file_to_load = os.path.join("Resources", "budget_data.csv")  
file_to_output = os.path.join("Analysis", "budget_analysis.txt")  

# Initialize variables and lists
totalMonths = 0
totalNetPL = 0
currentPL = 0 
priorPL = 0
changePL = 0
changePLList = [] # list for month-over-month change in profit
monthList = [] # list for corresponding month
maxChangePLList = ["", float()] # list to contain date and value for greatest % increase
minChangePLList = ["", float()] # list to contain date and value for greatest % decrease

# Open and read the csv
with open(file_to_load, "r", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile, delimiter = ",")

    # Skip header row
    header = next(reader)

    # Process each row of data
    # I FORMULATE SOLUTION SO DO NOT NEED TO TREAT FIRST DATA ROW IN ISOLATION, 
    # (GIVEN CHANGE IN PROFIT IS CALCULATED AGAINST PRIOR VALUE IN PRIOR ROW, AND ROW 2'S PRIOR ROW IS HEADER ROW)
    for row in reader:
        # Add 1 to running count of months
        totalMonths += 1
        # Obtain current PL value
        currentPL = int(row[1])
        # Add current PL value to running total net PL value
        totalNetPL += currentPL
        # Calculate month-over-month change in net PL, record to change list
        # Record corresponding month to month list
        if priorPL != 0:
            changePL = currentPL - priorPL
            changePLList.append(changePL)
            monthList.append(row[0])
        # Set prior PL used in next iteration to current PL value
        priorPL = currentPL
        # Determine greatest % increase in PL by comparing current change to max change so far
        if changePL > maxChangePLList[1]:
            maxChangePLList[1] = changePL
            maxChangePLList[0] = row[0]
        # Determine greatest % decrease in PL by comparing current change to min change so far
        if changePL < minChangePLList[1]:
            minChangePLList[1] = changePL
            minChangePLList[0] = row[0]
        
    # Calculate average net change across months:
    avgChange = sum(changePLList) / len(changePLList)

    # EASIER WAY TO DETERMINE GREATEST MONTH-OVER-MONTH PL INCREASE OR DECREASE, AND CORRESPONDING MONTHS:
    # MaxIncr = max(changePLList)
    # MaxIncrIndex = changePLList.index(MaxIncr)
    # MaxIncrMonth = monthList[MaxIncrIndex]
    # MaxDecr = min(changePLList)
    # MaxDecrIndex = changePLList.index(MaxDecr)
    # MaxDecrMonth = monthList[MaxDecrIndex]

# Generate output summary
output = (
    f"\nFinancial Analysis\n"
    f"\n--------------------------------------\n"
    f"\nTotal Months: {totalMonths}\n"
    f"\nTotal: ${totalNetPL}\n"
    f"\nAverage Change: ${avgChange:.2f}\n"
    f"\nGreatest Increase in Profits: {maxChangePLList[0]} (${maxChangePLList[1]})\n"
    # f"\nGreatest Increase in Profits: {MaxIncrMonth} (${MaxIncr})\n"  # THIS LINE WOULD REPLACE PRIOR IF USE ALTERNTIVE SOLUTION ABOVE
    f"\nGreatest Decrease in Profits: {minChangePLList[0]} (${minChangePLList[1]})\n\n"
    # f"\nGreatest Decrease in Profits: {MaxDecrMonth} (${MaxDecr})\n\n"  # THIS LINE WOULD REPLACE PRIOR IF USE ALTERNATIVE SOLUTION ABOVE
    )

# Print output to terminal
print(output)

# Export output to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
