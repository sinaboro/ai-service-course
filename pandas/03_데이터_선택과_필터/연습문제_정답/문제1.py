# 문제 1. 직원 데이터에서 Sales 부서 직원의 이름과 연봉만 출력하세요.

import pandas as pd

df = pd.DataFrame({
    "name": ["Kim", "Lee", "Park", "Choi", "Jung", "Kang"],
    "dept": ["Sales", "IT", "IT", "HR", "Sales", "IT"],
    "age": [23, 31, 27, 35, 29, 41],
    "salary": [3200, 4500, 3900, 4100, 3600, 5200],
})

print(df.loc[df["dept"] == "Sales", ["name", "salary"]])
