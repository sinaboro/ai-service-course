from pathlib import Path
import pandas as pd

pd.set_option("display.unicode.east_asian_width", True)   # 한글 열 줄맞춤
DATA = Path(__file__).parent / "data"                      # 이 파일 옆의 data 폴더

# 주문 표 · 상품 표 읽기
orders = pd.read_csv(DATA / "orders.csv", parse_dates=["date"])
products = pd.read_csv(DATA / "products.csv")

# indicator=True: 각 행이 양쪽에 다 있었는지(both) 왼쪽에만 있었는지(left_only) 알려 주는 _merge 열 추가
df = orders.merge(products, on="product_id", how="left", indicator=True)
print(df[["order_id", "product_id", "name", "qty", "price", "_merge"]])

missing = df[df["_merge"] == "left_only"]          # 상품표에 없는 주문
print("상품 정보가 없는 주문:", missing["order_id"].tolist())

# 짝이 있는 주문만 골라 금액 계산 (copy: 원본과 분리)
ok = df[df["_merge"] == "both"].copy()
ok["amount"] = ok["qty"] * ok["price"]
# 분류 · 상품별 금액 합계 보고서
report = ok.groupby(["category", "name"], as_index=False)["amount"].sum()
print(report.sort_values("amount", ascending=False))

# output 폴더에 저장 (utf-8-sig: 엑셀에서 한글이 안 깨져요)
out_dir = Path(__file__).parent / "output"
out_dir.mkdir(exist_ok=True)
report.to_csv(out_dir / "category_report.csv", index=False, encoding="utf-8-sig")
print("저장:", (out_dir / "category_report.csv").name)
