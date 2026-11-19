# 문제 1. ex02_conv_pool_numbers.py의 필터를 [[1, -1], [1, -1]]로 바꾸면 결과의 부호가 어떻게 바뀌는지 출력해 보세요.

import numpy as np  # 넘파이 (관례적으로 np 라는 별명)
img = np.array([[0, 0, 9, 9, 0, 0]] * 4, dtype=float)
k = np.array([[1, -1], [1, -1]], dtype=float)
# 이중 리스트 컴프리헨션 = 이중 for 문을 한 줄로 쓴 것:
# for i in range(3):        # 결과의 행 (위→아래로 3칸)
#     for j in range(5):    # 결과의 열 (왼→오른쪽 5칸)
#         img[i:i+2, j:j+2] (2×2 조각) 과 필터 k 를 곱해 모두 더한 값(sum) 하나
out = np.array([[(img[i:i + 2, j:j + 2] * k).sum() for j in range(5)] for i in range(3)])
print(out)
