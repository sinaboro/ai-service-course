# 문제 2. 점수 [95, 72, 58, 84]가 있는 DataFrame에 70 이상이면 "Pass", 아니면 "Fail"인 result 열을 apply와 lambda로 만드세요.

import pandas as pd  # 판다스 (관례적으로 pd 라는 별명)
df = pd.DataFrame({"score": [95, 72, 58, 84]})
# apply 가 점수 하나씩 lambda 에 넣어요: 70 이상이면 "Pass", 아니면 "Fail"
df["result"] = df["score"].apply(lambda s: "Pass" if s >= 70 else "Fail")
print(df)
