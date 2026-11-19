# 문제 3. names = np.array(["A", "B", "C", "D", "E"]), scores = np.array([70, 95, 82, 60, 88])에서 점수 상위 3명의 이름을 순서대로 출력하세요.

import numpy as np  # 넘파이 (관례적으로 np 라는 별명)
names = np.array(["A", "B", "C", "D", "E"])
scores = np.array([70, 95, 82, 60, 88])
top3 = np.argsort(scores)[::-1][:3]  # 점수 작은 순 위치 → [::-1] 뒤집기 → [:3] 앞 3개
print(names[top3])
