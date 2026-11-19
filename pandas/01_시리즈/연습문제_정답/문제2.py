# 문제 2. 위 Series에서 9000보 이상인 요일만 출력하세요.

import pandas as pd  # 판다스 (관례적으로 pd 라는 별명)
steps = pd.Series({"월": 8000, "화": 12000, "수": 6500, "목": 10000, "금": 9000})
print(steps[steps >= 9000])
