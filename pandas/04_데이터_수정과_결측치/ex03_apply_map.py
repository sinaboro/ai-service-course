import pandas as pd
import numpy as np

# 이름 · 점수 · 성별 3명짜리 표
df = pd.DataFrame({
    "name": ["kim", "lee", "park"],
    "score": [92, 67, 81],
    "gender": ["M", "F", "M"],
})

df["name"] = df["name"].str.upper()                       # 문자열 메서드
df["gender_kr"] = df["gender"].map({"M": "남", "F": "여"})  # 값 → 다른 값으로 대응

# 점수 하나를 받아 학점을 돌려주는 함수 (apply 로 모든 행에 적용할 거예요)
def grade(s):
    if s >= 90:
        return "A"
    elif s >= 80:
        return "B"
    return "C"

df["grade"] = df["score"].apply(grade)                    # 함수를 모든 값에 적용
# lambda: 이름 없는 짧은 함수 → 점수에 10% 가산점
df["bonus"] = df["score"].apply(lambda s: s * 1.1).round(1)
# np.where(조건, 참일 때, 거짓일 때): 70점 이상이면 "통과"
df["result"] = np.where(df["score"] >= 70, "통과", "재시험")
print(df)
