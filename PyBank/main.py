# import modules
import csv
import os

# source to read budget data file
fileLoad = os.path.join("Resources", "budget_data.csv")  # Input file path
outputFile = os.path.join("analysis", "budgetAnalysis.txt") # Output file path

# Define variables to track the financial data
totalMonths = 0 # initialize the total months to 0
totalRevenue = 0 # initialize the total revenue to 0
monthlyChanges = [] # initialize the list of monthly net changes
months = [] # initialize the list of months

# Open and read the csv
with open(fileLoad) as budgetData:
    csvreader = csv.reader(budgetData)

    # Read the header row
    header = next(csvreader)
    # move to the first row
    firstRow = next(csvreader)

    # increment the count of the total months
    totalMonths += 1

    # Track the total amount of revenue
        # revenue is in index 1 
    totalRevenue += float(firstRow[1])

    # establish the previous revenue
        # revenue is in index 1
    previousRevenue = float(firstRow[1])

    # Process each row of data
    for row in csvreader:
         # increment the count of the total months
        totalMonths += 1

        # Track the total amount of revenue
            # revenue is in index 1 
        totalRevenue += float(row[1])

        # Track the net change
        netChange = float(row[1]) - previousRevenue
       
       # add on to the list of monthly changes
        monthlyChanges.append(netChange)

        # add the first month a change occured
            # month is in index 0
        months.append(row[0])

        # update the previous revenue
        previousRevenue = float(row[1])

# Calculate the average net change per month
averageChangePerMonth = sum(monthlyChanges) / len(monthlyChanges)

greatestIncrease = [months [0], monthlyChanges[0]] # holds the month and value of greatest increase
greatestDecrease = [months [0], monthlyChanges[0]] # holds the month and value of greatest decrease

# use loop to calculate the index of the greatest and least monthy change

for m in range(len(monthlyChanges)):
    # Calculate the greatest increase in profits (month and amount)
    if(monthlyChanges[m] > greatestIncrease[1]):
        # if the value is greater than the greatest increase, that value becomes the new greatest increase
        greatestIncrease[1] = monthlyChanges[m]
        # update the month
        greatestIncrease[0] = months[m]

        # Calculate the greatest decrease in losses (month and amount)
    if(monthlyChanges[m] < greatestDecrease[1]):
        # if the value is greater than the greatest increase, that value becomes the new greatest decrease
        greatestDecrease[1] = monthlyChanges[m]
        # update the month
        greatestDecrease[0] = months[m]

# Generate the output summary
output = (
    f"Financial Analysis \n"
    f"-------------------------\n"
    f"Total Months: {totalMonths} \n"
    f"Total Net: ${totalRevenue:,.2f} \n" 
    f"Average Change: ${averageChangePerMonth:,.2f} \n"
    f"Greatest Increase in Profits: {greatestIncrease[0]} Amount ${greatestIncrease[1]:,.2f} \n"
    f"Greatest Decrease in Profits: {greatestDecrease[0]} Amount ${greatestDecrease[1]:,.2f} \n"
)
# Print the output to the console / terminal
print(output)

# Write the results to a text file
with open(outputFile, "w") as textfile:
        textfile.write(output)
