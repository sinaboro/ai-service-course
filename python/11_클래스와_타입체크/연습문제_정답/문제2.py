# 문제 2. Rectangle(width, height) 클래스를 만들되, 두 값이 int 또는 float가 아니면 TypeError, 0 이하면 ValueError를 발생시키세요. (3, 4), ("3", 4), (3, -1)로 테스트하세요.

class Rectangle:
    def __init__(self, width, height):
        for v in (width, height):
            if not isinstance(v, (int, float)) or isinstance(v, bool):
                raise TypeError("width, height 는 숫자여야 해요")
            if v <= 0:
                raise ValueError("width, height 는 0보다 커야 해요")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

for args in [(3, 4), ("3", 4), (3, -1)]:
    try:
        print("넓이:", Rectangle(*args).area())
    except (TypeError, ValueError) as e:
        print(f"{type(e).__name__}: {e}")
