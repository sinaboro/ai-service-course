# 6장 예제 2: AI 예측 웹 서비스 — 예측 API + 예측 화면
# 실행: 이 폴더에서  uvicorn ex02_predict_app:app --reload
# 확인: 브라우저에서 http://127.0.0.1:8000 (예측 화면) 또는 /docs
from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field

from ai_model import predict                  # 예제 1에서 써 본 그 함수

app = FastAPI(title="합격 예측 서비스")
HERE = Path(__file__).parent


# 받을 값의 모양과 범위 (2장) — 하루는 24시간이니 그 안의 값만 받아요
class Student(BaseModel):
    study_h: float = Field(ge=0, le=16)       # 공부 시간
    sleep_h: float = Field(ge=0, le=16)       # 수면 시간
    phone_h: float = Field(ge=0, le=24)       # 휴대폰 시간


# 예측 API: 받은 값을 AI 함수에 넣고 결과를 JSON 으로 (2장의 커피 주문과 같은 모양!)
@app.post("/predict")
def predict_api(s: Student):
    p = predict(s.study_h, s.sleep_h, s.phone_h)
    return {"probability": round(p, 3), "label": "합격" if p >= 0.5 else "불합격"}


# 예측 화면 (4장 3단계와 같은 방법)
@app.get("/", include_in_schema=False)
def page():
    return FileResponse(HERE / "predict_page.html")
