# 문제 4. @dataclass로 Score(name: str, points: list[int])를 만들고, __post_init__에서 points의 모든 원소가 0 ~ 100 사이 int인지 검사하세요. Score("A", [90, 80])과 Score("B", [90, "80"])으로 테스트하세요.

from dataclasses import dataclass

@dataclass
class Score:
    name: str
    points: list[int]

    def __post_init__(self):
        ok = isinstance(self.points, list) and all(
            isinstance(p, int) and not isinstance(p, bool) and 0 <= p <= 100 for p in self.points
        )
        if not ok:
            raise TypeError(f"points 의 모든 값은 0~100 사이 int 여야 해요: {self.points!r}")

print(Score("A", [90, 80]))
try:
    Score("B", [90, "80"])
except TypeError as e:
    print("TypeError:", e)
