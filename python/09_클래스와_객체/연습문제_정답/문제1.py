# 문제 1. Rectangle 클래스를 만들어 가로·세로를 받고, area()(넓이)와 perimeter()(둘레) 메서드를 만드세요. 가로 4, 세로 5로 테스트하세요.

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

r = Rectangle(4, 5)
print("넓이:", r.area())
print("둘레:", r.perimeter())
