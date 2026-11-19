# ex02_clean.py : 읽은 데이터 점검하고 정리하기: 빈 값 · 중복 · 자료형 · 새 열
import pandas as pd                       # 판다스 (관례적으로 pd 라는 별명)

df = pd.read_csv("cafe_sales.csv")
df.info()

print(df.isna().sum())                    # qty 에 빈 값 1개
print(df[df["qty"].isna()])               # 어느 행인지 확인

df["qty"] = df["qty"].fillna(0).astype(int)   # 0 으로 채우고 정수로
df["amount"] = df["qty"] * df["price"]
print(df.tail(3))
print(df.duplicated().sum(), "개의 중복 행")
