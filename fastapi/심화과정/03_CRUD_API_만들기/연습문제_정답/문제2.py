# 문제 2. 재고가 {"apple": 5}인 상점에서 POST /buy?item=apple&qty=8처럼 재고보다 많이 사면 400 과 "재고 부족" 메시지를 돌려주는 API를 만드세요.

from fastapi import FastAPI, HTTPException
from fastapi.testclient import TestClient  # 서버를 켜지 않고 코드로 요청을 보내는 도구

app = FastAPI()  # 앱(서버) 만들기 — uvicorn 이 이 app 을 실행해요
STOCK = {"apple": 5}


@app.post("/buy")
def buy(item: str, qty: int):
    if item not in STOCK:
        raise HTTPException(404, "없는 상품")
    if qty > STOCK[item]:
        raise HTTPException(400, f"재고 부족 (남은 수량 {STOCK[item]})")
    STOCK[item] -= qty
    return {"item": item, "left": STOCK[item]}


client = TestClient(app)  # app 에 요청을 보내는 "코드 속 브라우저"
r = client.post("/buy?item=apple&qty=3"); print(r.status_code, r.json())
r = client.post("/buy?item=apple&qty=8"); print(r.status_code, r.json())
