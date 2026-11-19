# ex01_elementwise.py : 원소별 연산: 같은 모양 배열끼리 같은 위치의 값끼리 계산
import numpy as np  # 넘파이 (관례적으로 np 라는 별명)

a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])

print(a + b)       # 같은 위치끼리 더하기
print(b - a)
print(a * b)       # 같은 위치끼리 곱하기
print(b / a)
print(a ** 2)
print(b % 3)
print(a > 2)       # 비교도 원소별
