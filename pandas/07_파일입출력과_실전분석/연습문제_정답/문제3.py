# 문제 3. 매장(store)별 총매출을 구해 store_total.csv로 저장한 뒤, 다시 읽어서 출력하세요.

import pandas as pd
df = pd.read_csv("cafe_sales.csv")
df["qty"] = df["qty"].fillna(0).astype(int)
df["amount"] = df["qty"] * df["price"]
total = df.groupby("store", as_index=False)["amount"].sum()
total.to_csv("store_total.csv", index=False, encoding="utf-8-sig")
print(pd.read_csv("store_total.csv"))
