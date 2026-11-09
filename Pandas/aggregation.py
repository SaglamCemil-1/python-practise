import pandas as pd

#summarize analyzed data

df = pd.read_csv("Data.csv")

#burdakiler df ye uyuglanabilir
print(f"{df.mean(numeric_only=True)}")
print(f"{df.sum(numeric_only=True)}")
print(f"{df.min(numeric_only=True)}")
print(f"{df.max(numeric_only=True)}")
print(f"{df.count()}") #nan saymaz null saymaz

#burdakiler sadece sütunlara
print(f"{df["Height"].mean()}")
print(f"{df["Height"].sum()}")
print(f"{df["Height"].min()}")
print(f"{df["Height"].max()}")
print(f"{df["Height"].count()}")

print(df)
group = df.groupby("Type1") #object
print(group["Height"].mean()) #Type1 aynı olanlar arasında karşılaştırma
print(group["Height"].sum())
print(group["Height"].count().max())