# 문제 3. Shape 부모 클래스(area()는 0 반환)를 상속받는 Square(한 변)와 Circle(반지름, π=3.14)을 만들고, 리스트에 담아 넓이를 출력하세요.

class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r ** 2

for shape in [Square(4), Circle(2)]:
    print(shape.area())
