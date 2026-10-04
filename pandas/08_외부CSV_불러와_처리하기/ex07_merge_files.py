from pathlib import Path
import pandas as pd

pd.set_option("display.unicode.east_asian_width", True)   # 한글 열 줄맞춤
DATA = Path(__file__).parent / "data"                      # 이 파일 옆의 data 폴더

orders = pd.read_csv(DATA / "orders.csv", parse_dates=["date"])
products = pd.read_csv(DATA / "products.csv")

df = orders.merge(products, on="product_id", how="left", indicator=True)
print(df[["order_id", "product_id", "name", "qty", "price", "_merge"]])

missing = df[df["_merge"] == "left_only"]          # 상품표에 없는 주문
print("상품 정보가 없는 주문:", missing["order_id"].tolist())

ok = df[df["_merge"] == "both"].copy()
ok["amount"] = ok["qty"] * ok["price"]
report = ok.groupby(["category", "name"], as_index=False)["amount"].sum()
print(report.sort_values("amount", ascending=False))

out_dir = Path(__file__).parent / "output"
out_dir.mkdir(exist_ok=True)
report.to_csv(out_dir / "category_report.csv", index=False, encoding="utf-8-sig")
print("저장:", (out_dir / "category_report.csv").name)
