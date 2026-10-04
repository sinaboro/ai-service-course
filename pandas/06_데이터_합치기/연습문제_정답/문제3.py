# 문제 3. 문제 2의 결과로 부서별 직원 수를 구하세요.

import pandas as pd
emp = pd.DataFrame({"eid": [1, 2, 3], "name": ["Kim", "Lee", "Park"], "dept_id": [10, 20, 10]})
dept = pd.DataFrame({"dept_id": [10, 20], "dept": ["Sales", "IT"]})
df = pd.merge(emp, dept, on="dept_id", how="left")
print(df.groupby("dept").size())
