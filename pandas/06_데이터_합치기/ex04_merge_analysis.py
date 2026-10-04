import pandas as pd

orders = pd.DataFrame({
    "order_id": [101, 102, 103, 104, 105, 106],
    "product_id": ["P1", "P2", "P1", "P3", "P2", "P1"],
    "qty": [2, 1, 3, 5, 2, 1],
})
products = pd.DataFrame({
    "product_id": ["P1", "P2", "P3"],
    "name": ["Mouse", "Keyboard", "Cable"],
    "price": [15000, 45000, 5000],
})

df = pd.merge(orders, products, on="product_id", how="left")
df["amount"] = df["qty"] * df["price"]
print(df)

report = df.groupby("name", as_index=False).agg(qty=("qty", "sum"), amount=("amount", "sum"))
print(report.sort_values("amount", ascending=False))
