import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("~/KIRC_tumor_diff_expression.csv")
p_corr = pd.read_csv("~/pearson_KIRC.csv")
s_corr = pd.read_csv("~/spearman_KIRC.csv")
k_corr = pd.read_csv("~/kendall_KIRC.csv")
d_corr = pd.read_csv("~/dcor_KIRC.csv")

gene_names = data['Unnamed: 0']
data = data.drop(columns = 'Unnamed: 0')
p_corr = p_corr.to_numpy()
s_corr = s_corr.to_numpy()
k_corr = k_corr.to_numpy()
d_corr = d_corr.to_numpy()

# select ith and jth genes for scatter plot (example : i = 20 , j = 45)
i = 20
j = 45
plt.scatter(data.iloc[i,:],data.iloc[j, :])
plt.xlabel(gene_names[i])
plt.ylabel(gene_names[j])
p = "{:.2f}".format(p_corr[i,j])
s = "{:.2f}".format(s_corr[i,j])
k = "{:.2f}".format(k_corr[i,j])
d = "{:.2f}".format(d_corr[i,j])
plt.legend([f"Pearson:{p}\nspearman:{s}\nkendall:{k}\ndistance:{d}"],loc="lower right", frameon=False)
x = gene_names[i]+ "--"+gene_names[j]+ ".pdf"
plt.show()
plt.savefig(x, format="pdf", bbox_inches="tight")
