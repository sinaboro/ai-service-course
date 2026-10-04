import numpy as np

scores = np.array([85, 42, 77, 93, 58, 61])

print(scores >= 60)               # 각 값마다 True/False
print(scores[scores >= 60])       # True 인 값만 꺼내기
print((scores >= 60).sum())       # True 의 개수 = 합격 인원

# 여러 조건: & (그리고), | (또는) — 괄호 필수!
print(scores[(scores >= 60) & (scores < 90)])
print(scores[(scores < 50) | (scores > 90)])

# 조건에 맞는 값만 바꾸기
scores[scores < 60] = 0
print(scores)

# np.where: 조건에 따라 다른 값
s = np.array([85, 42, 77])
print(np.where(s >= 60, "합격", "불합격"))
