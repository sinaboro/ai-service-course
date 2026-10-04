# 문제 2. 점수 [95, 72, 58, 84]가 있는 DataFrame에 70 이상이면 "Pass", 아니면 "Fail"인 result 열을 apply와 lambda로 만드세요.

import pandas as pd
df = pd.DataFrame({"score": [95, 72, 58, 84]})
df["result"] = df["score"].apply(lambda s: "Pass" if s >= 70 else "Fail")
print(df)
