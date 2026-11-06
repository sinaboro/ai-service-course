# 1장 예제 3: 쿼리 매개변수 — 주소 뒤 ? 에 값을 붙여 보내기
# 실행: 이 폴더에서  uvicorn ex03_query:app --reload
# 확인: /add?a=3&b=5 , /greet?name=철수 , /greet?name=Tom&lang=en , /greet , /add?a=3 를 열어 보세요
from fastapi import FastAPI

app = FastAPI()


# 주소에 {} 가 없는 매개변수는 쿼리로 받아요:  /add?a=3&b=5
# 기본값이 없으면 "꼭 보내야 하는 값" 이에요
@app.get("/add")
def add(a: int, b: int):
    return {"a": a, "b": b, "result": a + b}


# 기본값(= "손님", = "ko")이 있으면 안 보내도 돼요
@app.get("/greet")
def greet(name: str = "손님", lang: str = "ko"):
    if lang == "en":
        return {"message": f"Hello, {name}!"}
    return {"message": f"{name}님, 안녕하세요!"}
