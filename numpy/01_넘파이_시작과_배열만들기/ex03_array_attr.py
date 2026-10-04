import numpy as np

m = np.array([[10, 20, 30],
              [40, 50, 60]])

print("shape:", m.shape)     # (행, 열)
print("ndim :", m.ndim)      # 차원 수
print("size :", m.size)      # 전체 원소 개수
print("dtype:", m.dtype)     # 원소의 자료형
print("len  :", len(m))      # 첫 번째 축(행)의 길이

v = np.arange(5)
print(v.shape, v.ndim)       # 1차원은 (5,) 처럼 쉼표가 붙어요
