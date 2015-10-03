import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import ipdb
import matplotlib
matplotlib.style.use('ggplot')

def load_dataset(csvfile):
    """Return raw dataframe"""
    df = pd.read_excel(csvfile,sheetname="Test3",skiprows=9, header=1)
    df = df[["Weight","Time", "Chick", "Diet"]]
    return df

def separate_diet(df):
    """Return a list of data frame separated by diet"""
    df_separated_by_diet = []
    for d in np.unique(df["Diet"].values):
        group_chick = df[df["Diet"] == d].groupby("Chick") #df by chick
        newdf = pd.DataFrame({"Time":[]}).set_index("Time") #store data for each diet
        for ichick, df_by_chick in group_chick:
            column_to_add = df_by_chick[["Time","Weight"]].set_index("Time")
            column_to_add.columns = ["Weight_"+str(ichick)]
            newdf = pd.concat([newdf, column_to_add ], axis=1)

        newdf["Diet"] = d #add diet information
        df_separated_by_diet.append(newdf)

    return df_separated_by_diet







csvfile = "../Exercise.xlsx"
df = load_dataset(csvfile)
list_df = separate_diet(df)

for diet in list_df:
    mean_time = diet.mean(axis=1).plot(label="Diet"+str(np.unique(diet["Diet"])))

plt.legend()
plt.show()






