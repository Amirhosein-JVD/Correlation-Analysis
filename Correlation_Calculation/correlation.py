import pandas as pd
import numpy as np
from dcor import distance_correlation
from datetime import datetime
import os


os.chdir(os.path.dirname(os.path.abspath(__file__)))
print("Current working directory:", os.getcwd())


METHODS = ["spearman", "pearson", "kendall", "dcor"]

def main():
  
    data = pd.read_csv("../Data/KIRC.csv")
    data = data.transpose().iloc[1:, :]
    preparing_correlation_folders()
    # calculate_dcor_correlation_matrix(data)
    # calculate_kendall_correlation_matrix(data)
    # calculate_spearman_correlation_matrix(data)
    calculate_pearson_correlation_matrix(data)

def preparing_correlation_folders():
    for method in METHODS:
        folder = method + "Method"
        if not os.path.isdir(folder):
            os.makedirs(folder)


def calculate_dcor_correlation_matrix(data:pd.DataFrame):
    """This function calculates the correlation matrix based on the distance correlation method and outputs it in a CSV file.

    Args:
        data (pd.DataFrame): The data for which we intend to calculate the correlation matrix.
    """
    
    start_time = datetime.now()
        
    # number of columns
    number_of_columns = data.shape[1]
    
    # Creating a two-dimensional ndarray to save the correlation results
    temp_dcor = np.zeros((number_of_columns, number_of_columns))

    # We calculate the pairwise correlation of the columns and save it in a CSV file.
    # To avoid redundant computations, the matrix is calculated in a lower triangular form.
    for i in range(number_of_columns):
        for j in range(i, number_of_columns):
            temp_dcor[i][j] = distance_correlation(np.array(data.iloc[:, i]).astype(np.float64),
                                            np.array(data.iloc[:, j]).astype(np.float64))
            
        # After calculating each row of the matrix, we print its completion status.
        print("done" + str(i))


    # Completing the correlation matrix using its symmetric property.
    for i in range(number_of_columns):
        for j in range(i):
            temp_dcor[i][j] = temp_dcor[j][i]

    # Saving the results
    pd.DataFrame(temp_dcor).to_csv("dcorMethod/dcor.csv", index=False)

    end_time = datetime.now()

    # Printing the computation duration.
    print('Duration: {}'.format(end_time - start_time))



def calculate_kendall_correlation_matrix(data:pd.DataFrame):
    """This function calculates the correlation matrix based on the kendall correlation method and outputs it in a CSV file.

    Args:
        data (pd.DataFrame): The data for which we intend to calculate the correlation matrix.
    """
    
    start_time = datetime.now()

    # Calculating the correlation matrix using the Kendall method.
    corr = data.corr(method="kendall")
    
    # Saving the results
    corr.to_csv("kendallMethod/kendall.csv", index=False)

    end_time = datetime.now()

    # Printing the computation duration.
    print('Duration: {}'.format(end_time - start_time))

def calculate_spearman_correlation_matrix(data:pd.DataFrame):
    """This function calculates the correlation matrix based on the Spearman correlation method and outputs it in a CSV file.

    Args:
        data (pd.DataFrame): The data for which we intend to calculate the correlation matrix.
    """
    
    start_time = datetime.now()
    
    # Calculating the correlation matrix using the Spearman method.
    corr = data.corr(method="spearman")

    # Saving the results
    corr.to_csv("spearmanMethod/spearman.csv", index=False)

    end_time = datetime.now()

    # Printing the computation duration.
    print('Duration: {}'.format(end_time - start_time))


def calculate_pearson_correlation_matrix(data:pd.DataFrame):
    """This function calculates the correlation matrix based on the Pearson correlation method and outputs it in a CSV file.

    Args:
        data (pd.DataFrame): The data for which we intend to calculate the correlation matrix.
    """
    start_time = datetime.now()
        
    # Calculating the correlation matrix using the Pearson method.
    corr = data.corr(method="pearson")

    # Saving the results
    corr.to_csv("pearsonMethod/pearson.csv", index=False)

    end_time = datetime.now()

    # Printing the computation duration.
    print('Duration: {}'.format(end_time - start_time))

if __name__ == "__main__":
    main()