# 문제 3. ["A", "B", "A", "C", "A", "B"]의 값별 개수를 value_counts()로 구하세요.

import pandas as pd
s = pd.Series(["A", "B", "A", "C", "A", "B"])
print(s.value_counts())
