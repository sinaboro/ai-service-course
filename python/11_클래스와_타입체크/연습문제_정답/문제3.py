# 문제 3. Person 클래스에 age property를 만들어, setter에서 int가 아니면 TypeError, 0 ~ 150 범위가 아니면 ValueError를 발생시키세요. 25로 만든 뒤 "서른", 200, 30을 차례로 대입해 보세요.

class Person:
    def __init__(self, age):
        self.age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("나이는 int 여야 해요")
        if not 0 <= value <= 150:
            raise ValueError("나이는 0 ~ 150 사이여야 해요")
        self._age = value

p = Person(25)
for v in ["서른", 200, 30]:
    try:
        p.age = v
    except (TypeError, ValueError) as e:
        print(f"{type(e).__name__}: {e}")
print("최종 나이:", p.age)
