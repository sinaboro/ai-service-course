# 2장 예제 1: POST 로 데이터 받기 — 회원 가입
# 실행: 이 폴더에서  uvicorn ex01_post:app --reload
# 확인: POST 는 주소창으로 보낼 수 없어요 → http://127.0.0.1:8000/docs 의 Try it out 으로 시험해요
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# 받을 데이터의 "모양" 정하기 — 이름은 글자, 나이는 정수
# BaseModel 을 물려받아 클래스를 만들면, 들어온 JSON 을 이 모양대로 검사해 줘요
class Member(BaseModel):
    name: str
    age: int


# @app.post: POST 요청을 받는 창구. 본문(JSON)이 member 로 들어와요
@app.post("/join")
def join(member: Member):
    return {"message": f"{member.name}님, 가입을 환영해요!", "age_next_year": member.age + 1}
