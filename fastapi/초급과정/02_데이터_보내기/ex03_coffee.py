# 2장 예제 3: 커피 주문 받기 — 받은 값으로 계산해서 돌려주기
# 실행: 이 폴더에서  uvicorn ex03_coffee:app --reload
# 확인: /docs 에서 POST /order 를 열고 menu, size, count 를 바꿔 가며 보내 보세요
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

PRICE = {"아메리카노": 3000, "라떼": 3500, "녹차": 3200}      # 메뉴별 가격 (M 사이즈)


class Order(BaseModel):
    menu: str                                  # 메뉴 이름
    size: str = "M"                            # 기본값이 있으면 안 보내도 돼요 (S, M, L)
    count: int = Field(default=1, ge=1, le=10) # 1 ~ 10잔


@app.post("/order")
def order(o: Order):
    if o.menu not in PRICE:
        return {"error": f"{o.menu} 는 없는 메뉴예요", "menus": list(PRICE)}
    price = PRICE[o.menu]
    if o.size == "L":                          # L 사이즈는 500원 더
        price += 500
    return {"menu": o.menu, "size": o.size, "count": o.count, "total": price * o.count}
