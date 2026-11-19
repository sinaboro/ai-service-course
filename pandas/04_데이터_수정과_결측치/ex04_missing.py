# ex04_missing.py : 결측치(빈 값 NaN) 처리: isna · dropna · fillna
import pandas as pd               # 판다스 (관례적으로 pd 라는 별명)
import numpy as np                # 넘파이 (관례적으로 np 라는 별명)

df = pd.DataFrame({
    "name": ["Kim", "Lee", "Park", "Choi"],
    "age": [25, np.nan, 31, 28],
    "city": ["Seoul", "Busan", None, "Seoul"],
})
print(df)
print(df.isna())                  # 빈 값이면 True
print(df.isna().sum())            # 열마다 빈 값 개수

print(df.dropna())                # 빈 값이 있는 행 삭제
print(df.fillna({"age": df["age"].mean(), "city": "Unknown"}))   # 열마다 다른 값으로 채우기
print(df["age"].fillna(0))
