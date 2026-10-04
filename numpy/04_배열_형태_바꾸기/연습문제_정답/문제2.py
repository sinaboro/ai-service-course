# 문제 2. a = np.array([1, 2, 3]), b = np.array([4, 5, 6]), c = np.array([7, 8, 9])를 쌓아 3×3 배열을 만들고 1차원으로 펼쳐 출력하세요.

import numpy as np
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = np.array([7, 8, 9])
m = np.vstack([a, b, c])
print(m)
print(m.flatten())
