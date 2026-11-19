# ex02_transpose_flatten.py : .T(행 ↔ 열 바꾸기) · flatten / ravel(1차원으로 펼치기)
import numpy as np         # 넘파이 (관례적으로 np 라는 별명)

m = np.array([[1, 2, 3],
              [4, 5, 6]])
print(m.shape)

print(m.T)                 # 전치: 행 ↔ 열
print(m.T.shape)

print(m.flatten())         # 1차원으로 펼치기 (복사본)
print(m.ravel())           # 1차원으로 펼치기 (가능하면 뷰)

v = np.array([1, 2, 3])
print(v.reshape(-1, 1))    # 1차원 → 세로 한 줄(3행 1열)
