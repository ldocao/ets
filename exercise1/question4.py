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
##making a prediction requires to go through feature engineering, gathering and mining data, to learn and make a prediction. However, here, with this dataset only, there is no way we can learn from the data. I could go and look for some additional data, but I have no idea which stock the prices are about, nor if there are even real. So i will go for the three most simple models I can make, ie : random walk, linear regression, and smooth curve (linear on 5 points).



def linear_line(x, y, n=100):
    """Return a linear fit of y(x) with n points"""

    results = np.polyfit(x, y, 1)
    xx = np.linspace(np.min(x),np.max(x), n)
    yy = results[1] + results[0]*xx ##linear regression
    return xx, yy


## linear regression
prices_colname = ["Price1", "Price2", "Price3", "Price4", "Price5"]
time = df["Time"]
t0 = time.values[0]
x = ((time - t0)/np.timedelta64(1, 'm')).values #convert in minutes for fit
df["Time"] = x #replace time by float for plot

for price in prices_colname:
    y = df[price].values
    print "For :", price
    df.plot(kind="Scatter", x="Time", y=price)


    ##linear regression
    xx, yy = linear_line(x,y)
    plt.plot(xx,yy)

    ##smoothing curve, linear extrapolation on last 5 points
    xx = savgol_filter(x, 5, 1)
    yy = savgol_filter(y, 5, 1)
    size_x = len(x)
    plt.plot(xx, yy, "g", linewidth=3,alpha=0.5)


    plt.show()