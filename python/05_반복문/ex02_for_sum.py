# 누적 합계
total = 0
# range(1, 11): 1 부터 10 까지 (11 은 포함하지 않아요)
for i in range(1, 11):
    # total += i 는 total = total + i 와 같아요
    total += i
print("1 ~ 10 의 합:", total)

# 짝수의 합
even_sum = 0
# 1 ~ 100 중에서
for i in range(1, 101):
    # 2로 나눈 나머지가 0 인 수(짝수)만 더하기
    if i % 2 == 0:
        even_sum += i
print("1 ~ 100 짝수의 합:", even_sum)

# 내장 함수 sum 으로 한 번에
print("sum 사용:", sum(range(1, 11)))
