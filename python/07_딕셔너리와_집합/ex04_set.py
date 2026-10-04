# 집합(set): 중복 없음, 순서 없음
nums = {3, 1, 3, 2, 1}
print(nums)                      # 중복이 사라져요

data = [5, 5, 2, 8, 2, 5]
unique = set(data)               # 리스트의 중복 제거
print(sorted(unique))

a = {"파이썬", "자바", "C"}
b = {"자바", "자바스크립트", "C"}
print("교집합:", sorted(a & b))
print("합집합:", sorted(a | b))
print("차집합:", sorted(a - b))

a.add("Go")
a.discard("C")
print(sorted(a))
