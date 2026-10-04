import numpy as np

# 행: 학생 3명, 열: 국어 영어 수학
scores = np.array([[80, 90, 70],
                   [60, 75, 85],
                   [95, 88, 92]])

print("전체 평균:", scores.mean().round(2))
print("과목별 평균 (axis=0):", scores.mean(axis=0).round(2))
print("학생별 평균 (axis=1):", scores.mean(axis=1).round(2))
print("과목별 최고점:", scores.max(axis=0))
print("학생별 총점  :", scores.sum(axis=1))
