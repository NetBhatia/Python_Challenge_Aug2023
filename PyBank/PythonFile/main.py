# Import the os module
import os
# Module for reading CSV files
import csv

csvpath = os.path.join('..','Resources', 'budget_data.csv')

# Open and Read CSV file
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')

    # Set initial values for variables
    months_count = 0
    rows_count = 0
    totalsum = 0
    previous_month_rev = 0
    average_income_change = 0
    income_change_list = []
    change_month = []
    max_increase = ["", 0]
    max_decrease = ["", 99999999]

    # Skip the header
    csv_header = next(csvreader)

    # Loop through the csv file
    for row in csvreader:

        # Get row count
        months_count = months_count + 1
        
        # Get total revenue sum
        netincome = int(row[1])
        totalsum = totalsum + netincome

        # Calculate the changes in "Profit/Losses" over the entire period
        income_change = float(row[1]) - previous_month_rev
        previous_month_rev = float(row[1])
        if rows_count > 0:
            income_change_list = income_change_list + [income_change]
            change_month = [change_month] + [row[0]]
        rows_count = 1

        # calculate the highest increase in profits (date and amount) for the period
        if income_change>max_increase[1]:
            max_increase[1]=int(income_change)
            max_increase[0]=row[0]

        # Calculate the highest decrease in profits (date and amount) for the period
        if income_change<max_decrease[1]:
            max_decrease[1]=int(income_change)
            max_decrease[0]=row[0]
    
# Calculate average of the changes
average_income_change = sum(income_change_list)/len(income_change_list)
average_income_change = round(average_income_change, 2)

# Update analysis to a txt file

# Specify the file to write to
output_path = os.path.join("..", "Analysis", "Analysis.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("---------------------\n\n")
    txtfile.write(f"Total Months: {months_count}\n\n")
    txtfile.write(f"Total Income: ${totalsum}\n\n")
    txtfile.write(f"Average Change: $ {average_income_change}\n\n")
    txtfile.write(f"Greatest Increase in Profits: {max_increase[0]} (${max_increase[1]})\n\n")
    txtfile.write(f"Greatest Decrease in Profits: {max_decrease[0]} (${max_decrease[1]})")

print("\nFinancial Analysis")
print("-------------------------------------\n")
print(f"Total Months: {months_count}\n")
print(f"Total Income: ${totalsum}\n")
print(f"Average Change: $ {average_income_change}\n")
print(f"Greatest Increase in Profits: {max_increase[0]} (${max_increase[1]})\n")
print(f"Greatest Decrease in Profits: {max_decrease[0]} (${max_decrease[1]})")














    

