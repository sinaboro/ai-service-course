# 문제 2. 3명의 국·영·수 점수 [[70, 80, 90], [60, 65, 70], [88, 92, 95]]에 과목별 가중치 [1.0, 1.2, 1.5]를 곱한 배열을 소수 1자리로 출력하세요.

import numpy as np
scores = np.array([[70, 80, 90], [60, 65, 70], [88, 92, 95]])
weight = np.array([1.0, 1.2, 1.5])
print(np.round(scores * weight, 1))
