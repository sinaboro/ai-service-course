# 문제 3. /predict의 응답에 advice(합격 확률이 0.5 미만이면 "공부 시간을 늘려 보세요", 아니면 "지금처럼!")를 추가한 새 앱을 만들어 보세요. (힌트: 기존 앱의 모델 클래스와 같은 방식으로 lifespan에서 불러오기)

# 정답 폴더에서 실행해도 되도록: 장 폴더(06_...)를 import 경로와 작업 폴더로 지정
import os                                        # 환경 변수 · 경로 같은 운영체제 기능
import sys                                       # 파이썬 실행 환경 (import 경로 sys.path 등)
CHAPTER = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, CHAPTER)                      # model_core, ex01_serving_app 을 찾을 수 있게
os.chdir(CHAPTER)                                # "model/pass_model.npz" 같은 상대 경로가 맞도록

from contextlib import asynccontextmanager       # lifespan(켜질 때 · 꺼질 때 할 일)을 만드는 도구
import numpy as np                               # 넘파이 (관례적으로 np 라는 별명)
from fastapi import FastAPI, Request
from fastapi.testclient import TestClient        # 서버를 켜지 않고 코드로 요청을 보내는 도구
from pydantic import BaseModel, Field
from model_core import PassModel


class Features(BaseModel):
    study_h: float = Field(ge=0, le=16)
    sleep_h: float = Field(ge=0, le=16)
    phone_h: float = Field(ge=0, le=24)


@asynccontextmanager                             # 아래 함수를 lifespan(시작 · 종료 할 일)으로
async def lifespan(app: FastAPI):
    app.state.model = PassModel.load("model/pass_model.npz")
    yield                                        # yield 위 = 켜질 때, 아래 = 꺼질 때


app = FastAPI(lifespan=lifespan)


@app.post("/predict")
def predict(f: Features, request: Request):
    p = float(request.app.state.model.predict_proba(np.array([[f.study_h, f.sleep_h, f.phone_h]]))[0])
    return {"pass_probability": round(p, 3), "advice": "공부 시간을 늘려 보세요" if p < 0.5 else "지금처럼!"}


with TestClient(app) as c:
    print(c.post("/predict", json={"study_h": 1, "sleep_h": 8, "phone_h": 5}).json())
    print(c.post("/predict", json={"study_h": 5, "sleep_h": 7, "phone_h": 1}).json())
