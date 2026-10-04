import pandas as pd
import numpy as np

df = pd.DataFrame({
    "name": ["kim", "lee", "park"],
    "score": [92, 67, 81],
    "gender": ["M", "F", "M"],
})

df["name"] = df["name"].str.upper()                       # 문자열 메서드
df["gender_kr"] = df["gender"].map({"M": "남", "F": "여"})  # 값 → 다른 값으로 대응

def grade(s):
    if s >= 90:
        return "A"
    elif s >= 80:
        return "B"
    return "C"

df["grade"] = df["score"].apply(grade)                    # 함수를 모든 값에 적용
df["bonus"] = df["score"].apply(lambda s: s * 1.1).round(1)
df["result"] = np.where(df["score"] >= 70, "통과", "재시험")
print(df)
