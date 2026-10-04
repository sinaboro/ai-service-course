# 문제 3. {"temp": [21.5, None, 23.0, None, 22.5]}에서 빈 값의 개수를 세고, 빈 값을 평균으로 채운 결과를 출력하세요.

import pandas as pd
df = pd.DataFrame({"temp": [21.5, None, 23.0, None, 22.5]})
print("빈 값:", df["temp"].isna().sum())
print(df["temp"].fillna(df["temp"].mean()).round(1))
