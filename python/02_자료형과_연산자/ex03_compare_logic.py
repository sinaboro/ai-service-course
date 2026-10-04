# 비교 연산자: 결과는 True 또는 False
a = 10
b = 20
print(a == b, a != b)
print(a < b, a >= b)

# 논리 연산자
age = 25
print(age >= 20 and age < 30)   # 둘 다 참이어야 True
print(age < 10 or age > 20)     # 하나만 참이어도 True
print(not age > 20)             # 참/거짓을 뒤집기

# 파이썬은 범위 비교를 이렇게 쓸 수 있어요
print(20 <= age < 30)
