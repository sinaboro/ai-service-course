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

# 피벗: 행 = 매장, 열 = 메뉴, 칸 = 매출 합계 (팔린 적 없는 칸은 0)
pt = df.pivot_table(index="store", columns="menu", values="sales",
                    aggfunc="sum", fill_value=0)
print(pt)

# 행 = 날짜, 열 = 매장, 칸 = 수량 합계 + margins=True 로 합계 행 · 열 추가
pt2 = df.pivot_table(index="date", columns="store", values="qty",
                     aggfunc="sum", margins=True, margins_name="Total")   # 합계 행/열
print(pt2)
