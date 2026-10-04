import pandas as pd

df = pd.DataFrame({
    "name": ["Kim", "Lee", "Park", "Choi", "Jung", "Kang"],
    "dept": ["Sales", "IT", "IT", "HR", "Sales", "IT"],
    "age": [23, 31, 27, 35, 29, 41],
    "salary": [3200, 4500, 3900, 4100, 3600, 5200],
})

print(df["age"] >= 30)                    # 행마다 True/False
print(df[df["age"] >= 30])                # True 인 행만

it = df[df["dept"] == "IT"]
print(it)

# 여러 조건: & (그리고), | (또는) — 각 조건을 괄호로!
print(df[(df["dept"] == "IT") & (df["salary"] >= 4000)])
print(df[(df["age"] < 25) | (df["age"] > 40)])

# 조건 + 특정 열만
print(df.loc[df["salary"] > 4000, ["name", "salary"]])
