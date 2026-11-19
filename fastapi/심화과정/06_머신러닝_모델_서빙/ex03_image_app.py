# ex03_image_app.py : 이미지 분류 API: 업로드한 사진의 색을 보고 red · green · blue 확률 돌려주기
# 먼저 python ex00_train_model.py 로 모델을 만든 뒤, 이 폴더에서 uvicorn ex03_image_app:app --reload
import io                                                        # 메모리를 파일처럼 쓰는 도구 (BytesIO)
import os                                                        # 환경 변수 · 경로 같은 운영체제 기능
from contextlib import asynccontextmanager  # lifespan(켜질 때 · 꺼질 때 할 일)을 만드는 도구

import numpy as np                                               # 넘파이 (관례적으로 np 라는 별명)
from fastapi import FastAPI, HTTPException, Request, UploadFile
from PIL import Image, UnidentifiedImageError
from pydantic import BaseModel

from model_core import ColorModel

# 이 파일이 있는 폴더 (모델 파일 위치 기준)
HERE = os.path.dirname(__file__)


def preprocess(img: Image.Image, size=(32, 32)) -> np.ndarray:   # 5장의 전처리와 같은 방식
    arr = np.asarray(img.convert("RGB").resize(size), dtype=np.float32) / 255.0
    return arr[np.newaxis, ...]                                   # (1, 32, 32, 3)


# 클래스 하나의 점수 / 응답 전체 모양
class ClassScore(BaseModel):
    label: str
    probability: float


class ImagePrediction(BaseModel):
    filename: str
    top: ClassScore
    scores: list[ClassScore]
    model_version: str


# 서버 시작 때 색 분류 모델 불러오기
@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.model = ColorModel(os.path.join(HERE, "model", "color_model.npz"))
    yield                                                        # yield 위 = 켜질 때, 아래 = 꺼질 때


app = FastAPI(title="이미지 색 분류 API", lifespan=lifespan)


@app.post("/predict/image", response_model=ImagePrediction)
async def predict_image(file: UploadFile, request: Request):
    try:
        img = Image.open(io.BytesIO(await file.read()))
    except UnidentifiedImageError:
        raise HTTPException(400, "이미지를 읽을 수 없어요")
    model = request.app.state.model
    probs = model.predict_proba(preprocess(img))[0]
    # 확률이 높은 순서로 정렬해서 1등(top)과 전체 점수를 돌려주기
    scores = sorted([ClassScore(label=c, probability=round(float(p), 4)) for c, p in zip(model.classes, probs)],
                    key=lambda s: s.probability, reverse=True)   # 확률이 큰 순서로
    return ImagePrediction(filename=file.filename, top=scores[0], scores=scores, model_version=model.version)
