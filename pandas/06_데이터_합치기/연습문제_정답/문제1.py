# 문제 1. 두 표 a = {"city": ["Seoul", "Busan"], "pop": [940, 330]}, b = {"city": ["Daegu"], "pop": [236]}를 위아래로 합치고 인덱스를 새로 매기세요.

import pandas as pd
a = pd.DataFrame({"city": ["Seoul", "Busan"], "pop": [940, 330]})
b = pd.DataFrame({"city": ["Daegu"], "pop": [236]})
print(pd.concat([a, b], ignore_index=True))
