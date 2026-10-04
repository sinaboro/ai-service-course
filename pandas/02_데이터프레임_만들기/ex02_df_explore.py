import pandas as pd

df = pd.DataFrame({
    "name": ["Kim", "Lee", "Park", "Choi", "Jung", "Kang"],
    "dept": ["Sales", "IT", "IT", "HR", "Sales", "IT"],
    "age": [23, 31, 27, 35, 29, 41],
    "salary": [3200, 4500, 3900, 4100, 3600, 5200],
})

print(df.head(3))          # 앞 3행 (기본 5행)
print(df.tail(2))          # 뒤 2행
print(df.shape)            # (행 수, 열 수)
print(df.columns.tolist()) # 열 이름들
print(df.dtypes)           # 열마다 자료형
df.info()                  # 요약 정보 (print 없이 바로 출력)
print(df.describe())       # 숫자 열의 요약 통계
