# 문제 2. 상품 이름(name)과 가격(price, 0 보다 큼), 할인율(discount, 0 ~ 50, 기본값 0)을 받아
#        할인된 가격을 돌려주는 POST /sale 을 만드세요.
#        예) {"name": "운동화", "price": 50000, "discount": 20} → {"name": "운동화", "sale_price": 40000}
# 실행: 이 폴더에서  uvicorn 문제2:app --reload  →  /docs 에서 시험
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class Item(BaseModel):
    name: str
    price: int = Field(gt=0)                       # gt: 0 보다 커야 해요 (0 은 안 돼요)
    discount: int = Field(default=0, ge=0, le=50)  # 0 ~ 50 %


@app.post("/sale")
def sale(item: Item):
    sale_price = item.price * (100 - item.discount) // 100   # // : 소수점 버린 나눗셈
    return {"name": item.name, "sale_price": sale_price}
