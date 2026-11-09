import pandas as pd

#temizleme
df = pd.read_csv("Data.csv")
df = df.drop(columns=["Legendary","No"])
print(df)

#handle missing type
da = pd.read_csv("Data.csv")
da = da.dropna(subset=["Type2","Height"])
print(da.to_string())

dk = pd.read_csv("Data.csv")
dk = dk.fillna({"Type2": "None"})
print(dk)

#fix inconsistent values
dr = pd.read_csv("Data.csv")
type_rep = "Grass"
dr["Type1"] = dr["Type1"].replace({type_rep: type_rep.upper()})
print(dr)

#standartizetext
dy = pd.read_csv("Data.csv")
dy["Name"] = dy["Name"].str.lower()
#fix data types
dy["Legendary"] = dy["Legendary"].astype(bool)
print(dy)
#remove duplicates
dy = dy.drop_duplicates()
print(dy)