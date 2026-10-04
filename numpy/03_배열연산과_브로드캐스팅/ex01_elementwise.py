import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])

print(a + b)       # 같은 위치끼리 더하기
print(b - a)
print(a * b)       # 같은 위치끼리 곱하기
print(b / a)
print(a ** 2)
print(b % 3)
print(a > 2)       # 비교도 원소별
