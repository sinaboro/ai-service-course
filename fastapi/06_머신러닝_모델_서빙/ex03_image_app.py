import io
import os
from contextlib import asynccontextmanager

import numpy as np
from fastapi import FastAPI, HTTPException, Request, UploadFile
from PIL import Image, UnidentifiedImageError
from pydantic import BaseModel

from model_core import ColorModel

HERE = os.path.dirname(__file__)


def preprocess(img: Image.Image, size=(32, 32)) -> np.ndarray:   # 5장의 전처리와 같은 방식
    arr = np.asarray(img.convert("RGB").resize(size), dtype=np.float32) / 255.0
    return arr[np.newaxis, ...]                                   # (1, 32, 32, 3)


class ClassScore(BaseModel):
    label: str
    probability: float


class ImagePrediction(BaseModel):
    filename: str
    top: ClassScore
    scores: list[ClassScore]
    model_version: str


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.model = ColorModel(os.path.join(HERE, "model", "color_model.npz"))
    yield


app = FastAPI(title="이미지 색 분류 API", lifespan=lifespan)


@app.post("/predict/image", response_model=ImagePrediction)
async def predict_image(file: UploadFile, request: Request):
    try:
        img = Image.open(io.BytesIO(await file.read()))
    except UnidentifiedImageError:
        raise HTTPException(400, "이미지를 읽을 수 없어요")
    model = request.app.state.model
    probs = model.predict_proba(preprocess(img))[0]
    scores = sorted([ClassScore(label=c, probability=round(float(p), 4)) for c, p in zip(model.classes, probs)],
                    key=lambda s: s.probability, reverse=True)
    return ImagePrediction(filename=file.filename, top=scores[0], scores=scores, model_version=model.version)
