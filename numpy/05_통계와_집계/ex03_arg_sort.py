import numpy as np

names = np.array(["홍길동", "이순신", "유관순", "강감찬"])
scores = np.array([78, 92, 85, 64])

print("최고점 위치:", scores.argmax())
print("1등:", names[scores.argmax()])
print("꼴찌:", names[scores.argmin()])

print(np.sort(scores))                 # 오름차순 정렬
print(np.sort(scores)[::-1])           # 내림차순

order = np.argsort(scores)[::-1]       # 점수 높은 순서의 "위치"
print("순서(위치):", order)
print("등수대로 이름:", names[order])
