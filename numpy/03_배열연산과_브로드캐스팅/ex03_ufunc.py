# ex03_ufunc.py : 유니버설 함수: np.sqrt · np.round · np.floor 등을 배열 전체에 한 번에
import numpy as np                 # 넘파이 (관례적으로 np 라는 별명)

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
