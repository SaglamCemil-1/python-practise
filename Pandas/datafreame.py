import pandas as pd

data = {
    "name": ["A","B","C"],
    "age" : [15,25,35]
}
df = pd.DataFrame(data)
kf = pd.DataFrame(data,index=["A1","A2","A3"])
print(df)
print(kf)
print("---------------<>-------------")
print(kf.loc["A1"])
print(df.iloc[1])

#adding a new coulmn
df["Position"] = ["KX1","KX2","KX3"]
#adding a new row
new_row = pd.DataFrame(
    [{"name":"D","age":45,"Position":"KX4"}], index=[3]
    #3 ten sonra ekstrada olursa 4 eğer 2 farklı varsa index= [3,4]
)
df = pd.concat([df,new_row])
print(df)