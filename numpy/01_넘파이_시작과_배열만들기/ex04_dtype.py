import numpy as np

a = np.array([1, 2, 3])
b = np.array([1.5, 2.0, 3.7])
c = np.array([1, 2.5, 3])          # 정수 + 실수 → 모두 실수로
print(a.dtype, b.dtype, c.dtype)
print(c)

d = b.astype(int)                   # 실수 → 정수 (소수점 버림)
print(d, d.dtype)

e = np.array(["1", "2", "3"]).astype(int)   # 문자열 → 정수
print(e + 10)

f = np.array([1, 2, 3], dtype=float)        # 만들 때 자료형 지정
print(f)
