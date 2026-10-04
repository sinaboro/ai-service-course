import numpy as np

A = np.array([[1, 2],
              [3, 4]])
B = np.array([[5, 6],
              [7, 8]])

print("원소별 곱 A * B")
print(A * B)
print("행렬 곱 A @ B")
print(A @ B)
print(np.dot(A, B))                # @ 와 같아요

# 활용: 수량 x 단가 = 총액
qty = np.array([2, 1, 3])          # 상품별 수량
price = np.array([1500, 4000, 800])
print("총액:", qty @ price)        # 2*1500 + 1*4000 + 3*800
