# 문제 3. np.arange(10)을 앞 3개, 가운데 4개, 뒤 3개로 나누세요.

import numpy as np
a = np.arange(10)
x, y, z = np.split(a, [3, 7])
print(x, y, z)
