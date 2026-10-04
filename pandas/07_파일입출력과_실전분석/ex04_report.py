import pandas as pd

# 1) 읽기 + 정리
df = pd.read_csv("cafe_sales.csv", parse_dates=["date"])
df["qty"] = df["qty"].fillna(0).astype(int)
df["amount"] = df["qty"] * df["price"]

# 2) 전체 요약
print(f"기간: {df['date'].min().date()} ~ {df['date'].max().date()}")
print(f"총 매출: {df['amount'].sum():,}원 / 판매 수량: {df['qty'].sum()}개")

# 3) 매장별
by_store = df.groupby("store", as_index=False)["amount"].sum().sort_values("amount", ascending=False)
by_store["share(%)"] = (by_store["amount"] / by_store["amount"].sum() * 100).round(1)
print(by_store)

# 4) 상품별 TOP 3
top = df.groupby("product")["qty"].sum().nlargest(3)
print(top)

# 5) 날짜 x 카테고리 피벗
pt = df.pivot_table(index=df["date"].dt.strftime("%m-%d"), columns="category",
                    values="amount", aggfunc="sum", fill_value=0)
print(pt)

# 6) 저장
by_store.to_csv("report_by_store.csv", index=False, encoding="utf-8-sig")
print("report_by_store.csv 저장 완료")
