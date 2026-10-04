# 문제 3. 수량 [3, 0, 2, 5]과 단가 [1200, 3000, 2500, 800]으로 총 결제 금액을 @로 구하세요.

import numpy as np
qty = np.array([3, 0, 2, 5])
price = np.array([1200, 3000, 2500, 800])
print("총액:", qty @ price)
