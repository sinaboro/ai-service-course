# 문제 1. 공부 시간 0 ~ 8시간(1시간 간격)일 때의 합격 확률을 GET /table 로 한꺼번에 돌려주세요.
#        수면 7시간, 휴대폰 2시간으로 고정해요.
#        예) /table → [{"study_h": 0, "probability": 1.1}, {"study_h": 1, ...}, ...]   (확률은 % 로)
# 실행: 장 폴더(06_AI_맛보기)에서  uvicorn 연습문제_정답.문제1:app --reload  →  /table
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))   # 장 폴더의 ai_model.py 를 찾을 수 있게
from fastapi import FastAPI

from ai_model import predict

app = FastAPI()


@app.get("/table")
def table():
    return [{"study_h": h, "probability": round(predict(h, 7, 2) * 100, 1)} for h in range(0, 9)]
