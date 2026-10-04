import numpy as np

a = np.array([[1, 2],
              [3, 4]])
b = np.array([[5, 6],
              [7, 8]])

print(np.concatenate([a, b]))           # 기본: 위아래로 (axis=0)
print(np.concatenate([a, b], axis=1))   # 좌우로 (axis=1)
print(np.vstack([a, b]))                # vertical: 세로로 쌓기
print(np.hstack([a, b]))                # horizontal: 가로로 붙이기

x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
print(np.vstack([x, y]))                # 1차원 두 개 → 2행
