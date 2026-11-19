# 문제 1. 상품 가격 [12000, 8500, 30000]에 15% 할인을 적용한 가격을 정수로 출력하세요.

import numpy as np  # 넘파이 (관례적으로 np 라는 별명)
price = np.array([12000, 8500, 30000])
print((price * 0.85).astype(int))
