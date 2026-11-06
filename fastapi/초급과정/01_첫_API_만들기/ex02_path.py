# 1장 예제 2: 경로 매개변수 — 주소 안에 값을 넣어 보내기
# 실행: 이 폴더에서  uvicorn ex02_path:app --reload
# 확인: /menu/1 , /menu/3 , /menu/9 , /square/7 , /menu/abc 를 열어 보세요
from fastapi import FastAPI

app = FastAPI()

# 식당 메뉴판: 번호 → 메뉴 이름
MENU = {1: "김치찌개", 2: "된장찌개", 3: "비빔밥"}


# {number} 자리에 들어온 값이 함수의 number 로 들어와요
# number: int  ← "정수로 받을게요" 라는 표시. 주소의 "3"(글자)을 3(숫자)으로 바꿔 줘요
@app.get("/menu/{number}")
def menu(number: int):
    if number in MENU:
        return {"number": number, "food": MENU[number]}
    return {"number": number, "food": "없는 메뉴예요"}


# 숫자를 받아 제곱을 돌려주기 — /square/7 → 49
@app.get("/square/{n}")
def square(n: int):
    return {"n": n, "square": n * n}
