# 문제 2. Americano의 날짜별 판매 수량 합계를 구하세요.

import pandas as pd
df = pd.read_csv("cafe_sales.csv")
ame = df[df["product"] == "Americano"]
print(ame.groupby("date")["qty"].sum().astype(int))
