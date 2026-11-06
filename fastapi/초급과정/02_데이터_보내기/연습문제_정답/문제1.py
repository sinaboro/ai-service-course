# 문제 1. 이름과 국어·영어·수학 점수를 POST /score 로 받아 총점과 평균(소수 1자리)을 돌려주세요.
#        점수는 0 ~ 100 만 받도록 Field 로 규칙을 정하세요.
#        예) {"name": "영희", "kor": 90, "eng": 85, "math": 70} → {"name": "영희", "total": 245, "average": 81.7}
# 실행: 이 폴더에서  uvicorn 문제1:app --reload  →  /docs 에서 시험
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class Score(BaseModel):
    name: str
    kor: int = Field(ge=0, le=100)
    eng: int = Field(ge=0, le=100)
    math: int = Field(ge=0, le=100)


@app.post("/score")
def score(s: Score):
    total = s.kor + s.eng + s.math
    return {"name": s.name, "total": total, "average": round(total / 3, 1)}
