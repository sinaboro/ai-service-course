# 문제 2. temps = np.array([18, 25, 31, 22, 35, 28, 15])에서 30도 이상인 날의 온도와 그 날의 수를 출력하세요.

import numpy as np  # 넘파이 (관례적으로 np 라는 별명)
temps = np.array([18, 25, 31, 22, 35, 28, 15])
hot = temps[temps >= 30]
print(hot)
print("폭염 일수:", len(hot))
