import pandas as pd
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
print("Current working directory:", os.getcwd())


# Reading not sorted data
pearson = pd.read_csv("Not_Sorted_Degree/pearsonNotSorted.csv")
spearman = pd.read_csv("Not_Sorted_Degree/spearmanNotSorted.csv")
kendall = pd.read_csv("Not_Sorted_Degree/kendallNotSorted.csv")
dcor = pd.read_csv("Not_Sorted_Degree/dcorNotSorted.csv")


# Saving sorted data in sorted directory
METHODS_FILES = {"pearson.csv": pearson, "spearman.csv": spearman, "kendall.csv": kendall, "dcor.csv": dcor}

for method in METHODS_FILES:
    METHODS_FILES[method].sort_values(by="0", ascending=False).to_csv(f"Sorted_Degree/{method[:-4]}Sorted.csv", index=False)

