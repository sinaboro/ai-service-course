# 문제 1. 1 ~ 24를 4행 6열로 만든 뒤, 전치해서 shape를 출력하세요.

import numpy as np
m = np.arange(1, 25).reshape(4, 6)
print(m.T.shape)
