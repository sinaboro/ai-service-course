# 문제 2. ex03_first_server.py 를 참고해 GET /about 에 {"name": 내 이름, "course": "FastAPI"} 를
#        돌려주는 서버를 만들고, 브라우저로 확인하세요.
# 실행: 정답 폴더에서  uvicorn 문제2:app --reload  →  브라우저에서 http://127.0.0.1:8000/about
from fastapi import FastAPI

app = FastAPI()


@app.get("/about")
def about():
    return {"name": "홍길동", "course": "FastAPI"}
