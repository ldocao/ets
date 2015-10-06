import pandas as pd
import numpy as np


xlfile = "../Exercise.xlsx"
df = pd.read_excel(xlfile,sheetname="Test1", skiprows=11, header=1)
df = df[["Unnamed: 2","Prices1", "Prices 2", "Prices 3", "Prices 4"]]
df.columns = ["Time", "Price1", "Price2", "Price3", "Price4"]

