# 문제 1. df = pd.DataFrame({"item": ["A", "B", "C"], "price": [1000, 2500, 1800], "qty": [3, 1, 4]})에 amount(price × qty) 열을 추가하고 amount가 큰 순으로 정렬하세요.

import pandas as pd
df = pd.DataFrame({"item": ["A", "B", "C"], "price": [1000, 2500, 1800], "qty": [3, 1, 4]})
df["amount"] = df["price"] * df["qty"]
print(df.sort_values("amount", ascending=False))
