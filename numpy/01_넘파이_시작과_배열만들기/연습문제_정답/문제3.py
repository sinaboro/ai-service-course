# 문제 3. 0부터 100까지를 같은 간격으로 나눈 값 5개를 만들고 정수로 바꿔 출력하세요.

import numpy as np
v = np.linspace(0, 100, 5)
print(v.astype(int))
