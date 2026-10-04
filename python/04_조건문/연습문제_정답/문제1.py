# 문제 1. n = 15가 3의 배수이면서 5의 배수이면 "FizzBuzz", 3의 배수면 "Fizz", 5의 배수면 "Buzz", 아니면 숫자를 출력하세요.

n = 15
if n % 3 == 0 and n % 5 == 0:
    print("FizzBuzz")
elif n % 3 == 0:
    print("Fizz")
elif n % 5 == 0:
    print("Buzz")
else:
    print(n)
