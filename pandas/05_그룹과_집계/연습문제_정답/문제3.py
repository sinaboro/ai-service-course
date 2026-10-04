# 문제 3. 행은 date, 열은 menu, 값은 qty 합계인 피벗 테이블을 만드세요. 빈 칸은 0으로 채우세요.

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

print(df.pivot_table(index="date", columns="menu", values="qty", aggfunc="sum", fill_value=0))
