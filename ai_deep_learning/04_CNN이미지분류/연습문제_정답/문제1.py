# 문제 1. ex02_conv_pool_numbers.py의 필터를 [[1, -1], [1, -1]]로 바꾸면 결과의 부호가 어떻게 바뀌는지 출력해 보세요.

import numpy as np
img = np.array([[0, 0, 9, 9, 0, 0]] * 4, dtype=float)
k = np.array([[1, -1], [1, -1]], dtype=float)
out = np.array([[(img[i:i + 2, j:j + 2] * k).sum() for j in range(5)] for i in range(3)])
print(out)
