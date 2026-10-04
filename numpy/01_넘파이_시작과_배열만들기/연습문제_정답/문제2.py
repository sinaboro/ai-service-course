# 문제 2. 5로 채운 3행 4열 배열을 만들고 shape와 size를 출력하세요.

import numpy as np
m = np.full((3, 4), 5)
print(m)
print(m.shape, m.size)
