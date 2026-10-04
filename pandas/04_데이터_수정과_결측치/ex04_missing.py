import pandas as pd
import numpy as np

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
