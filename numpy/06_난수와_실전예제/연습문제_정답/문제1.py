# 문제 1. seed=1인 난수 생성기로 동전(0: 뒷면, 1: 앞면)을 1000번 던져 앞면 비율을 출력하세요.

import numpy as np
rng = np.random.default_rng(seed=1)
coins = rng.integers(0, 2, size=1000)
print(f"앞면 비율: {coins.mean():.1%}")
