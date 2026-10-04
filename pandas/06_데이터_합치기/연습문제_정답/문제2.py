# 문제 2. 직원 emp = {"eid": [1, 2, 3], "name": ["Kim", "Lee", "Park"], "dept_id": [10, 20, 10]}와 부서 dept = {"dept_id": [10, 20], "dept": ["Sales", "IT"]}를 연결해 이름과 부서명을 출력하세요.

import pandas as pd
emp = pd.DataFrame({"eid": [1, 2, 3], "name": ["Kim", "Lee", "Park"], "dept_id": [10, 20, 10]})
dept = pd.DataFrame({"dept_id": [10, 20], "dept": ["Sales", "IT"]})
df = pd.merge(emp, dept, on="dept_id", how="left")
print(df[["name", "dept"]])
