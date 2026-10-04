import pandas as pd

df = pd.DataFrame({
    "date": ["10-01", "10-01", "10-02", "10-02", "10-03", "10-03", "10-03"],
    "store": ["Gangnam", "Hongdae", "Gangnam", "Hongdae", "Gangnam", "Hongdae", "Gangnam"],
    "menu": ["Coffee", "Latte", "Latte", "Coffee", "Coffee", "Tea", "Tea"],
    "qty": [10, 5, 8, 12, 7, 4, 6],
    "price": [4000, 4500, 4500, 4000, 4000, 3500, 3500],
})
df["sales"] = df["qty"] * df["price"]

pt = df.pivot_table(index="store", columns="menu", values="sales",
                    aggfunc="sum", fill_value=0)
print(pt)

pt2 = df.pivot_table(index="date", columns="store", values="qty",
                     aggfunc="sum", margins=True, margins_name="Total")   # 합계 행/열
print(pt2)
