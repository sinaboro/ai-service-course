import numpy as np

a = np.array([1, 4, 9, 16])
print(np.sqrt(a))                  # 제곱근
print(np.square(a))                # 제곱

b = np.array([-2.567, 3.141, -0.5])
print(np.abs(b))                   # 절댓값
print(np.round(b, 1))              # 소수 1자리 반올림
print(np.floor(b), np.ceil(b))     # 내림, 올림

c = np.array([3, 8, 1])
d = np.array([5, 2, 7])
print(np.maximum(c, d))            # 위치마다 큰 값
