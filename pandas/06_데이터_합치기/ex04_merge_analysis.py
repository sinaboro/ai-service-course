import pandas as pd

# 주문 기록: 어떤 상품(product_id)을 몇 개(qty) 샀는지
orders = pd.DataFrame({
    "order_id": [101, 102, 103, 104, 105, 106],
    "product_id": ["P1", "P2", "P1", "P3", "P2", "P1"],
    "qty": [2, 1, 3, 5, 2, 1],
})
# 상품 정보: 이름과 가격
products = pd.DataFrame({
    "product_id": ["P1", "P2", "P3"],
    "name": ["Mouse", "Keyboard", "Cable"],
    "price": [15000, 45000, 5000],
})

# 주문 표 기준(left)으로 상품 정보를 붙이기 → 주문마다 상품 이름 · 가격이 생겨요
df = pd.merge(orders, products, on="product_id", how="left")
# 주문 금액 = 수량 × 가격
df["amount"] = df["qty"] * df["price"]
print(df)

# 상품 이름별로 수량 · 금액 합계 (as_index=False: 묶은 열을 일반 열로 두기)
report = df.groupby("name", as_index=False).agg(qty=("qty", "sum"), amount=("amount", "sum"))
# 금액이 큰 순서로 정렬해서 출력
print(report.sort_values("amount", ascending=False))
