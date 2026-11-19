# 문제 2. lifespan에서 app.state.counter = 0으로 시작하고, /visit를 부를 때마다 1씩 늘려 돌려주세요. 세 번 호출한 결과를 출력하세요.

from contextlib import asynccontextmanager  # lifespan(켜질 때 · 꺼질 때 할 일)을 만드는 도구
from fastapi import FastAPI, Request
from fastapi.testclient import TestClient  # 서버를 켜지 않고 코드로 요청을 보내는 도구


@asynccontextmanager                        # 아래 함수를 lifespan(시작 · 종료 할 일)으로
async def lifespan(app: FastAPI):
    app.state.counter = 0
    yield                                   # yield 위 = 켜질 때, 아래 = 꺼질 때


app = FastAPI(lifespan=lifespan)


@app.get("/visit")
def visit(request: Request):
    request.app.state.counter += 1
    return {"count": request.app.state.counter}


with TestClient(app) as client:
    for _ in range(3):
        print(client.get("/visit").json()["count"])
