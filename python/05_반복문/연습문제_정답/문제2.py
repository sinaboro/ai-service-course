# 문제 2. 5! = 5 × 4 × 3 × 2 × 1(팩토리얼)을 for로 계산하세요.

result = 1
for i in range(1, 6):
    result *= i
print("5! =", result)
