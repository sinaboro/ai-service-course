# 문제 1. ex01_rule_vs_learning.py의 데이터에 (10, 92)를 추가하면 배운 규칙(기울기 · 절편)이 어떻게 바뀌는지 출력해 보세요.

import numpy as np
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 10])
y = np.array([52, 55, 61, 64, 70, 73, 78, 83, 92])
w, b = np.polyfit(x, y, deg=1)
print(f"점수 = {b:.2f} + {w:.2f} × 시간")
