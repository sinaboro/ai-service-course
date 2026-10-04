import pandas as pd

df = pd.DataFrame({
    "date": ["10-01", "10-01", "10-02", "10-02", "10-03", "10-03", "10-03"],
    "store": ["Gangnam", "Hongdae", "Gangnam", "Hongdae", "Gangnam", "Hongdae", "Gangnam"],
    "menu": ["Coffee", "Latte", "Latte", "Coffee", "Coffee", "Tea", "Tea"],
    "qty": [10, 5, 8, 12, 7, 4, 6],
    "price": [4000, 4500, 4500, 4000, 4000, 3500, 3500],
})
df["sales"] = df["qty"] * df["price"]

summary = df.groupby("store")["sales"].agg(["sum", "mean", "max", "count"])
print(summary)

summary2 = df.groupby("menu").agg(
    total_qty=("qty", "sum"),          # 새 이름=(열, 통계)
    avg_price=("price", "mean"),
    days=("date", "nunique"),          # 팔린 날짜 수
)
print(summary2)
