# while: 조건이 참인 동안 반복
n = 1
while n <= 5:
    print("n =", n)
    n += 1              # 이 줄이 없으면 영원히 반복!

# 합이 100 을 넘을 때까지 더하기
total = 0
count = 0
while total <= 100:
    count += 1
    total += count
print(f"{count}까지 더하면 {total} (처음으로 100 초과)")
