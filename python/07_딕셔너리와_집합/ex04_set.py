# 집합(set): 중복 없음, 순서 없음
nums = {3, 1, 3, 2, 1}
print(nums)                      # 중복이 사라져요

# 리스트 → 집합으로 바꾸면 중복이 사라져요 / sorted 로 정렬된 리스트로
data = [5, 5, 2, 8, 2, 5]
unique = set(data)               # 리스트의 중복 제거
print(sorted(unique))

a = {"파이썬", "자바", "C"}
b = {"자바", "자바스크립트", "C"}
# & 교집합(둘 다 있는 것), | 합집합(어느 한쪽이라도), - 차집합(a 에만 있는 것)
print("교집합:", sorted(a & b))
print("합집합:", sorted(a | b))
print("차집합:", sorted(a - b))

# add: 추가 / discard: 삭제 (없는 값이어도 오류 없음)
a.add("Go")
a.discard("C")
print(sorted(a))
