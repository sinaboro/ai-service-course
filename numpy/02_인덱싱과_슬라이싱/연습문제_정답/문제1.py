# 문제 1. m = np.arange(1, 17).reshape(4, 4)에서 가운데 2×2 부분(6, 7, 10, 11)을 꺼내세요.

import numpy as np
m = np.arange(1, 17).reshape(4, 4)
print(m[1:3, 1:3])
