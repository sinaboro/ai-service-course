# 누적 합계
total = 0
for i in range(1, 11):
    total += i
print("1 ~ 10 의 합:", total)

# 짝수의 합
even_sum = 0
for i in range(1, 101):
    if i % 2 == 0:
        even_sum += i
print("1 ~ 100 짝수의 합:", even_sum)

# 내장 함수 sum 으로 한 번에
print("sum 사용:", sum(range(1, 11)))
