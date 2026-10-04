import numpy as np

a = np.arange(10, 100, 10)    # [10 20 30 40 50 60 70 80 90]
print(a)
print(a[0], a[-1])            # 첫 값, 마지막 값
print(a[2:5])                 # 2 ~ 4 번 (5는 미포함)
print(a[:3], a[6:])
print(a[::2])                 # 2칸씩
print(a[::-1])                # 거꾸로

a[0] = 999                    # 값 바꾸기
a[1:3] = 0                    # 여러 칸을 한 번에
print(a)
