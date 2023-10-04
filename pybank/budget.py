import csv
import os

file_path = os.path.join("..", "resources", "budget_data.csv")

with open(file_path, "r") as csv_file:
    # Create lists to store the profit/loss data and dates
    profit_loss = []
    dates = []

    # Read the CSV file row by row
    csv_reader = csv.reader(csv_file)
    next(csv_reader)  # Skip the header row

    # Iterate over the rows in the CSV file
    for row in csv_reader:
        # Get the profit/loss amount as a float
        profit_loss_value = float(row[1])

        # Add the profit/loss value to the list
        profit_loss.append(profit_loss_value)

        # Get the date
        date = row[0]

        # Add the date to the list
        dates.append(date)

# Calculate the average change in profit/loss
average_change = round((profit_loss[-1] - profit_loss[0]) / (len(profit_loss) - 1), 2)

# Calculate the total profit/loss
total_profit_loss = int(sum(profit_loss))

# Find the greatest increase and its date
greatest_profit_loss = int(max(profit_loss))
greatest_profit_loss_date = dates[profit_loss.index(greatest_profit_loss)]

# Find the greatest decrease and its date
greatest_decrease = int(min(profit_loss))
greatest_decrease_date = dates[profit_loss.index(greatest_decrease)]

# Print the results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(dates)}")
print(f"Total: ${total_profit_loss}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {greatest_profit_loss_date} (${greatest_profit_loss})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")
