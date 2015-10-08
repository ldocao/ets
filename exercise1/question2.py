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

##compute the value at risk for a period of 1 year, with risk 5%
## https://fr.wikipedia.org/wiki/Value_at_risk

df.plot(kind="hist", bins=30, alpha=0.5)
plt.xlabel("Price")
plt.show()