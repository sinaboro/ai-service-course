# 변수: 값을 저장하는 이름표
name = "홍길동"
age = 20
height = 175.5

print(name)
print("나이:", age)
print("키:", height)

age = age + 1          # 변수 값 바꾸기
print("내년 나이:", age)

# 여러 변수에 한 번에 넣기
a, b, c = 1, 2, 3
print(a, b, c)

# 두 변수의 값 바꾸기
x, y = 10, 20
x, y = y, x
print("x =", x, ", y =", y)
