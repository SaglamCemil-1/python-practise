import pandas as pd

df = pd.read_csv("Data.csv")

heavy_ass_df = df[df["Weight"]>50]
print(heavy_ass_df)
heavy_ass_df_2 = df[(df["Legendary"] != 0) | (df["No"]<100)]
print(heavy_ass_df_2)