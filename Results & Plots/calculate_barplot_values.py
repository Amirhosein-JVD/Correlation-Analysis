import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import Binarizer

p_corr = pd.read_csv("~/pearson_KIRC.csv")
s_corr = pd.read_csv("~/spearman_KIRC.csv")
p_corr = p_corr.fillna(0)
s_corr = s_corr.fillna(0)
p_corr = p_corr.to_numpy()
s_corr = s_corr.to_numpy()
x = len(p_corr)
diff_p_s_corr = np.zeros((x,x))
diff_p_s_corr  = np.subtract(p_corr,s_corr)
transformer = Binarizer(threshold = 0.05).fit(diff_p_s_corr)
diff_p_s_corr = transformer.transform(diff_p_s_corr)
diff_p_s_corr = pd.DataFrame(diff_p_s_corr)
print("KIRC: ")
print(((diff_p_s_corr.sum()).sum())/((x*x)-x))

