import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
import matplotlib
from scipy.signal import savgol_filter
import ipdb
matplotlib.style.use('ggplot')




xlfile = "../Exercise.xlsx"
df = pd.read_excel(xlfile,sheetname="Test1", skiprows=11, header=1)
df = df[["Unnamed: 2","Prices1", "Prices 2", "Prices 3", "Prices 4", "Prices 5"]]
df.columns = ["Time", "Price1", "Price2", "Price3", "Price4", "Price5"]
df.drop(df.index[:1],inplace=True) #remove 31st december 2012
df = df.dropna()



##question5: I trust the prediction from smooth curve (cf question4). I'm looking for the highest relative prediction (cf question1)


## linear regression
prices_colname = ["Price1", "Price2", "Price3", "Price4", "Price5"]
time = df["Time"]
t0 = time.values[0]
unit = np.timedelta64(1, 'D') #unit of time is minutes
x = ((time - t0) / unit).values #convert in minutes for fit
df["Time"] = x #replace time by float for plot
nx = len(x)
nfit=5
final_x = x[nx-1] + np.timedelta64(1, "D") / unit #time we want to predict the prices at
for price in prices_colname:
    y = df[price].values

    ###add final point
    last_x = x[nx-nfit:nx]
    last_y = y[nx-nfit:nx]
    results = np.polyfit(last_x, last_y, 1)
    print "For", price, "slope=", results[0]
