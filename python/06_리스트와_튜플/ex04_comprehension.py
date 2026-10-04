# 리스트 컴프리헨션: [식 for 변수 in 대상 if 조건]
# 1 ~ 5 의 제곱 → [1, 4, 9, 16, 25]
squares = [x ** 2 for x in range(1, 6)]
print(squares)

# if 조건을 붙이면 조건에 맞는 것만 → 짝수만
evens = [x for x in range(1, 11) if x % 2 == 0]
print(evens)

names = ["kim", "lee", "park"]
# 문자열에도 쓸 수 있어요: 모두 대문자로
upper_names = [n.upper() for n in names]
print(upper_names)

# 같은 일을 for 문으로 하면
squares2 = []
for x in range(1, 6):
    squares2.append(x ** 2)
print(squares2)
