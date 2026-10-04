import numpy as np

# 배열 + 숫자 하나: 숫자가 모든 칸으로 "퍼져서" 계산
price = np.array([1000, 2500, 4000])
print(price * 1.1)               # 10% 인상

# 2차원 + 1차원: 1차원이 각 행마다 퍼짐
scores = np.array([[80, 90, 70],
                   [60, 75, 85]])
bonus = np.array([5, 0, 10])     # 과목별 보너스
print(scores + bonus)

# 열 방향으로 퍼지게 하려면 (2, 1) 모양
student_bonus = np.array([[1], [2]])
print(scores + student_bonus)
