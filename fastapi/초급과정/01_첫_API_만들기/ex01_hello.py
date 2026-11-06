# 1장 예제 1: 주소(창구) 여러 개 만들기
# 실행: 이 폴더에서  uvicorn ex01_hello:app --reload
# 확인: 브라우저에서 http://127.0.0.1:8000 , /hello , /about 을 차례로 열어 보세요
from fastapi import FastAPI

app = FastAPI()                       # 서버(앱) 만들기. 이름은 보통 app 이라고 지어요


# 주소 "/" → 첫 화면
@app.get("/")
def home():
    return {"message": "환영합니다! /hello 와 /about 도 열어 보세요"}


# 주소 "/hello" → 인사
@app.get("/hello")
def hello():
    return {"message": "안녕하세요!"}


# 주소 "/about" → 자기소개 (값을 여러 개 담아도 돼요)
@app.get("/about")
def about():
    return {"name": "홍길동", "age": 20, "hobby": ["축구", "게임"]}
