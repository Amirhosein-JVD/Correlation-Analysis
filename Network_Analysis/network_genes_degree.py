import pandas as pd
import numpy as np
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
print("Current working directory:", os.getcwd())


def main():
        
    # Reading data
    mainData = pd.read_csv("../Data/KIRC.csv")
    
    # Getting the threshold as input.
    threshold = ask_threshold()
    calculate_degree_of_genes_and_network_matrix(mainData, threshold)

def ask_threshold():
    try:
        threshold = float(input("Please enter a threshold for the correlation values: "))
        if threshold < -1 or threshold > 1:
            raise ValueError
        return threshold
        
    except(ValueError):
        return ask_threshold()

def calculate_degree_of_genes_and_network_matrix(mainData:pd.DataFrame, threshold:float):

    """This function can be used to calculate the degree of each gene in different correlations,
    and it also outputs the necessary matrix for drawing the network in "Cytoscape".
    Methods : ["pearson", "spearman", "kendall", "dcor"]
    
    Args:
        mainData (pd.DataFrame): Raw data.
        threshold (float): This value determines whether or not to establish an edge between two genes in the network.
    """
    
    # Saving names
    buffer = pd.DataFrame(np.transpose(mainData))
    buffer = pd.DataFrame(buffer.iloc[0, :])

    # Generating degrees
    for method in ["pearson.csv", "spearman.csv", "kendall.csv", "dcor.csv"]:

        # Reading the data
        data = pd.read_csv(f"../Correlation_Calculation/{method[:-4]}Method/{method}")

        # Convert all elements grater than threshold to 1 and otherwise 0
        data = pd.DataFrame((abs(data) > ask_threshold()))

        # Change titles
        data.columns = buffer.iloc[:, 0]

        # Saving data for drawing network
        data.to_csv(f"Zero_One_Matrices/{method[:-4]}_zero_one_matrix.csv", index=False)

        # Calculating sum of columns
        data = pd.DataFrame(data.sum())

        # Reset indexes
        data.reset_index(drop=True, inplace=True)
        buffer.reset_index(drop=True, inplace=True)

        # Saving the results
        final_result = pd.concat([buffer.transpose(), data.transpose()]).transpose()
        final_result.to_csv(f"Not_Sorted_Degree/{method[:-4]}NotSorted.csv", index=False)

if __name__ == "__main__":
    main()