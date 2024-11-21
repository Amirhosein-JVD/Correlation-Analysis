import pandas as pd
import statsmodels.api as sm
import pylab as py

data = pd.read_csv("~/STAD_allsamples_diff_genexpression.csv")
gene_names = data['Unnamed: 0']
data = data.drop(columns = 'Unnamed: 0')
print(data.shape)
# select ith gene to draw it qqplot
i = 23
x = str(gene_names[i])+".pdf"
sm.qqplot(data.iloc[23, :], line='45', fit=True)
py.savefig(x,format="pdf", bbox_inches="tight")
