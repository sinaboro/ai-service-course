import numpy as np                # 관례적으로 np 라는 별명으로 가져와요

# 리스트로 모든 값에 10 을 곱하려면 반복문이 필요해요
prices = [1000, 2500, 4000]
result = []
for p in prices:
    result.append(p * 10)
print("리스트:", result)
print("리스트 * 2:", prices * 2)   # 리스트 * 2 는 "반복"이에요!

# NumPy 배열은 한 번에 계산 (벡터 연산)
arr = np.array([1000, 2500, 4000])
print("배열:", arr * 10)
print("배열 * 2:", arr * 2)
print(type(arr))
