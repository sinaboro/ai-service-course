import os
import time
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

APP_NAME = os.getenv("APP_NAME", "my-model-server")            # 환경 변수, 없으면 기본값
MODEL_VERSION = os.getenv("MODEL_VERSION", "1.0.0")
ALLOWED = os.getenv("ALLOWED_ORIGINS", "http://localhost:3000").split(",")

app = FastAPI(title=APP_NAME)

app.add_middleware(CORSMiddleware, allow_origins=ALLOWED,       # 다른 주소의 웹페이지에서 호출 허용
                   allow_methods=["*"], allow_headers=["*"])


@app.middleware("http")
async def add_process_time(request: Request, call_next):       # 모든 요청을 지나가는 관문
    start = time.perf_counter()
    response = await call_next(request)                        # 실제 API 실행
    ms = (time.perf_counter() - start) * 1000
    response.headers["X-Process-Time-ms"] = f"{ms:.1f}"
    response.headers["X-Model-Version"] = MODEL_VERSION
    return response


@app.get("/info")
def info():
    return {"app": APP_NAME, "model_version": MODEL_VERSION, "allowed_origins": ALLOWED}


@app.get("/slow")
def slow():
    time.sleep(0.05)
    return {"done": True}
