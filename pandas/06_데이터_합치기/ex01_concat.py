# ex01_concat.py : concat: 칸이 같은 표를 위아래로 · 좌우로 이어 붙이기
import pandas as pd                                  # 판다스 (관례적으로 pd 라는 별명)

jan = pd.DataFrame({"name": ["Kim", "Lee"], "sales": [100, 200]})
feb = pd.DataFrame({"name": ["Park", "Kim"], "sales": [150, 120]})

both = pd.concat([jan, feb])                         # 위아래로
print(both)

both2 = pd.concat([jan, feb], ignore_index=True)     # 인덱스 새로 매기기
print(both2)

jan["month"] = "Jan"
feb["month"] = "Feb"
print(pd.concat([jan, feb], ignore_index=True))      # 어느 달인지 표시해서 합치기

info = pd.DataFrame({"age": [23, 31]})
print(pd.concat([jan, info], axis=1))                # 좌우로 붙이기
