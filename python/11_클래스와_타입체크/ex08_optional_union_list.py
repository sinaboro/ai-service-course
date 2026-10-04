# Optional, Union(|), list[int] 힌트와 원소 검사
from typing import Optional

class Member:
    # Optional[str] = str 또는 None, list[int] | None = 정수 리스트 또는 None
    def __init__(self, name: str, email: Optional[str] = None, scores: list[int] | None = None):
        if not isinstance(name, str):
            raise TypeError("name 은 str")
        if email is not None and not isinstance(email, str):     # None 이거나 str
            raise TypeError("email 은 str 또는 None")
        # scores 를 안 주면 빈 리스트로 (기본값에 [] 를 직접 쓰면 모든 객체가 같은 리스트 하나를 함께 쓰게 돼요)
        scores = scores if scores is not None else []
        # all(...): 모든 원소가 int 인지 한 번에 검사
        if not isinstance(scores, list) or not all(isinstance(s, int) for s in scores):
            raise TypeError("scores 는 int 들의 list")
        self.name = name
        self.email = email
        self.scores = scores

    # 점수가 없으면 평균 대신 None
    def average(self) -> float | None:
        if not self.scores:
            return None
        return sum(self.scores) / len(self.scores)

m1 = Member("홍길동", "hong@test.com", [90, 80])
m2 = Member("이순신")                         # email, scores 생략
print(m1.name, m1.email, m1.average())
print(m2.name, m2.email, m2.average())

# 잘못된 scores 3가지: 글자 섞임, 튜플, 실수
for bad in [[90, "80"], (90, 80), [1.5]]:
    try:
        Member("검사", scores=bad)
    except TypeError as e:
        print(f"{bad!r} → {e}")
