# 문제 1. 원의 반지름을 받아 넓이를 돌려주는 함수 circle_area(r)를 만들고 r=3일 때 소수점 2자리로 출력하세요. (π = 3.14159)

def circle_area(r):
    return 3.14159 * r * r

print(f"넓이: {circle_area(3):.2f}")
