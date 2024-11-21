# find intersect of hubs(high degree nodes) and survival-related genes
import pandas as pd

p_rank_data = pd.read_csv("~/pearsonSSKirc.csv")
s_rank_data = pd.read_csv("~/spearmanSSKirc.csv")
k_rank_data = pd.read_csv("~/kendallSSKirc.csv")
d_rank_data = pd.read_csv("~/dcorSSKirc.csv")

survival_data = pd.read_csv("~/KIRC_survival.csv")
print(len(survival_data))

# Select 100 top high degree(hub) nodes
rank_data_filter = p_rank_data.iloc[:100,:]
x = rank_data_filter["gene"].values
intersect = survival_data[survival_data["gene"].isin(x)]

print(len(rank_data_filter)," top genes were selected:")
print("KIRC cancer")
print("pearson")
print(len(intersect)/len(rank_data_filter))

rank_data_filter = s_rank_data.iloc[:100,:]
x = rank_data_filter["gene"].values
intersect = survival_data[survival_data["gene"].isin(x)]

print("spearman")
print(len(intersect)/len(rank_data_filter))

rank_data_filter = k_rank_data.iloc[:100,:]
x = rank_data_filter["gene"].values
intersect = survival_data[survival_data["gene"].isin(x)]

print("kendall")
print(len(intersect)/len(rank_data_filter))

rank_data_filter = d_rank_data.iloc[:100,:]
x = rank_data_filter["gene"].values
intersect = survival_data[survival_data["gene"].isin(x)]

print("dcor")
print(len(intersect)/len(rank_data_filter))