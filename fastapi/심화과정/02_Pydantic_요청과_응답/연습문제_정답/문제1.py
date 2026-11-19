# 문제 1. Review(BaseModel): product: str, stars: int(1 ~ 5), comment: str(최대 50자)를 정의하고 POST /reviews가 {"product": ..., "stars": ...}를 돌려주게 하세요. stars=7을 보내 상태 코드를 확인하세요.

from fastapi import FastAPI
from fastapi.testclient import TestClient  # 서버를 켜지 않고 코드로 요청을 보내는 도구
from pydantic import BaseModel, Field

app = FastAPI()  # 앱(서버) 만들기 — uvicorn 이 이 app 을 실행해요


class Review(BaseModel):
    product: str
    stars: int = Field(ge=1, le=5)
    comment: str = Field(default="", max_length=50)


@app.post("/reviews")
def create_review(r: Review):
    return {"product": r.product, "stars": r.stars}


client = TestClient(app)  # app 에 요청을 보내는 "코드 속 브라우저"
res = client.post("/reviews", json={"product": "마우스", "stars": 5, "comment": "좋아요"})
print(res.status_code, res.json())
print(client.post("/reviews", json={"product": "마우스", "stars": 7}).status_code)
