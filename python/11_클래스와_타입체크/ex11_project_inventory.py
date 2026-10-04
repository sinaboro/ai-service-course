# 종합 실습: 타입 체크가 들어간 재고 관리
from dataclasses import dataclass

@dataclass
class Item:
    code: str
    name: str
    price: int
    stock: int = 0

    def __post_init__(self):
        for field_name, expected in [("code", str), ("name", str), ("price", int), ("stock", int)]:
            value = getattr(self, field_name)
            if not isinstance(value, expected) or isinstance(value, bool):
                raise TypeError(f"{field_name} 은(는) {expected.__name__} 이어야 해요: {value!r}")
        if self.price < 0 or self.stock < 0:
            raise ValueError("price, stock 은 0 이상이어야 해요.")

class Inventory:
    def __init__(self) -> None:
        self._items: dict[str, Item] = {}

    def add(self, item: Item) -> None:
        if not isinstance(item, Item):
            raise TypeError("Item 객체만 추가할 수 있어요.")
        self._items[item.code] = item

    def sell(self, code: str, qty: int) -> int:
        if not isinstance(qty, int) or qty <= 0:
            raise ValueError("수량은 1 이상의 정수여야 해요.")
        item = self._items[code]
        if item.stock < qty:
            raise ValueError(f"{item.name} 재고 부족 (남은 수량 {item.stock})")
        item.stock -= qty
        return item.price * qty

    def report(self) -> None:
        for it in self._items.values():
            print(f"{it.code} {it.name:6} {it.price:>7,}원  재고 {it.stock}")

inv = Inventory()
inv.add(Item("A01", "마우스", 15000, 10))
inv.add(Item("A02", "키보드", 45000, 3))

print("판매 금액:", f"{inv.sell('A01', 4):,}원")

requests = [
    lambda: inv.add({"code": "A03"}),               # Item 이 아님
    lambda: Item("A04", "모니터", "20만원", 1),      # price 가 str
    lambda: inv.sell("A02", 5),                      # 재고 부족
    lambda: inv.sell("A02", 1.5),                    # 수량이 실수
]
for req in requests:
    try:
        req()
    except (TypeError, ValueError) as e:
        print(f"{type(e).__name__}: {e}")

inv.report()
