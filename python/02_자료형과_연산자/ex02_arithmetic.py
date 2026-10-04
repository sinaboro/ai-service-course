# 산술 연산자
x = 17
y = 5
print("더하기   :", x + y)
print("빼기     :", x - y)
print("곱하기   :", x * y)
print("나누기   :", x / y)    # 결과는 항상 실수
print("몫       :", x // y)
print("나머지   :", x % y)
print("거듭제곱 :", x ** 2)

# 복합 대입 연산자
n = 10
n += 5      # n = n + 5
n *= 2      # n = n * 2
print("n =", n)

# 연산 순서: ** → * / // % → + -
print(2 + 3 * 4)       # 14
print((2 + 3) * 4)     # 20
