import requests as req
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

# 支援中文
matplotlib.rc("font", family="Microsoft JhengHei")
"""
臺北咖啡廳資訊 Web API:
https://cafenomad.tw/api/v1.2/cafes/taipei
"""
url = "https://cafenomad.tw/api/v1.2/cafes/taipei"
res = req.get(url)
data = res.json()
df = pd.DataFrame(data)
print(df)
print(df.describe())
print("-" * 50)

df["limited_time"] = df["limited_time"].replace("", "undefind")
print(df.value_counts("limited_time"))
print("-" * 50)


plt.bar(df["limited_time"].unique().tolist(), df.value_counts("limited_time"))
plt.xlabel("限制時間")
plt.ylabel("次數")
plt.show()

# 利用條件做篩選(兩種方法)
print(
    df.loc[df["address"].str.contains("臺北市大安區", case=False), :].reset_index(drop=True)
)
print(
    df[
        (df["address"].str.contains("臺北市大安區"))
        & (df["socket"] == "yes")
        & (df["limited_time"] == "no")
    ]
)
print(df[["latitude", "longitude"]])
print("-" * 50)

print(df.groupby("limited_time")["limited_time"].size())
print("-" * 50)

df["position"] = np.nan
df.loc[df["address"].str.contains("台北市"), "position"] = "台北"
df.loc[df["address"].str.contains("臺北市"), "position"] = "臺北"
print(df.value_counts("position"))
print(df.value_counts("position").values)


plt.pie(
    df.value_counts("position").values,
    labels=df.value_counts("position").index,
    explode=(0, 0.2),
    autopct="%1.2f%%",
)
plt.title("[數量] 臺北市 vs. 台北市")
plt.xlabel("地區")
plt.ylabel("數量")
plt.show()
