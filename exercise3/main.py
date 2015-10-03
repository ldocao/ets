import pandas as pd
import numpy as np



def prepare_dataset(csvfile):
    """Return raw dataframe"""

    df = pd.read_excel(csvfile,sheetname="Test3",skiprows=9, header=1)
    df = df[["Weight","Time", "Chick", "Diet"]]

    return df

csvfile = "../Exercise.xlsx"
df = prepare_dataset(csvfile)

