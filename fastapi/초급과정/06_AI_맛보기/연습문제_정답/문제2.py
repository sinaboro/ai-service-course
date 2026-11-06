# 문제 2. 예측 결과에 조언(advice)을 붙여 주세요.
#        합격 확률 50% 미만 → "공부 시간을 조금 늘려 보세요", 80% 이상 → "지금처럼만 하세요!", 그 사이 → "조금만 더 힘내요"
# 실행: 장 폴더(06_AI_맛보기)에서  uvicorn 연습문제_정답.문제2:app --reload  →  /docs 에서 POST /predict
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))   # 장 폴더의 ai_model.py 를 찾을 수 있게
from fastapi import FastAPI
from pydantic import BaseModel, Field

from ai_model import predict

app = FastAPI()


class Student(BaseModel):
    study_h: float = Field(ge=0, le=16)
    sleep_h: float = Field(ge=0, le=16)
    phone_h: float = Field(ge=0, le=24)


@app.post("/predict")
def predict_api(s: Student):
    p = predict(s.study_h, s.sleep_h, s.phone_h)
    if p < 0.5:
        advice = "공부 시간을 조금 늘려 보세요"
    elif p >= 0.8:
        advice = "지금처럼만 하세요!"
    else:
        advice = "조금만 더 힘내요"
    return {"probability": round(p, 3), "advice": advice}
