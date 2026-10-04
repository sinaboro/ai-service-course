# 리스트 메서드
fruits = ["사과", "바나나"]
fruits.append("포도")           # 맨 뒤에 추가
print(fruits)
fruits.insert(1, "딸기")        # 1번 위치에 끼워 넣기
print(fruits)
fruits.remove("바나나")          # 값으로 삭제
print(fruits)
last = fruits.pop()             # 마지막 값을 꺼내며 삭제
print("꺼낸 값:", last, "/ 남은 리스트:", fruits)

nums = [5, 2, 9, 1, 7]
nums.sort()                     # 오름차순 정렬 (원본이 바뀜)
print(nums)
nums.sort(reverse=True)         # 내림차순
print(nums)
print(sorted([3, 1, 2]))        # sorted: 정렬된 "새" 리스트를 돌려줌
print(nums.index(9), nums.count(7))
