# 문제 2. 장바구니 API 를 만드세요. (메모장 API 와 같은 모양이에요)
#        POST /cart  {"item": "사과", "count": 3}  → 담기 (201)
#        GET  /cart                               → 담긴 목록과 전체 개수
#        DELETE /cart/{item}                      → 그 상품 빼기 (없으면 404)
# 실행: 이 폴더에서  uvicorn 문제2:app --reload  →  /docs 에서 시험
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()


class CartIn(BaseModel):
    item: str = Field(min_length=1)
    count: int = Field(default=1, ge=1, le=99)


cart = {}                                      # 상품 이름 → 개수


@app.post("/cart", status_code=201)
def add_to_cart(c: CartIn):
    cart[c.item] = cart.get(c.item, 0) + c.count   # 이미 있으면 개수를 더해요
    return {"item": c.item, "count": cart[c.item]}


@app.get("/cart")
def show_cart():
    return {"items": cart, "total_count": sum(cart.values())}


@app.delete("/cart/{item}")
def remove_from_cart(item: str):
    if item not in cart:
        raise HTTPException(status_code=404, detail=f"장바구니에 {item} 이(가) 없어요")
    del cart[item]
    return {"message": f"{item} 을(를) 뺐어요"}
