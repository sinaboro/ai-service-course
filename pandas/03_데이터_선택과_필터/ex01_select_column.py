import pandas as pd

df = pd.DataFrame({
    "name": ["Kim", "Lee", "Park", "Choi", "Jung", "Kang"],
    "dept": ["Sales", "IT", "IT", "HR", "Sales", "IT"],
    "age": [23, 31, 27, 35, 29, 41],
    "salary": [3200, 4500, 3900, 4100, 3600, 5200],
})

print(df["name"])                 # 열 하나 → Series
print(type(df["name"]))
print(df[["name", "salary"]])     # 여러 열 → DataFrame (대괄호 두 겹)
print(df.age.mean())              # 점(.)으로도 접근 가능 (열 이름이 간단할 때)
