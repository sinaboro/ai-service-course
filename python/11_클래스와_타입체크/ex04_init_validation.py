# __init__ 에서 자료형과 값 검사하기
class Student:
    def __init__(self, name, age):
        if not isinstance(name, str):
            raise TypeError(f"name 은 str 이어야 해요. 받은 값: {type(name).__name__}")
        if not isinstance(age, int) or isinstance(age, bool):
            raise TypeError(f"age 는 int 이어야 해요. 받은 값: {type(age).__name__}")
        if age < 0:
            raise ValueError(f"age 는 0 이상이어야 해요. 받은 값: {age}")
        self.name = name
        self.age = age

    def __str__(self):
        return f"Student({self.name}, {self.age}살)"

print(Student("홍길동", 20))

tests = [("이순신", "서른"), (123, 30), ("유관순", -5), ("강감찬", True)]
for name, age in tests:
    try:
        s = Student(name, age)
        print("생성 성공:", s)
    except TypeError as e:
        print("TypeError :", e)
    except ValueError as e:
        print("ValueError:", e)
