# 6-2단계: 버튼을 누르면 자바스크립트가 API 를 부르기 + 동기/비동기 체험 (서버로 실행)
# 실행: 이 폴더에서  uvicorn ex03_step2_fetch:app --reload
# 확인: 브라우저에서 http://127.0.0.1:8000 → 버튼들을 눌러 보세요
import time
from datetime import datetime
from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()
HERE = Path(__file__).parent


# 바로 대답하는 API: 지금 시각
@app.get("/api/time")
def get_time():
    return {"now": datetime.now().strftime("%H:%M:%S")}


# 이름을 쿼리로 받아 인사하는 API (1장의 쿼리 매개변수와 같아요)
@app.get("/api/hello")
def hello(name: str = "손님"):
    return {"message": f"{name}님, 반가워요!"}


# 일부러 느리게 대답하는 API: 모델 예측·데이터베이스처럼 "시간이 걸리는 일" 을 흉내 내요
# seconds 쿼리로 기다릴 시간을 정해요 (0 ~ 5초)
@app.get("/api/slow")
def slow(seconds: float = 2.0):
    seconds = max(0.0, min(seconds, 5.0))
    time.sleep(seconds)                        # 서버 쪽에서 기다리는 시간
    return {"message": f"{seconds}초 걸리는 일을 마쳤어요", "finished": datetime.now().strftime("%H:%M:%S")}


@app.get("/", include_in_schema=False)
def page():
    return FileResponse(HERE / "step2_page.html")
