# 딕셔너리 반복
prices = {"사과": 1000, "바나나": 2500, "포도": 4000}

print(list(prices.keys()))
print(list(prices.values()))

for fruit in prices:                  # 기본은 키를 하나씩
    print(fruit, end=" ")
print()

for fruit, price in prices.items():  # 키와 값을 함께
    print(f"{fruit}: {price:,}원")

print("총합:", sum(prices.values()))
cheap = {k: v for k, v in prices.items() if v < 3000}   # 딕셔너리 컴프리헨션
print("3000원 미만:", cheap)
