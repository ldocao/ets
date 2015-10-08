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
##making a prediction requires to go through feature engineering, gathering and mining data, to learn and make a prediction. However, here, with this dataset only, there is no way we can learn from the data. I could go and look for some additional data, but I have no idea which stock the prices are about, nor if there are even real. So i will go for the three most simple models I can make, ie : random walk, linear regression, and smooth curve

## linear regression
prices_colname = ["Price1", "Price2", "Price3", "Price4", "Price5"]
time = df["Time"]
t0 = time.values[0]
x = ((time - t0)/np.timedelta64(1, 'm')).values #convert in minutes for fit
df["Time"] = x #replace time by float for plot

for price in prices_colname:
    y = df[price].values
    results = np.polyfit(x,y,1)
    print "For :", price
    xx = np.arange(np.min(x),np.max(x))
    yy = results[1] + results[0]*xx ##linear regression
    #yy2 = savgol_filter(y, 11, 3)
    df.plot(kind="Scatter", x="Time", y=price)
    plt.plot(xx,yy)
    #plt.plot(xx,yy2,"g")
    plt.show()