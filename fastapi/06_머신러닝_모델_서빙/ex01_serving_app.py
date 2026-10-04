import os
from contextlib import asynccontextmanager
from typing import Annotated

import numpy as np
from fastapi import Depends, FastAPI, HTTPException, Request
from pydantic import BaseModel, Field

from model_core import PassModel

MODEL_PATH = os.getenv("MODEL_PATH", os.path.join(os.path.dirname(__file__), "model", "pass_model.npz"))


# ── 입력·출력 스키마 ──
class StudentFeatures(BaseModel):
    study_h: float = Field(ge=0, le=16, description="하루 공부 시간", examples=[4.5])
    sleep_h: float = Field(ge=0, le=16, description="하루 수면 시간", examples=[7.0])
    phone_h: float = Field(ge=0, le=24, description="하루 휴대폰 사용 시간", examples=[2.0])


class Prediction(BaseModel):
    pass_probability: float
    label: str
    model_version: str


class BatchRequest(BaseModel):
    students: list[StudentFeatures] = Field(min_length=1, max_length=100)


class BatchResponse(BaseModel):
    count: int
    predictions: list[Prediction]


# ── 서버 시작 시 모델 한 번 불러오기 ──
@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        app.state.model = PassModel.load(MODEL_PATH)
        app.state.model_error = None
    except Exception as e:                       # 모델이 없어도 서버는 켜지게
        app.state.model = None
        app.state.model_error = f"{type(e).__name__}: {e}"
    app.state.n_predictions = 0
    yield
    app.state.model = None


app = FastAPI(title="합격 예측 API", version="1.0.0", lifespan=lifespan)


def get_model(request: Request) -> PassModel:   # 의존성: 모델 꺼내기 (없으면 503)
    model = request.app.state.model
    if model is None:
        raise HTTPException(status_code=503, detail="모델이 준비되지 않았어요")
    return model


Model = Annotated[PassModel, Depends(get_model)]


def to_array(items: list[StudentFeatures]) -> np.ndarray:
    return np.array([[s.study_h, s.sleep_h, s.phone_h] for s in items])   # 학습 때와 같은 열 순서


def make_prediction(p: float, version: str) -> Prediction:
    return Prediction(pass_probability=round(float(p), 4), label="합격" if p >= 0.5 else "불합격",
                      model_version=version)


@app.get("/health", tags=["status"])
def health(request: Request):
    return {"status": "ok", "model_loaded": request.app.state.model is not None,
            "model_error": request.app.state.model_error}


@app.get("/model/info", tags=["status"])
def model_info(model: Model, request: Request):
    return {**model.card, "predictions_served": request.app.state.n_predictions}


@app.post("/predict", response_model=Prediction, tags=["predict"])
def predict(student: StudentFeatures, model: Model, request: Request):
    p = model.predict_proba(to_array([student]))[0]
    request.app.state.n_predictions += 1
    return make_prediction(p, model.version)


@app.post("/predict/batch", response_model=BatchResponse, tags=["predict"])
def predict_batch(req: BatchRequest, model: Model, request: Request):
    probs = model.predict_proba(to_array(req.students))       # 한 번에 계산 (빠름)
    request.app.state.n_predictions += len(probs)
    return BatchResponse(count=len(probs), predictions=[make_prediction(p, model.version) for p in probs])
