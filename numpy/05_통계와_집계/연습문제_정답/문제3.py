# 문제 3. names = np.array(["A", "B", "C", "D", "E"]), scores = np.array([70, 95, 82, 60, 88])에서 점수 상위 3명의 이름을 순서대로 출력하세요.

import numpy as np
names = np.array(["A", "B", "C", "D", "E"])
scores = np.array([70, 95, 82, 60, 88])
top3 = np.argsort(scores)[::-1][:3]
print(names[top3])
