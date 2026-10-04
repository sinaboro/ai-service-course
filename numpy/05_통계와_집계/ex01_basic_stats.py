import numpy as np

scores = np.array([85, 92, 78, 64, 95, 70])

print("합계  :", scores.sum())
print("평균  :", scores.mean())
print("최댓값:", scores.max())
print("최솟값:", scores.min())
print("중앙값:", np.median(scores))
print("표준편차:", round(scores.std(), 2))
print("개수  :", scores.size)

# 함수 방식과 메서드 방식은 같아요
print(np.sum(scores) == scores.sum())
