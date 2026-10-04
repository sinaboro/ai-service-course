# dataclass: __init__, __repr__ 를 자동으로 만들어 주는 도구
from dataclasses import dataclass, field

@dataclass
class Book:
    title: str
    author: str
    price: int = 0                       # 기본값
    tags: list[str] = field(default_factory=list)   # 리스트 기본값은 이렇게

    def __post_init__(self):             # __init__ 이 끝난 직후 자동 실행 → 검사하기 좋은 곳
        if not isinstance(self.title, str) or not self.title:
            raise TypeError("title 은 비어 있지 않은 str 이어야 해요.")
        if not isinstance(self.price, int):
            raise TypeError("price 는 int 여야 해요.")

b1 = Book("파이썬 첫걸음", "김파이", 15000, ["입문"])
b2 = Book("넘파이 기초", "이넘", 18000)
print(b1)                                # 보기 좋은 출력이 자동으로
print(b2.tags)
print(b1 == Book("파이썬 첫걸음", "김파이", 15000, ["입문"]))   # 값이 같으면 같다 (== 자동)

try:
    Book("가격 오류", "누군가", "만오천원")
except TypeError as e:
    print("TypeError:", e)
