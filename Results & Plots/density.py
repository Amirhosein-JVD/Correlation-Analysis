# Importing necessary libraries
import matplotlib.pyplot as plt  # For plotting graphs
import pandas as pd  # For reading and handling CSV data
import os  # For interacting with the operating system (e.g., to change directories)

# Change the current working directory to the directory of the script
os.chdir(os.path.dirname(os.path.abspath(__file__)))
# Print the current working directory to verify the change
print("Current working directory:", os.getcwd())

# List of correlation methods to analyze
METHODS = ["pearson", "spearman", "dcor", "kendall"]

# Main function to iterate through the methods and analyze the data for each
def main():
    # Iterate through each correlation method and call the density function
    for i in METHODS:
        density(i)

# Function to convert a number to a string with 5 characters (including decimals)
def creatorStr(number):
    string = str(number)  # Convert the number to a string
    if string == "nan":  # If the value is NaN, return a default value of "1.0"
        string = "1.0"
    # Ensure the string is exactly 5 characters long, padding with zeros if necessary
    while len(string) != 5:
        string += "0"
    return string  # Return the formatted string

# Function to calculate and plot the density of correlation coefficients for a given method
def density(method):
    # Read the data from a CSV file based on the correlation method
    data = pd.read_csv(f"../Correlation_Calculation//{method}Method/{method}.csv")
    
    # Initialize a count value to 0.001
    count = 0.001
    limit = ['0.000']  # List to store the correlation values (formatted to 5 decimal places)

    # Generate 1000 values from 0.001 to 1.000 and add them to the 'limit' list
    for i in range(1000):
        limit.append(str(count)[:5])  # Add the current count to the limit list, formatted to 5 decimal places
        count += 0.001  # Increment the count by 0.001

    result = {}  # Dictionary to store the frequency of each correlation value

    # Initialize the dictionary with 0 for each limit value
    for i in limit:
        result[i] = 0

    # Loop through the data (assumes a square matrix of correlations)
    for i in range(data.shape[1]):  # Iterate through columns
        for j in range(i, data.shape[1]):  # Iterate through columns (symmetrical matrix)
            # Calculate the absolute value of the correlation coefficient, round it to 3 decimal places, and format it
            result[creatorStr((round(abs(data.iloc[i, j]), 3)))] += 1  # type: ignore # Increment the count for this correlation value

    y = []  # List to store the frequencies of each correlation value

    # Populate the y list with the counts for each value in the limit list
    for i in limit:
        y.append(result[i])

    maximum = max(y)  # Find the maximum frequency value
    print(method + " :")  # Print the method name
    print(f"Maximum Frequency: {maximum}")  # Print the maximum frequency value

    # Print the correlation values that have the highest frequency
    for i in limit:
        if result[i] == maximum:
            print(f"The correlation value with the highest frequency: {i}")

    # Plot the correlation density (method vs. frequency)
    plt.plot(limit, y, label=method)

    # Customize the plot (remove x-ticks and add the legend)
    plt.gca().set_xticks([])  # Hide x-axis ticks
    plt.legend()  # Display the legend
    plt.tight_layout()  # Adjust layout to avoid clipping of labels
    plt.show()  # Display the plot

# Ensure the script runs the main function when executed directly
if __name__ == "__main__":
    main()
