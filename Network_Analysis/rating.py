import pandas as pd
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
print("Current working directory:", os.getcwd())


METHODS= ["Dcor", "Pearson", "Spearman", "Kendall"]

def main():

    # Executing the functions defined below for each pair of correlation methods.
    for h in range(len(METHODS)):
        for j in range(h + 1, len(METHODS)):
            rating(METHODS[h], METHODS[j], 100)

def rater(arr):
    """The selected percentage of the available genes.

    Args:
        arr (List): A list.
    """
    rate_result = []
    flag = arr[0]
    count = 0
    rate = 0
    for i in arr:
        if flag != i:
            flag = i
            rate = count
        count += 1
        rate_result.append(rate)
 
    
def rating(method1:str, method2:str, percent:float):
    """This function takes two correlation methods and outputs the comparison results of these methods on the genes in a CSV file.

    Args:
        method1 (str): name of correlation 1
        method2 (str): name of correlation 2
        percent (float): The selected percentage of the available genes.
    """

    if not os.path.isdir(f"{method1}-{method2}"):
        os.makedirs(f"{method1}-{method2}")

    # Reading sorted data of each method
    data1 = pd.read_csv(f"../Network_Analysis/Sorted_Degree/{method1}Sorted.csv")
    data2 = pd.read_csv(f"../Network_Analysis/Sorted_Degree/{method2}Sorted.csv")

    # Based on the percentage provided as input in the function, we select the genes.
    data1 = pd.DataFrame(data1.iloc[:int(data1.shape[1] * (percent / 100)), :])
    data2 = pd.DataFrame(data2.iloc[:int(data1.shape[1] * (percent / 100)), :])

    # Finding intersect of hubs that exist in data of method 1 and method 2
    intersect = [i for i in data1.iloc[:, 0].tolist() if i in data2.iloc[:, 0].tolist()]

    # Filter the data of methods by intersect
    data1 = data1[data1["Unnamed: 0"].isin(intersect)]
    data2 = data2[data2["Unnamed: 0"].isin(intersect)]

    # Sort by name for concatenating
    data2 = data2.sort_values(by="Unnamed: 0")
    data1 = data1.sort_values(by="Unnamed: 0")

    # Reset indexes for sorting
    data1.reset_index(drop=True, inplace=True)
    data2.reset_index(drop=True, inplace=True)

    # Concat data of methods without column name of method2
    result = pd.concat([data1, data2.iloc[:, 1]], axis=1)

    # Update column names
    result.columns = ["Unnamed: 0", f"{method1} degree", f"{method2} degree"]

    # Sorting base on degree of method1 and saving it
    method1_sorted = result.sort_values(by=f"{method1} degree", ascending=False)
    # Reset indexes for sorting
    method1_sorted.reset_index(drop=True, inplace=True)

    # Sorting base on degree of method2 and store it
    method2_sorted = result.sort_values(by=f"{method2} degree", ascending=False)
    # Reset indexes for sorting
    method2_sorted.reset_index(drop=True, inplace=True)

    # Adding "rate of method 1" column to method1_sorted
    degree_method1 = method1_sorted[f"{method1} degree"].tolist()
    method1_sorted[f"rate {method1}"] = rater(degree_method1)

    # Adding "rate of method 2" column to method2_sorted
    degree_method2 = method2_sorted[f"{method2} degree"].tolist()
    method2_sorted[f"rate {method2}"] = rater(degree_method2)

    # Saving name of genes as list
    genes_name = result.iloc[:, 0].tolist()

    # New Columns
    total_rate = []
    method1_rate = []
    method2_rate = []

    # Generate Columns
    for gene in genes_name:
        # Generating total rate Columns
        total_rate.append(method1_sorted[method1_sorted["Unnamed: 0"] == gene].iloc[0, 3] + method2_sorted[
            method2_sorted["Unnamed: 0"] == gene].iloc[0, 3])
        
        # Generating rate of method1 Columns
        method1_rate.append(method1_sorted[method1_sorted["Unnamed: 0"] == gene].iloc[0, 3])
        
        # Generating rate of method2 Columns
        method2_rate.append(method2_sorted[method2_sorted["Unnamed: 0"] == gene].iloc[0, 3])

    # Adding columns
    result[f"{method1} rate"] = method1_rate
    result[f"{method2} rate"] = method2_rate
    result["Total rate"] = total_rate

    # Sort data based on total rate
    result = result.sort_values(by="Total rate1")
    
    # Reset indexes for sorting
    result.reset_index(drop=True, inplace=True)

    # storing CSV file
    result.to_csv(f"{method1}-{method2}/{method1[0]}-{method2[0]}.csv", index=False)

if __name__ == "__main__":
    main()