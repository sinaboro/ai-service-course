# ex01_serving_app.py : 모델 서빙 앱: 서버가 켜질 때 모델을 불러오고 /predict 로 합격 확률 예측
# 먼저 python ex00_train_model.py 로 모델을 만든 뒤, 이 폴더에서 uvicorn ex01_serving_app:app --reload
import os                                        # 환경 변수 · 경로 같은 운영체제 기능
from contextlib import asynccontextmanager       # lifespan(켜질 때 · 꺼질 때 할 일)을 만드는 도구
from typing import Annotated                     # 타입 힌트에 Depends 같은 정보를 덧붙이는 도구

import numpy as np                               # 넘파이 (관례적으로 np 라는 별명)
from fastapi import Depends, FastAPI, HTTPException, Request
from pydantic import BaseModel, Field

from model_core import PassModel

# 모델 파일 위치: 환경 변수 MODEL_PATH 가 있으면 그것, 없으면 이 폴더의 model/pass_model.npz
MODEL_PATH = os.getenv("MODEL_PATH", os.path.join(os.path.dirname(__file__), "model", "pass_model.npz"))


# ── 입력·출력 스키마 ──
class StudentFeatures(BaseModel):
    study_h: float = Field(ge=0, le=16, description="하루 공부 시간", examples=[4.5])
    sleep_h: float = Field(ge=0, le=16, description="하루 수면 시간", examples=[7.0])
    phone_h: float = Field(ge=0, le=24, description="하루 휴대폰 사용 시간", examples=[2.0])


# 응답 하나의 모양: 합격 확률 · 결과 · 모델 버전
class Prediction(BaseModel):
    pass_probability: float
    label: str
    model_version: str


# 여러 명을 한 번에 (1 ~ 100명)
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
    # 예측 횟수 세기용 변수
    app.state.n_predictions = 0
    yield                                        # yield 위 = 켜질 때, 아래 = 꺼질 때
    app.state.model = None


app = FastAPI(title="합격 예측 API", version="1.0.0", lifespan=lifespan)


def get_model(request: Request) -> PassModel:   # 의존성: 모델 꺼내기 (없으면 503)
    model = request.app.state.model
    if model is None:
        raise HTTPException(status_code=503, detail="모델이 준비되지 않았어요")
    return model


# 다른 함수에서 model: Model 로 쓰면 get_model 을 거쳐 모델이 들어와요
Model = Annotated[PassModel, Depends(get_model)]


def to_array(items: list[StudentFeatures]) -> np.ndarray:
    return np.array([[s.study_h, s.sleep_h, s.phone_h] for s in items])   # 학습 때와 같은 열 순서


def make_prediction(p: float, version: str) -> Prediction:
    return Prediction(pass_probability=round(float(p), 4), label="합격" if p >= 0.5 else "불합격",
                      model_version=version)


# 상태 확인: 모델이 불러와졌는지, 실패했다면 이유
@app.get("/health", tags=["status"])
def health(request: Request):
    return {"status": "ok", "model_loaded": request.app.state.model is not None,
            "model_error": request.app.state.model_error}


@app.get("/model/info", tags=["status"])
def model_info(model: Model, request: Request):
    # 모델 설명서 내용 + 예측 횟수
    return {**model.card, "predictions_served": request.app.state.n_predictions}


# 한 명 예측: 입력 → 배열 → 확률 → 응답 모양
@app.post("/predict", response_model=Prediction, tags=["predict"])
def predict(student: StudentFeatures, model: Model, request: Request):
    p = model.predict_proba(to_array([student]))[0]
    request.app.state.n_predictions += 1
    return make_prediction(p, model.version)


# 여러 명 예측
@app.post("/predict/batch", response_model=BatchResponse, tags=["predict"])
def predict_batch(req: BatchRequest, model: Model, request: Request):
    probs = model.predict_proba(to_array(req.students))       # 한 번에 계산 (빠름)
    request.app.state.n_predictions += len(probs)
    # 확률마다 Prediction 하나씩
    return BatchResponse(count=len(probs), predictions=[make_prediction(p, model.version) for p in probs])
