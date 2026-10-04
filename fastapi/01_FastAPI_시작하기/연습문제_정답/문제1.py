# 문제 1. GET /square/{n}에 정수 n을 받아 {"n": n, "square": n의 제곱}을 돌려주는 앱을 만들고, TestClient로 n=7을 요청해 보세요.

from fastapi import FastAPI
from fastapi.testclient import TestClient

app = FastAPI()


@app.get("/square/{n}")
def square(n: int):
    return {"n": n, "square": n * n}


client = TestClient(app)
print(client.get("/square/7").json())
