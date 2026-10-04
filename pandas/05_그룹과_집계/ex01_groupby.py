import pandas as pd

df = pd.DataFrame({
    "date": ["10-01", "10-01", "10-02", "10-02", "10-03", "10-03", "10-03"],
    "store": ["Gangnam", "Hongdae", "Gangnam", "Hongdae", "Gangnam", "Hongdae", "Gangnam"],
    "menu": ["Coffee", "Latte", "Latte", "Coffee", "Coffee", "Tea", "Tea"],
    "qty": [10, 5, 8, 12, 7, 4, 6],
    "price": [4000, 4500, 4500, 4000, 4000, 3500, 3500],
})
df["sales"] = df["qty"] * df["price"]

print(df)

print(df.groupby("store")["sales"].sum())          # 매장별 매출 합계
print(df.groupby("menu")["qty"].mean().round(1))   # 메뉴별 평균 판매량
print(df.groupby("store").size())                  # 매장별 행 개수

print(df.groupby(["store", "menu"])["sales"].sum())   # 매장 x 메뉴

result = df.groupby("store", as_index=False)["sales"].sum()   # 결과를 일반 표로
print(result.sort_values("sales", ascending=False))
