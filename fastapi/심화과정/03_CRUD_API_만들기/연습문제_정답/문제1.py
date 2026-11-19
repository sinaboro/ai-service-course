# 문제 1. 메모리 딕셔너리로 회원(name, email) 을 저장하는 POST /members(201)와 GET /members/{id}(없으면 404)를 만들고, 만든 뒤 1번과 99번을 조회해 상태 코드를 출력하세요.

from fastapi import FastAPI, HTTPException
from fastapi.testclient import TestClient  # 서버를 켜지 않고 코드로 요청을 보내는 도구
from pydantic import BaseModel

app = FastAPI()  # 앱(서버) 만들기 — uvicorn 이 이 app 을 실행해요
MEMBERS: dict[int, dict] = {}


class MemberIn(BaseModel):
    name: str
    email: str


@app.post("/members", status_code=201)
def create(m: MemberIn):
    new_id = len(MEMBERS) + 1
    MEMBERS[new_id] = {"id": new_id, **m.model_dump()}  # id + 받은 값(name, email)을 펼쳐 저장
    return MEMBERS[new_id]


@app.get("/members/{member_id}")
def read(member_id: int):
    if member_id not in MEMBERS:
        raise HTTPException(404, "회원이 없어요")
    return MEMBERS[member_id]


client = TestClient(app)  # app 에 요청을 보내는 "코드 속 브라우저"
print(client.post("/members", json={"name": "kim", "email": "kim@test.com"}).status_code)
r = client.get("/members/1"); print(r.status_code, r.json())
r = client.get("/members/99"); print(r.status_code, r.json())
