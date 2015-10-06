import load_data as ld
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import ipdb
import matplotlib
matplotlib.style.use('ggplot')



csvfile = "../Exercise.xlsx"
df_raw = ld.load_dataset(csvfile)

group = df_raw.groupby("Diet")


for i in xrange(1,5):
    df = group.get_group(i)
    x = df["Time"]
    y = df["Weight"]
    results = np.polyfit(x,y,1)
    print "For diet:", i, "slope=", results[0]
    xx = np.arange(0, 25)
    yy = results[1] + results[0]*xx
    plt.figure()
    df.plot(kind="Scatter", x="Time", y="Weight")
    plt.plot(xx,yy)
    plt.show()

