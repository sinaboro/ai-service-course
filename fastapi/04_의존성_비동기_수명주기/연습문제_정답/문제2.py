# 문제 2. lifespan에서 app.state.counter = 0으로 시작하고, /visit를 부를 때마다 1씩 늘려 돌려주세요. 세 번 호출한 결과를 출력하세요.

from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from fastapi.testclient import TestClient


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.counter = 0
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/visit")
def visit(request: Request):
    request.app.state.counter += 1
    return {"count": request.app.state.counter}


with TestClient(app) as client:
    for _ in range(3):
        print(client.get("/visit").json()["count"])
