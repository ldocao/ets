import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
import matplotlib
matplotlib.style.use('ggplot')

xlfile = "../Exercise.xlsx"
df = pd.read_excel(xlfile,sheetname="Test1", skiprows=11, header=1)
df = df[["Unnamed: 2","Prices1", "Prices 2", "Prices 3", "Prices 4", "Prices 5"]]
df.columns = ["Time", "Price1", "Price2", "Price3", "Price4", "Price5"]


df.plot(x="Time")
plt.show()



##question1
##compute the difference between 1s jan and 31st december, in absolute value
t0 = pd.Timestamp(np.datetime64('2003-01-01T01:00:00')) #add 1h to be midnight in UTC, to be used if you are in UTC+1 !
t1 = pd.Timestamp(np.datetime64("2003-12-31T01:00:00"))
begin = df[df["Time"] == t0]
end =  df[df["Time"] == t1]
profit = end.iloc[0] - begin.iloc[0]