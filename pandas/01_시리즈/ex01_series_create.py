import pandas as pd                 # 관례적으로 pd 라는 별명

s1 = pd.Series([90, 75, 88])        # 리스트로 → 인덱스는 0, 1, 2 자동
print(s1)

s2 = pd.Series([90, 75, 88], index=["kim", "lee", "park"])   # 인덱스(라벨) 지정
print(s2)

s3 = pd.Series({"apple": 1000, "banana": 2500, "grape": 4000})   # 딕셔너리로
print(s3)

print(s3.index)      # 라벨들
print(s3.values)     # 값들 (NumPy 배열)
print(s3.dtype, len(s3))
