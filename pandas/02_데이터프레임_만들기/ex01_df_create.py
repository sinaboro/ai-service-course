import pandas as pd

# 방법 1: 딕셔너리 (키 = 열 이름, 값 = 그 열의 데이터 리스트)
df = pd.DataFrame({
    "name": ["Kim", "Lee", "Park", "Choi"],
    "age": [23, 31, 27, 35],
    "city": ["Seoul", "Busan", "Seoul", "Daegu"],
})
print(df)

# 방법 2: 딕셔너리들의 리스트 (한 행씩)
rows = [
    {"name": "Kim", "score": 90},
    {"name": "Lee", "score": 85},
]
print(pd.DataFrame(rows))

# 방법 3: 2차원 리스트 + 열 이름
data = [[1, 2, 3], [4, 5, 6]]
print(pd.DataFrame(data, columns=["A", "B", "C"]))
