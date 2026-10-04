import pandas as pd

# 날짜 · 매장 · 메뉴별 판매 기록 7건 (이 장의 예제가 함께 써요)
df = pd.DataFrame({
    "date": ["10-01", "10-01", "10-02", "10-02", "10-03", "10-03", "10-03"],
    "store": ["Gangnam", "Hongdae", "Gangnam", "Hongdae", "Gangnam", "Hongdae", "Gangnam"],
    "menu": ["Coffee", "Latte", "Latte", "Coffee", "Coffee", "Tea", "Tea"],
    "qty": [10, 5, 8, 12, 7, 4, 6],
    "price": [4000, 4500, 4500, 4000, 4000, 3500, 3500],
})
# 매출 = 수량 × 가격 (열끼리 곱하면 행마다 계산돼요)
df["sales"] = df["qty"] * df["price"]

# 매장별로 묶어서 매출의 합 · 평균 · 최대 · 건수를 한 번에
summary = df.groupby("store")["sales"].agg(["sum", "mean", "max", "count"])
print(summary)

# 열마다 다른 통계를 새 이름으로 (nunique: 서로 다른 값의 개수)
summary2 = df.groupby("menu").agg(
    total_qty=("qty", "sum"),          # 새 이름=(열, 통계)
    avg_price=("price", "mean"),
    days=("date", "nunique"),          # 팔린 날짜 수
)
print(summary2)
