# 리스트 컴프리헨션: [식 for 변수 in 대상 if 조건]
squares = [x ** 2 for x in range(1, 6)]
print(squares)

evens = [x for x in range(1, 11) if x % 2 == 0]
print(evens)

names = ["kim", "lee", "park"]
upper_names = [n.upper() for n in names]
print(upper_names)

# 같은 일을 for 문으로 하면
squares2 = []
for x in range(1, 6):
    squares2.append(x ** 2)
print(squares2)
