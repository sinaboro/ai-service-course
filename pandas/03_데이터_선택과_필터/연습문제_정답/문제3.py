# 문제 3. IT 부서 직원의 평균 연봉을 구하세요.

import pandas as pd  # 판다스 (관례적으로 pd 라는 별명)

df = pd.DataFrame({
    "name": ["Kim", "Lee", "Park", "Choi", "Jung", "Kang"],
    "dept": ["Sales", "IT", "IT", "HR", "Sales", "IT"],
    "age": [23, 31, 27, 35, 29, 41],
    "salary": [3200, 4500, 3900, 4100, 3600, 5200],
})

avg = df[df["dept"] == "IT"]["salary"].mean()
print(f"IT 평균 연봉: {avg:.2f}")
