import pandas as pd

df = pd.read_csv("Data.csv",index_col="No")
print(df["Weight"].to_string())
#sıralama sınırlama
print(df[["Weight","Name","Height"]].to_string())
print(df["Name"].iloc[[x for x in range(25)]])
"""
af = df["Name"]
print(af.iloc[[x for x in range(40)]])
"""
#liste kuralları hepsi geçerli