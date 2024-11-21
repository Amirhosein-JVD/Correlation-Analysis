import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

X = ['STAD', 'BLCA', 'KIRC', 'COAD']
pearson = [20.4, 23.54, 18.65, 23.27]
spearman = [27.7, 40.63, 44.08, 34.28]
equal = [51.9, 35.83, 37.27, 42.45]

X_axis = np.arange(4)
width = 0.25
plt.bar(X_axis- 0.2, pearson, 0.2, label='Pearson > Spearman')
addlabels(X_axis- 0.2, pearson,0.2)
plt.bar(X_axis, spearman, 0.2 , label='Spearman > Pearson')
plt.bar(X_axis+ 0.2, equal, 0.2 , label='Spearman = Pearson')

plt.xticks(X_axis, X)
plt.xlabel("Cancers")
plt.ylabel("Percentage")
#plt.title("Disagreement among Pearson & Spearman")
plt.legend()
plt.show()