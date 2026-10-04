# 문제 3. /predict의 응답에 advice(합격 확률이 0.5 미만이면 "공부 시간을 늘려 보세요", 아니면 "지금처럼!")를 추가한 새 앱을 만들어 보세요. (힌트: 기존 앱의 모델 클래스와 같은 방식으로 lifespan에서 불러오기)

from contextlib import asynccontextmanager
import numpy as np
from fastapi import FastAPI, Request
from fastapi.testclient import TestClient
from pydantic import BaseModel, Field
from model_core import PassModel


class Features(BaseModel):
    study_h: float = Field(ge=0, le=16)
    sleep_h: float = Field(ge=0, le=16)
    phone_h: float = Field(ge=0, le=24)


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.model = PassModel.load("model/pass_model.npz")
    yield


app = FastAPI(lifespan=lifespan)


@app.post("/predict")
def predict(f: Features, request: Request):
    p = float(request.app.state.model.predict_proba(np.array([[f.study_h, f.sleep_h, f.phone_h]]))[0])
    return {"pass_probability": round(p, 3), "advice": "공부 시간을 늘려 보세요" if p < 0.5 else "지금처럼!"}


with TestClient(app) as c:
    print(c.post("/predict", json={"study_h": 1, "sleep_h": 8, "phone_h": 5}).json())
    print(c.post("/predict", json={"study_h": 5, "sleep_h": 7, "phone_h": 1}).json())
