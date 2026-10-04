# @property: 속성을 바꿀 때마다 검사하기
class Product:
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price          # ← 여기서도 아래 setter 가 실행돼요

    # 실제 값은 밑줄이 붙은 self._price 에 저장해요
    @property
    def price(self) -> int:         # 읽을 때: p.price
        return self._price

    @price.setter
    def price(self, value: int) -> None:   # 쓸 때: p.price = 값
        if not isinstance(value, int):
            raise TypeError("가격은 정수(int)여야 해요.")
        if value < 0:
            raise ValueError("가격은 0 이상이어야 해요.")
        # 검사를 통과해야만 저장
        self._price = value

p = Product("마우스", 15000)
print(p.name, p.price)

p.price = 18000                     # 정상 변경
print("변경 후:", p.price)

# 잘못된 값 3가지 넣어 보기
for wrong in ["2만원", -500, 9.99]:
    try:
        p.price = wrong
    except (TypeError, ValueError) as e:
        print(f"{wrong!r} → {type(e).__name__}: {e}")

print("최종 가격:", p.price)        # 잘못된 값은 하나도 들어가지 않았어요
