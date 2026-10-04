import pandas as pd

df = pd.read_csv("cafe_sales.csv")          # 같은 폴더의 CSV 읽기
print(df.head())
print(df.shape)

# 자주 쓰는 옵션
df2 = pd.read_csv("cafe_sales.csv", usecols=["date", "product", "qty"], nrows=3)
print(df2)
