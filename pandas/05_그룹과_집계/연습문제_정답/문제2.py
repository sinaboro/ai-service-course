# 문제 2. 날짜별 매출 합계와 주문 건수를 agg로 구하세요. 열 이름은 total, orders로 하세요.

import pandas as pd

df = pd.DataFrame({
    "date": ["10-01", "10-01", "10-02", "10-02", "10-03", "10-03", "10-03"],
    "store": ["Gangnam", "Hongdae", "Gangnam", "Hongdae", "Gangnam", "Hongdae", "Gangnam"],
    "menu": ["Coffee", "Latte", "Latte", "Coffee", "Coffee", "Tea", "Tea"],
    "qty": [10, 5, 8, 12, 7, 4, 6],
    "price": [4000, 4500, 4500, 4000, 4000, 3500, 3500],
})
df["sales"] = df["qty"] * df["price"]

print(df.groupby("date").agg(total=("sales", "sum"), orders=("sales", "count")))
