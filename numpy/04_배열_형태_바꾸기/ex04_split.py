# ex04_split.py : 배열 나누기: split · hsplit
import numpy as np                       # 넘파이 (관례적으로 np 라는 별명)

a = np.arange(1, 10)
p1, p2, p3 = np.split(a, 3)              # 똑같이 3등분
print(p1, p2, p3)

front, back = np.split(a, [4])           # 4번 위치에서 자르기
print(front, back)

m = np.arange(1, 13).reshape(3, 4)
left, right = np.hsplit(m, 2)            # 열 방향으로 2등분
print(left)
print(right)
