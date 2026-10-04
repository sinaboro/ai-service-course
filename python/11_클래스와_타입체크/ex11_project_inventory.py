# 종합 실습: 타입 체크가 들어간 재고 관리
from dataclasses import dataclass

# @dataclass: __init__ 을 자동으로 만들어 주는 장식 (필드 이름: 자료형)
@dataclass
class Item:
    code: str
    name: str
    price: int
    stock: int = 0

    # __post_init__: 자동으로 만든 __init__ 이 끝난 뒤 실행 → 여기서 검사해요
    def __post_init__(self):
        # (필드 이름, 기대하는 자료형) 4쌍을 차례로 검사
        for field_name, expected in [("code", str), ("name", str), ("price", int), ("stock", int)]:
            value = getattr(self, field_name)
            if not isinstance(value, expected) or isinstance(value, bool):
                raise TypeError(f"{field_name} 은(는) {expected.__name__} 이어야 해요: {value!r}")
        if self.price < 0 or self.stock < 0:
            raise ValueError("price, stock 은 0 이상이어야 해요.")

class Inventory:
    # 상품들을 코드(A01 ...)로 찾을 수 있게 사전에 보관
    def __init__(self) -> None:
        self._items: dict[str, Item] = {}

    # 상품 추가: Item 객체만 받기
    def add(self, item: Item) -> None:
        if not isinstance(item, Item):
            raise TypeError("Item 객체만 추가할 수 있어요.")
        self._items[item.code] = item

    # 판매: 수량 검사 → 재고 검사 → 재고 줄이기 → 판매 금액 돌려주기
    def sell(self, code: str, qty: int) -> int:
        if not isinstance(qty, int) or qty <= 0:
            raise ValueError("수량은 1 이상의 정수여야 해요.")
        item = self._items[code]
        if item.stock < qty:
            raise ValueError(f"{item.name} 재고 부족 (남은 수량 {item.stock})")
        item.stock -= qty
        return item.price * qty

    # 남은 재고를 표처럼 출력 (:6 은 6칸, :>7, 는 오른쪽 정렬 + 쉼표)
    def report(self) -> None:
        for it in self._items.values():
            print(f"{it.code} {it.name:6} {it.price:>7,}원  재고 {it.stock}")

# 재고 관리 객체를 만들고 상품 2개 넣기
inv = Inventory()
inv.add(Item("A01", "마우스", 15000, 10))
inv.add(Item("A02", "키보드", 45000, 3))

print("판매 금액:", f"{inv.sell('A01', 4):,}원")

# 일부러 틀린 요청 4가지 (lambda: 나중에 실행할 짧은 함수로 묶어 두기)
requests = [
    lambda: inv.add({"code": "A03"}),               # Item 이 아님
    lambda: Item("A04", "모니터", "20만원", 1),      # price 가 str
    lambda: inv.sell("A02", 5),                      # 재고 부족
    lambda: inv.sell("A02", 1.5),                    # 수량이 실수
]
# 하나씩 실행하고, 오류가 나면 종류와 메시지 출력
for req in requests:
    try:
        req()
    except (TypeError, ValueError) as e:
        print(f"{type(e).__name__}: {e}")

inv.report()
