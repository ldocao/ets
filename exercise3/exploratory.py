import load_data as ld
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import ipdb
import matplotlib
matplotlib.style.use('ggplot')



csvfile = "../Exercise.xlsx"
df = ld.load_dataset(csvfile)
list_df = ld.separate_diet(df)

for diet in list_df:
    mean_time = diet.mean(axis=1).plot(label="Diet"+str(np.unique(diet["Diet"])))

plt.legend()
plt.savefig("mean.pdf")



plt.figure()    
for diet in list_df:
    diet_string = str(np.unique(diet["Diet"])[0])
    diet.to_csv("chicken_weights_"+diet_string+".csv")
    weights_colnames = list(diet.columns.values)
    weights_colnames.remove('Diet')
    diet = diet.reset_index()
    plt.figure()
    ax = diet.plot(kind="scatter", x="Time", y=0) 
    ax.set_ylim([0,400])
    ax.set_xlim([0,25])
    ax.set_ylabel("Weight")

    for weight in weights_colnames:
        print weight, diet["Diet"]
        diet.plot(kind="scatter", x="Time", y=weight, ax=ax)


    plt.savefig("scatter_"+diet_string+".pdf")


