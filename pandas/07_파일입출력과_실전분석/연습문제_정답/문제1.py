# 문제 1. cafe_sales.csv를 읽어 카테고리(category)별 총매출을 구하세요. (qty 빈 값은 0)

import pandas as pd
df = pd.read_csv("cafe_sales.csv")
df["qty"] = df["qty"].fillna(0).astype(int)
df["amount"] = df["qty"] * df["price"]
print(df.groupby("category")["amount"].sum())
