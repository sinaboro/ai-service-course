# lambda: 이름 없는 한 줄 함수
square = lambda x: x ** 2
print(square(5))

students = [("홍길동", 85), ("이순신", 92), ("유관순", 78)]
by_score = sorted(students, key=lambda s: s[1], reverse=True)   # 점수 기준 정렬
print(by_score)

nums = [1, 2, 3, 4, 5, 6]
print(list(map(lambda x: x * 10, nums)))          # 모든 원소에 적용
print(list(filter(lambda x: x % 2 == 0, nums)))   # 조건에 맞는 것만
