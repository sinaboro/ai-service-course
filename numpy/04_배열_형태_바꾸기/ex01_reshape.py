# ex01_reshape.py : reshape: 데이터는 그대로 두고 배열의 모양만 바꾸기 (-1 은 자동 계산)
import numpy as np            # 넘파이 (관례적으로 np 라는 별명)

a = np.arange(1, 13)          # 1 ~ 12 (12개)
print(a)

print(a.reshape(3, 4))        # 3행 4열
print(a.reshape(2, 6))        # 2행 6열
print(a.reshape(4, -1))       # -1: 나머지는 알아서 계산 → 4행 3열
print(a.reshape(-1, 2).shape) # 2열로, 행 수는 자동 → (6, 2)
print(a.reshape(2, 2, 3))     # 3차원: 2장 x 2행 x 3열
