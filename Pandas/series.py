import pandas as pd

data = [100,200,300]

freshly_created_series = pd.Series(data,index=["a","b","c"])
print(freshly_created_series)
print(freshly_created_series.iloc[2]) #integerloc -> 2
print(freshly_created_series.loc["a"]) #locate -> a

freshly_created_series.loc["b"] = 1000
#numpy tarzı
print(freshly_created_series[freshly_created_series >= 200])

#dict
calories = {
    "day1:": 1500,
    "day2:": 1000,
    "day3:": 2000,
    "day4:": 2200,
}
#S büyük olmalı constructor
series = pd.Series(calories)
print(series[series < 1900])
print(series.iloc[2])
series.iloc[1] += 100