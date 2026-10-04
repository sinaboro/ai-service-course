# 직접 만든 모듈: 다른 파일에서 import 해서 사용
# 상수: 대문자 이름은 "바꾸지 않을 값"이라는 약속
PI = 3.14159

# 원의 넓이 = 원주율 × 반지름 × 반지름
def circle_area(r):
    return PI * r * r

# 숫자 → "12,000원" 같은 글자
def won(n):
    return f"{n:,}원"
