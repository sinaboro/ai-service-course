# 문제 4. 아래처럼 숫자 피라미드를 출력하세요.

for line in range(1, 5):
    for n in range(1, line + 1):
        print(n, end="")
    print()
