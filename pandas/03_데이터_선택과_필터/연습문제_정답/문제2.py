# 문제 2. 나이가 30 미만이면서 연봉이 3500 이상인 직원의 이름 목록을 출력하세요.

import pandas as pd

df = pd.DataFrame({
    "name": ["Kim", "Lee", "Park", "Choi", "Jung", "Kang"],
    "dept": ["Sales", "IT", "IT", "HR", "Sales", "IT"],
    "age": [23, 31, 27, 35, 29, 41],
    "salary": [3200, 4500, 3900, 4100, 3600, 5200],
})

result = df[(df["age"] < 30) & (df["salary"] >= 3500)]
print(result["name"].tolist())
