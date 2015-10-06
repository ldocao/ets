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
plt.show()




for diet in list_df:
    weights_colnames = list(diet.columns.values)
    weights_colnames.remove('Diet')
    diet = diet.reset_index()
    for weight in weights_colnames:
        print weight
        try:
            diet.plot(kind="scatter", x="Time", y=weight, ax=ax)
        except NameError:
            ax = diet.plot(kind="scatter", x="Time", y=weight)
    plt.show()


