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



##question4
##making a prediction requires to go through feature engineering, gathering and mining data, to learn and make a prediction. However, here, with this dataset only, there is no way we can learn from the data. I could go and look for some additional data, but I have no idea which stock the prices are about, nor if there are even real. So i will go for the two most simple models I can make, ie : linear regression, and smooth curve (linear on 5 points). bsically, the random walk and linear regression depends on the whole timeline whereas the smooth curve depends only on the last N points.






## linear regression
prices_colname = ["Price1", "Price2", "Price3", "Price4", "Price5"]
time = df["Time"]
t0 = time.values[0]
unit = np.timedelta64(1, 'D') #unit of time is minutes
x = ((time - t0) / unit).values #convert in minutes for fit
df["Time"] = x #replace time by float for plot
nx = len(x)
final_x = x[nx-1] + np.timedelta64(1, "D") / unit #time we want to predict the prices at
for price in prices_colname:
    print "For :", price
    y = df[price].values
    df.plot(kind="Scatter", x="Time", y=price)


    ##linear regression
    results = np.polyfit(x, y, 1)
    xx = np.linspace(np.min(x),np.max(x), 100)
    yy = results[1] + results[0]*xx ##linear regression
    final_y = results[1] + results[0]*final_x
    plt.plot(xx, yy, color="k")
    plt.plot(final_x, final_y, "k*")

    ##smoothing curve, linear extrapolation on last 5 points
    ###first plot the smooth curve
    nfit = 5
    xx = savgol_filter(x, nfit, 1)
    yy = savgol_filter(y, nfit, 1)
    plt.plot(xx, yy, "r", linewidth=3,alpha=0.5)

    ###add final point
    last_x = x[nx-nfit:nx]
    last_y = y[nx-nfit:nx]
    results = np.polyfit(last_x, last_y, 1)
    final_y = results[1] + results[0]*final_x
    plt.plot(final_x, final_y, "r*")
    plt.xlabel("Time [days]")
    plt.savefig("question4_"+price+".pdf")