import pandas as pd
import numpy as np
import math

from pandas.core.interchange import column

new_list_to_use_asindex = ["A","T","K"]
new_obj = pd.Series([1,9,17],index=new_list_to_use_asindex)
print(new_obj.index) #index | atamalı yoksa default
print(new_obj["A"]) #numpy gibi array_like erişim
print(new_obj[new_list_to_use_asindex])
print(new_obj[new_obj>5]) #siler: False statement
print(new_obj*2) #çarpma vektör dahil

#index -> index_1  data_1
#         index_2  data_2
print("---------------->><<-------------")
#dict -> Series()
brand_and_prices = {"Audi": 7000,"Mercedes": 10000}
dict_to_Series = pd.Series(brand_and_prices)
print(dict_to_Series)
brand_and_prices_copy = dict_to_Series.to_dict()
print(brand_and_prices_copy)
print(pd.notna(dict_to_Series)) #isna -> tersi
print("---------------->><<-------------")
"""
serie_1 ---> {a:b,c:d,e:f}
serie_2 ---> {a:z,k:y,e:t,u:l}
serie_1 + serie_2 ==> a:b+z, c:nan k:nan u:nan e:t+f    """

print("---------------->><<-------------")
df = pd.DataFrame(dict_to_Series) #ilk 5 tail son5
print(df.head())
print(df.loc["Audi"])

df_2 = pd.DataFrame([8775],index=["BMW"])
print(df_2)
df = pd.concat([df_2,df])
print(df)
print("---------------->><<-------------")
"""
val = pd.Series([-1.2, -1.5, -1.7], index=[2, 4, 5])
frame2["debt"] = val
tüm satırları [2,4,5] i değiştirir
"""

df["debt"] = np.nan
print(df)
df["debt"] = pd.Series([-1,2],index=["Audi","Mercedes"])
print(df)
print("---------------->><<-------------")

s = [1,2,3,4]
new_series = pd.Series(s)
new_series_numpy = new_series.to_numpy()
print(new_series_numpy.reshape(2,2).T)
print("---------------->><<-------------")

df = df.reindex(["Mercedes","BMW","Audi"])
print(df)
#frame.reindex(columns=states) reindex herşeye bakabilir
#frame.reindex(states, axis="columns") böyle de olur

def mak(x):
    # frame apply da kullanılacak
    return x.max() - x.min()

frame = pd.DataFrame(np.random.standard_normal((4,3)),
                  columns=list("abc"),
                  index=["utah","ohio","texas","oregon"])
print(np.abs(frame))
print(frame.apply(mak,axis="columns"))

frame = pd.DataFrame(np.random.standard_normal((4,3)),
                  columns=list("abc"),
                  index=["utah","ohio","texas","oregon"])

def my_format(x):
   return f"{x:.2f}"

print(frame.map(my_format))

#5.4 bitti