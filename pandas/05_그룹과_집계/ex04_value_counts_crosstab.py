import pandas as pd

df = pd.DataFrame({
    "date": ["10-01", "10-01", "10-02", "10-02", "10-03", "10-03", "10-03"],
    "store": ["Gangnam", "Hongdae", "Gangnam", "Hongdae", "Gangnam", "Hongdae", "Gangnam"],
    "menu": ["Coffee", "Latte", "Latte", "Coffee", "Coffee", "Tea", "Tea"],
    "qty": [10, 5, 8, 12, 7, 4, 6],
    "price": [4000, 4500, 4500, 4000, 4000, 3500, 3500],
})
df["sales"] = df["qty"] * df["price"]

print(df["menu"].value_counts())                       # 메뉴별 주문 건수
print(df["menu"].value_counts(normalize=True).round(2))   # 비율
print(pd.crosstab(df["store"], df["menu"]))            # 매장 x 메뉴 건수 표
