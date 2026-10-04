# 타입 힌트: "이런 자료형을 넣어 주세요" 라는 표시
def add(a: int, b: int) -> int:
    return a + b

name: str = "홍길동"
age: int = 20
scores: list[int] = [90, 85, 77]

print(add(3, 5))
print(add.__annotations__)        # 함수에 적힌 힌트 확인

# ⚠ 힌트는 실행 중에 검사되지 않아요!
print(add("안녕", "하세요"))       # 오류 없이 문자열이 이어져요
age = "스무 살"                    # 힌트와 다른 값이 들어가도 실행됨
print(age)
