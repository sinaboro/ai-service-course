# 매개변수와 반환값
def add(a, b):              # a, b: 매개변수
    return a + b            # 결과를 돌려줌

result = add(3, 5)          # 3, 5: 인자
print(result)
print(add(10, 20) * 2)      # 반환값을 바로 계산에 사용

def is_even(n):
    return n % 2 == 0

print(is_even(4), is_even(7))

def calc(a, b):
    return a + b, a - b     # 여러 값 반환 → 튜플

plus, minus = calc(10, 3)
print(plus, minus)

def say(msg):               # return 이 없는 함수
    print(msg)

r = say("반환값이 없으면?")
print(r)                    # None
