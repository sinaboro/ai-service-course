import numpy as np

a = np.array([1, 2, 3, 4])              # 리스트 → 1차원 배열
b = np.array([[1, 2, 3], [4, 5, 6]])    # 리스트의 리스트 → 2차원 배열
print(a)
print(b)

print(np.arange(10))           # 0 ~ 9
print(np.arange(1, 11, 2))     # 1 ~ 10, 2씩 (range 와 같은 규칙)
print(np.zeros(5))             # 0 으로 채운 배열
print(np.ones((2, 3)))         # 1 로 채운 2행 3열
print(np.full((2, 2), 7))      # 7 로 채운 2행 2열
print(np.linspace(0, 1, 5))    # 0 ~ 1 을 똑같은 간격으로 5개 (끝 포함)
print(np.eye(3))               # 3x3 단위 행렬
