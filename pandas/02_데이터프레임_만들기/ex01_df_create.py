import pandas as pd

# 방법 1: 딕셔너리 (키 = 열 이름, 값 = 그 열의 데이터 리스트)
df = pd.DataFrame({
    "name": ["Kim", "Lee", "Park", "Choi"],
    "age": [23, 31, 27, 35],
    "city": ["Seoul", "Busan", "Seoul", "Daegu"],
})
# print(df): 왼쪽 0, 1, 2, 3 은 행 번호(인덱스), 위쪽은 열 이름
print(df)

# 방법 2: 딕셔너리들의 리스트 (한 행씩)
# 사전 하나 = 한 행. 키가 열 이름이 돼요
rows = [
    {"name": "Kim", "score": 90},
    {"name": "Lee", "score": 85},
]
print(pd.DataFrame(rows))

# 방법 3: 2차원 리스트 + 열 이름
# 리스트 안의 리스트 = 행들. 열 이름은 columns= 로 따로 정해 줘요
data = [[1, 2, 3], [4, 5, 6]]
print(pd.DataFrame(data, columns=["A", "B", "C"]))
