# 가장 작은 웹 서버 — 브라우저로 접속해 보기 (서버로 실행)
# 실행: 이 폴더에서  uvicorn ex03_first_server:app --reload
# 확인: 브라우저 주소창에  http://127.0.0.1:8000  과  http://127.0.0.1:8000/time  입력
# 끄기: 서버를 켠 터미널에서 Ctrl + C
from datetime import datetime

from fastapi import FastAPI

app = FastAPI()                                # 서버(앱) 하나 만들기


@app.get("/")                                  # 주소 "/" 로 들어오면
def home():
    return {"message": "제 첫 웹 서버예요!"}     # 이 딕셔너리가 JSON 으로 브라우저에 보여요


@app.get("/time")                              # 주소 "/time" 으로 들어오면
def now():
    # 요청이 올 때마다 함수가 다시 실행되므로 새로고침할 때마다 시각이 바뀌어요
    return {"now": datetime.now().strftime("%H:%M:%S")}
