import time
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request

# 서버가 켜지고 꺼질 때 일어난 일을 기록할 목록
LOG: list[str] = []


def load_model():
    time.sleep(0.3)                                   # 큰 모델 파일을 읽는 데 시간이 걸린다고 가정
    LOG.append("모델 불러옴")
    # 가짜 모델: predict 는 x 를 받아 2배를 돌려주는 함수(lambda)
    return {"name": "demo-model", "version": "1.0", "predict": lambda x: x * 2}


# lifespan: 서버 시작 · 종료 때 할 일을 한 함수에 (yield 앞 = 시작, 뒤 = 종료)
@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.model = load_model()                     # ① 서버 시작: 한 번만 실행
    LOG.append("서버 시작")
    yield                                              # ② 이 동안 요청을 처리
    app.state.model = None                             # ③ 서버 종료: 정리
    LOG.append("서버 종료 (모델 해제)")


app = FastAPI(lifespan=lifespan)


@app.get("/predict")
def predict(x: float, request: Request):
    model = request.app.state.model                    # 미리 불러 둔 모델 사용 (매번 불러오지 않음)
    return {"model": model["name"], "x": x, "y": model["predict"](x)}


# 지금까지의 기록 보기
@app.get("/log")
def log():
    return LOG
