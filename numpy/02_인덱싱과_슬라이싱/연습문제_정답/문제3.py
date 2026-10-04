# 문제 3. a = np.arange(1, 11)에서 짝수는 그대로, 홀수는 0으로 바꾼 배열을 np.where로 만드세요.

import numpy as np
a = np.arange(1, 11)
print(np.where(a % 2 == 0, a, 0))
