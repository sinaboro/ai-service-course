# 리스트: 대괄호 [ ] 안에 쉼표로 구분
scores = [90, 75, 88, 62, 95]
names = ["홍길동", "이순신", "유관순"]
mixed = [1, "two", 3.0, True]      # 여러 자료형을 섞을 수도 있어요
empty = []

print(scores)
print(len(scores))      # 개수
print(scores[0])        # 첫 번째 (인덱스 0)
print(scores[-1])       # 마지막
print(scores[1:3])      # 슬라이싱 (3장 문자열과 같아요)

scores[0] = 100         # 값 바꾸기 (문자열과 달리 가능!)
print(scores)
print("이순신" in names)
print(mixed, empty)
