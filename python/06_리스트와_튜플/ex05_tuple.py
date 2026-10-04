# 튜플: 소괄호 ( ), 만든 뒤에는 바꿀 수 없음
point = (3, 5)
print(point[0], point[1])

rgb = (255, 128, 0)
r, g, b = rgb            # 언패킹: 값을 나눠 담기
print(r, g, b)

# 함수가 여러 값을 돌려줄 때 튜플을 써요 (8장)
def min_max(nums):
    return min(nums), max(nums)

lo, hi = min_max([4, 9, 1, 7])
print("최소:", lo, "최대:", hi)

one = (5,)               # 원소가 하나면 쉼표 필요
print(type(one), type((5)))
