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






