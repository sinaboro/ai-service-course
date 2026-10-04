# 문제 5. 덕 타이핑으로 area라는 메서드가 있는 객체만 넓이를 더하는 함수 total_area(shapes)를 만드세요. area가 없는 값은 건너뛰세요.

class Square:
    def __init__(self, s): self.s = s
    def area(self): return self.s ** 2

class Circle:
    def __init__(self, r): self.r = r
    def area(self): return 3.0 * self.r ** 2

def total_area(shapes):
    total = 0.0
    for sh in shapes:
        if hasattr(sh, "area") and callable(sh.area):
            total += sh.area()
    return total

print("총 넓이:", total_area([Square(5), Circle(2), "삼각형", 42]))
