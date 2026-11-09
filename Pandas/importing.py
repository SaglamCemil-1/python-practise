import numpy as np
import pandas as pd

df = pd.read_csv("Data.csv",index_col = "No")
print(df)
# readjson da var.
print(df.to_string())

"""
df.loc[df["Weight"]>1, "Height"] = 0.11
print(df.to_string())
"""
#df.loc[df["Name"] == "Mewtwo", "Weight"] = 17
df.loc[df["Height"] > 0, "Weight"] = np.nan
print(df.to_string())

for index,row in df.iterrows():
    print(f"{index} contains: \n{row}")