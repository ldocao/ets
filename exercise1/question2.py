import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
import matplotlib
import ipdb
matplotlib.style.use('ggplot')




xlfile = "../Exercise.xlsx"
df = pd.read_excel(xlfile,sheetname="Test1", skiprows=11, header=1)
df = df[["Unnamed: 2","Prices1", "Prices 2", "Prices 3", "Prices 4", "Prices 5"]]
df.columns = ["Time", "Price1", "Price2", "Price3", "Price4", "Price5"]
df.drop(df.index[:1],inplace=True)




##compute the value at risk for a period of 1 year, with risk alpha in percentage
## https://fr.wikipedia.org/wiki/Value_at_risk
df = df - df.mean() 
df.plot(kind="hist", bins=40, alpha=0.5, stacked=True)
plt.xlabel("Price")
plt.show()

alpha=0.05
results={} #store results as dict
for col in df.columns:
    try:
        results[col] = np.percentile(df[col], alpha*100)
    except TypeError:
        pass

print results
print "Descending risked price (alpha=0.05)", sorted(results, key=results.get)