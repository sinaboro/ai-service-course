import numpy as np

# 투표 결과: 후보 번호 8표
votes = np.array([3, 1, 2, 3, 3, 1, 2, 3])
# unique: 중복 없는 값들 + return_counts=True 면 각 값의 개수도
values, counts = np.unique(votes, return_counts=True)
print("후보:", values)
print("득표:", counts)

sales = np.array([120, 80, 150, 200, 90])     # 일별 매출
# cumsum: 앞에서부터 차례로 더한 누적 합 / diff: 바로 앞 값과의 차이
print("누적 매출:", np.cumsum(sales))
print("전날 대비:", np.diff(sales))

# any: 하나라도 참이면 True / all: 모두 참이어야 True
print("100 이상인 날이 있나?", np.any(sales >= 100))
print("모두 50 이상인가?", np.all(sales >= 50))
