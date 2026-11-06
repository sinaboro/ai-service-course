# 4장 3단계: 입력 칸에 적은 값을 POST 로 보내고, 결과·오류를 화면에 보여 주기 (서버로 실행)
# 실행: 이 폴더에서  uvicorn ex03_post:app --reload
# 확인: 브라우저에서 http://127.0.0.1:8000 → 이름과 점수를 넣고 [학점 계산] (점수 150 도 넣어 보세요)
from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field

app = FastAPI()
HERE = Path(__file__).parent


# 2장에서 배운 Pydantic 모델: 화면에서 보낸 JSON 의 모양과 규칙
class ScoreIn(BaseModel):
    name: str = Field(min_length=1, max_length=20)    # 이름: 1 ~ 20글자
    score: int = Field(ge=0, le=100)                  # 점수: 0 ~ 100


# POST /api/grade: 본문 JSON {"name": ..., "score": ...} → 학점 계산
@app.post("/api/grade")
def grade(data: ScoreIn):
    if data.score >= 90:
        letter = "A"
    elif data.score >= 80:
        letter = "B"
    elif data.score >= 70:
        letter = "C"
    else:
        letter = "F"
    return {"name": data.name, "score": data.score, "grade": letter}


@app.get("/", include_in_schema=False)
def page():
    return FileResponse(HERE / "page3.html")
