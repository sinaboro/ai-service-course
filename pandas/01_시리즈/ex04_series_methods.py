import pandas as pd

score = pd.Series([88, 92, 75, 92, 60, 75, 75],
                  index=["a", "b", "c", "d", "e", "f", "g"])

print("합계:", score.sum(), "평균:", round(score.mean(), 2))
print("최고:", score.max(), "최고인 라벨:", score.idxmax())
print(score.describe())               # 요약 통계 한 번에

print(score.sort_values(ascending=False).head(3))   # 높은 순 3개
print(score.value_counts())           # 값별 개수
print(score.unique())                 # 중복 없는 값
