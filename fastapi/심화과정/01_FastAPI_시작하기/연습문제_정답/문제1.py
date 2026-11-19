# 문제 1. GET /square/{n}에 정수 n을 받아 {"n": n, "square": n의 제곱}을 돌려주는 앱을 만들고, TestClient로 n=7을 요청해 보세요.

from fastapi import FastAPI
from fastapi.testclient import TestClient  # 서버를 켜지 않고 코드로 요청을 보내는 도구

app = FastAPI()  # 앱(서버) 만들기 — uvicorn 이 이 app 을 실행해요


@app.get("/square/{n}")
def square(n: int):
    return {"n": n, "square": n * n}


client = TestClient(app)  # app 에 요청을 보내는 "코드 속 브라우저"
print(client.get("/square/7").json())
