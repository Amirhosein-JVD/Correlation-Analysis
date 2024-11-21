import pandas as pd
import numpy as np
from scipy import stats

data = pd.read_csv("~/KIRC_allsamples_diff_genexpression.csv")
gene_names = data['Unnamed: 0']
data = data.drop(columns = 'Unnamed: 0')

x = np.ones((len(data),2))
for i in range(len(data)):
    res = stats.shapiro(data.iloc[i, :])
    x[i,0] = res.statistic
    x[i,1] = res.pvalue
x = pd.DataFrame(x,columns= ['stat','pvalue'])
x = x.loc[x.pvalue < 0.05]
x.to_csv("KIRC_shapiro-wilk.csv",index= False)

