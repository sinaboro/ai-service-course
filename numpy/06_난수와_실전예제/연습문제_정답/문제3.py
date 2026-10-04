# 문제 3. ["철수", "영희", "민수", "지영", "현우"] 중에서 seed=10으로 중복 없이 2명을 뽑아 출력하세요.

import numpy as np
rng = np.random.default_rng(seed=10)
people = np.array(["철수", "영희", "민수", "지영", "현우"])
print("당첨:", rng.choice(people, size=2, replace=False))
