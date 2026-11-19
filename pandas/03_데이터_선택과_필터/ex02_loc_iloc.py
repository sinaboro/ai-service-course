# ex02_loc_iloc.py : loc(라벨 이름으로) 와 iloc(위치 번호로) 로 행과 열 고르기
import pandas as pd                # 판다스 (관례적으로 pd 라는 별명)

df = pd.DataFrame({
    "name": ["Kim", "Lee", "Park", "Choi", "Jung", "Kang"],
    "dept": ["Sales", "IT", "IT", "HR", "Sales", "IT"],
    "age": [23, 31, 27, 35, 29, 41],
    "salary": [3200, 4500, 3900, 4100, 3600, 5200],
})

df = df.set_index("name")          # 이름을 행 라벨로

print(df.loc["Lee"])               # 라벨로 행 하나
print(df.loc["Lee", "salary"])     # 행, 열 → 값 하나
print(df.loc[["Kim", "Park"], ["dept", "age"]])   # 여러 행, 여러 열
print(df.loc["Lee":"Choi"])        # 라벨 슬라이싱 (끝 포함)

print(df.iloc[0])                  # 위치로 첫 행
print(df.iloc[0:2, 1:3])           # 0~1 행, 1~2 열 (끝 미포함)
print(df.iloc[-1, -1])             # 마지막 행, 마지막 열
