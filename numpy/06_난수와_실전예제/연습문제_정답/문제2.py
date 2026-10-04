# 문제 2. seed=3으로 1 ~ 100 사이 정수 20개를 만들고, 50 이상인 값의 개수와 평균(소수 1자리)을 출력하세요.

import numpy as np
rng = np.random.default_rng(seed=3)
nums = rng.integers(1, 101, size=20)
big = nums[nums >= 50]
print(f"50 이상: {big.size}개, 평균 {big.mean():.1f}")
