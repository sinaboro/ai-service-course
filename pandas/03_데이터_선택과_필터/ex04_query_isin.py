import pandas as pd

df = pd.DataFrame({
    "name": ["Kim", "Lee", "Park", "Choi", "Jung", "Kang"],
    "dept": ["Sales", "IT", "IT", "HR", "Sales", "IT"],
    "age": [23, 31, 27, 35, 29, 41],
    "salary": [3200, 4500, 3900, 4100, 3600, 5200],
})

print(df[df["dept"].isin(["HR", "Sales"])])        # 목록 중 하나에 해당
print(df[df["age"].between(27, 31)])               # 27 이상 31 이하
print(df[df["name"].str.contains("a")])            # 문자열 포함
print(df[~df["dept"].isin(["IT"])])                # ~ : 조건 뒤집기 (NOT)
print(df.query("age >= 30 and dept == 'IT'"))      # 문자열로 조건 쓰기
print(len(df[df["salary"] >= 4000]), "명")          # 조건에 맞는 행 수
