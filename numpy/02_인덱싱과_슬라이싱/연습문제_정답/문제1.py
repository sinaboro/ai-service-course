# 문제 1. m = np.arange(1, 17).reshape(4, 4)에서 가운데 2×2 부분(6, 7, 10, 11)을 꺼내세요.

import numpy as np  # 넘파이 (관례적으로 np 라는 별명)
m = np.arange(1, 17).reshape(4, 4)
print(m[1:3, 1:3])
