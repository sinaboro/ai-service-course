# ex01_read_csv.py : CSV 파일 읽기: read_csv 와 자주 쓰는 옵션 (cafe_sales.csv 가 같은 폴더에 있어야 해요)
import pandas as pd                         # 판다스 (관례적으로 pd 라는 별명)

df = pd.read_csv("cafe_sales.csv")          # 같은 폴더의 CSV 읽기
print(df.head())
print(df.shape)

# 자주 쓰는 옵션
df2 = pd.read_csv("cafe_sales.csv", usecols=["date", "product", "qty"], nrows=3)
print(df2)
