# 읽기 전용 속성과 계산 속성
class Circle:
    def __init__(self, radius: float):
        # 숫자(int 또는 float)가 아니면 오류 / float 로 바꿔 저장
        if not isinstance(radius, (int, float)):
            raise TypeError("반지름은 숫자여야 해요.")
        self._radius = float(radius)

    @property
    def radius(self) -> float:        # setter 가 없으면 읽기 전용
        return self._radius

    @property
    def area(self) -> float:          # 저장하지 않고 그때그때 계산
        return round(3.14159 * self._radius ** 2, 2)

# 괄호 없이 c.radius, c.area 로 읽어요
c = Circle(3)
print(c.radius, c.area)

try:
    c.radius = 10                     # setter 가 없어서 바꿀 수 없음
except AttributeError as e:
    print("AttributeError:", e)
