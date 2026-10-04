# __init__ 에서 자료형과 값 검사하기
class Student:
    def __init__(self, name, age):
        # isinstance(값, 자료형): 그 자료형이 맞으면 True
        if not isinstance(name, str):
            raise TypeError(f"name 은 str 이어야 해요. 받은 값: {type(name).__name__}")
        # bool 은 int 의 한 종류(True == 1)라서 따로 막아요
        if not isinstance(age, int) or isinstance(age, bool):
            raise TypeError(f"age 는 int 이어야 해요. 받은 값: {type(age).__name__}")
        # 자료형은 맞지만 값이 틀린 경우는 ValueError
        if age < 0:
            raise ValueError(f"age 는 0 이상이어야 해요. 받은 값: {age}")
        # 검사를 모두 통과해야 속성에 저장
        self.name = name
        self.age = age

    def __str__(self):
        return f"Student({self.name}, {self.age}살)"

print(Student("홍길동", 20))

# 잘못된 값 4가지로 객체 만들어 보기
tests = [("이순신", "서른"), (123, 30), ("유관순", -5), ("강감찬", True)]
for name, age in tests:
    # 오류 종류에 따라 다른 메시지
    try:
        s = Student(name, age)
        print("생성 성공:", s)
    except TypeError as e:
        print("TypeError :", e)
    except ValueError as e:
        print("ValueError:", e)
