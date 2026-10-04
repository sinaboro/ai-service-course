import numpy as np

votes = np.array([3, 1, 2, 3, 3, 1, 2, 3])
values, counts = np.unique(votes, return_counts=True)
print("후보:", values)
print("득표:", counts)

sales = np.array([120, 80, 150, 200, 90])     # 일별 매출
print("누적 매출:", np.cumsum(sales))
print("전날 대비:", np.diff(sales))

print("100 이상인 날이 있나?", np.any(sales >= 100))
print("모두 50 이상인가?", np.all(sales >= 50))
