# 가장 간단한 예측 API — 모델을 한 번 불러 두고, POST /predict 로 합격 확률 돌려주기 (서버로 실행)
# 준비: 이 폴더에서 먼저  python ex00_train_model.py  (model/pass_model.npz 가 없을 때만)
# 실행: 이 폴더에서  uvicorn ex01_predict_simple:app --reload
# 확인: 브라우저에서 http://127.0.0.1:8000 (예측 화면) 또는 http://127.0.0.1:8000/docs
from pathlib import Path

import numpy as np
from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field

from model_core import PassModel             # 2·3절에서 만든 모델 클래스

HERE = Path(__file__).parent

# ① 서버가 켜질 때(이 파일을 불러올 때) 모델을 딱 한 번 불러 둬요 — 요청마다 불러오면 느려요
model = PassModel.load(HERE / "model" / "pass_model.npz")

app = FastAPI(title="합격 예측 API (간단 버전)")


# ② 입력 모양: 공부·수면·휴대폰 시간 (2장의 Field 로 범위 검사)
class Student(BaseModel):
    study_h: float = Field(ge=0, le=16, examples=[4.5])     # 하루 공부 시간
    sleep_h: float = Field(ge=0, le=16, examples=[7.0])     # 하루 수면 시간
    phone_h: float = Field(ge=0, le=24, examples=[2.0])     # 하루 휴대폰 시간


# ③ 예측 API: 받은 값 → 모델이 원하는 배열 [[공부, 수면, 휴대폰]] → 확률 → JSON
@app.post("/predict")
def predict(student: Student):
    x = np.array([[student.study_h, student.sleep_h, student.phone_h]])   # 학습 때와 같은 순서
    p = float(model.predict_proba(x)[0])                                  # 0 ~ 1 사이 합격 확률
    return {"pass_probability": round(p, 3), "label": "합격" if p >= 0.5 else "불합격"}


# ④ 예측 화면: 3장 6-3단계처럼 입력 칸 → POST 를 보내는 HTML 페이지
@app.get("/", include_in_schema=False)
def page():
    return FileResponse(HERE / "predict_page.html")
