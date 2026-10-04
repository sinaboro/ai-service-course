# Optional, Union(|), list[int] 힌트와 원소 검사
from typing import Optional

class Member:
    def __init__(self, name: str, email: Optional[str] = None, scores: list[int] | None = None):
        if not isinstance(name, str):
            raise TypeError("name 은 str")
        if email is not None and not isinstance(email, str):     # None 이거나 str
            raise TypeError("email 은 str 또는 None")
        scores = scores if scores is not None else []
        if not isinstance(scores, list) or not all(isinstance(s, int) for s in scores):
            raise TypeError("scores 는 int 들의 list")
        self.name = name
        self.email = email
        self.scores = scores

    def average(self) -> float | None:
        if not self.scores:
            return None
        return sum(self.scores) / len(self.scores)

m1 = Member("홍길동", "hong@test.com", [90, 80])
m2 = Member("이순신")                         # email, scores 생략
print(m1.name, m1.email, m1.average())
print(m2.name, m2.email, m2.average())

for bad in [[90, "80"], (90, 80), [1.5]]:
    try:
        Member("검사", scores=bad)
    except TypeError as e:
        print(f"{bad!r} → {e}")
