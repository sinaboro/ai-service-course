import pandas as pd

price = pd.Series({"apple": 1000, "banana": 2500, "grape": 4000})
qty = pd.Series({"apple": 3, "banana": 2, "grape": 1})

print(price * 1.1)               # 모든 값에 (브로드캐스팅)
print(price * qty)               # 같은 라벨끼리 곱하기
print((price * qty).sum())       # 총액

print(price > 2000)              # 조건 → True/False Series
print(price[price > 2000])       # True 인 것만 (불리언 인덱싱)

a = pd.Series({"x": 1, "y": 2})
b = pd.Series({"y": 10, "z": 20})
print(a + b)                     # 라벨이 한쪽에만 있으면 NaN (결측치)
