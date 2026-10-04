# 지역 변수와 전역 변수
count = 0                 # 전역 변수 (함수 밖)

def func():
    x = 10                # 지역 변수 (함수 안에서만)
    print("함수 안 x:", x)
    print("함수 안에서 전역 count 읽기:", count)

func()
# print(x)                # 오류! 함수 밖에서는 x 가 없어요

def increase():
    global count          # 전역 변수를 바꾸려면 global
    count += 1

increase()
increase()
print("count:", count)
