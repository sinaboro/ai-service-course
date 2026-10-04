from fastapi import FastAPI, status
from pydantic import BaseModel, Field

app = FastAPI()


class Item(BaseModel):
    name: str
    price: int = Field(gt=0)
    qty: int = Field(default=1, ge=1)


class Order(BaseModel):            # 모델 안에 모델 (중첩)
    customer: str
    items: list[Item] = Field(min_length=1)       # Item 들의 리스트, 최소 1개
    coupon: str | None = None


class UserIn(BaseModel):           # 요청으로 받는 모양 (비밀번호 포함)
    username: str
    password: str = Field(min_length=8)


class UserOut(BaseModel):          # 응답으로 돌려줄 모양 (비밀번호 없음!)
    username: str
    message: str


@app.post("/orders", status_code=status.HTTP_201_CREATED)     # 생성 성공은 201
def create_order(order: Order):
    total = sum(i.price * i.qty for i in order.items)
    if order.coupon == "WELCOME":
        total = int(total * 0.9)
    return {"customer": order.customer, "count": len(order.items), "total": total}


@app.post("/users", response_model=UserOut)    # 응답을 UserOut 모양으로 "걸러서" 보냄
def create_user(user: UserIn):
    return {"username": user.username, "password": user.password, "message": "가입 완료"}
