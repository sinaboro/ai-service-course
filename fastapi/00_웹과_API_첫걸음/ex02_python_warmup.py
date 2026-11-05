# FastAPI 코드를 읽기 위한 파이썬 문법 미리보기 (python 으로 실행)
# FastAPI 예제에는 아래 다섯 가지가 계속 나와요. 여기서 먼저 익숙해져요.

# ── 1) 타입 힌트: "이 변수에는 이런 값이 들어와요" 라는 표시 ──
# FastAPI 는 이 표시를 보고 들어온 값을 자동으로 바꾸고(변환) 검사해요.
def add(a: int, b: int) -> int:                # a, b 는 정수, 돌려주는 값도 정수
    return a + b

print("1) add(3, 4) =", add(3, 4))

# ── 2) 기본값이 있는 매개변수: 안 보내면 기본값을 써요 ──
# FastAPI 에서는 "기본값이 있으면 선택, 없으면 필수" 쿼리가 돼요.
def greet(name: str, lang: str = "ko") -> str:
    if lang == "en":
        return f"Hello, {name}!"
    return f"{name}님, 안녕하세요!"            # f-문자열: {} 안의 변수 값이 들어가요

print("2)", greet("철수"), "/", greet("Tom", lang="en"))

# ── 3) None 이 될 수 있는 값: str | None ──
# "글자이거나, 아예 없을 수도 있어요" 라는 뜻 (Python 3.10 이상 문법)
def search(keyword: str | None = None) -> str:
    if keyword is None:
        return "전체 목록"
    return f"'{keyword}' 검색 결과"

print("3)", search(), "/", search("마우스"))

# ── 4) 데코레이터 @: 함수 위에 붙이는 "등록 스티커" ──
# FastAPI 의 @app.get("/주소") 는 "이 주소로 요청이 오면 아래 함수를 실행해 줘" 라고 등록하는 스티커예요.
# 아래는 그 원리를 아주 작게 흉내 낸 것이에요. (내부 동작은 몰라도 사용하는 데 문제없어요)
ROUTES = {}                                    # 주소 → 함수 를 적어 두는 장부


def route(path):                               # route("/hello") 가 스티커를 만들어 줘요
    def sticker(func):
        ROUTES[path] = func                    # 장부에 등록
        return func
    return sticker


@route("/hello")                               # ← FastAPI 의 @app.get("/hello") 와 같은 모양
def hello():
    return {"message": "안녕하세요"}


@route("/health")
def health():
    return {"status": "ok"}


print("4) 등록된 주소:", list(ROUTES))
print("   '/hello' 로 요청이 왔다고 치면 →", ROUTES["/hello"]())

# ── 5) import: 다른 파일(모듈)의 것을 가져와 쓰기 ──
# from fastapi import FastAPI  ← "fastapi 라는 설치된 묶음에서 FastAPI 를 가져와요"
from datetime import date
print("5) date 를 가져와서 쓰기:", date(2026, 3, 2).strftime("%Y년 %m월 %d일"))   # 설치 없이 쓰는 표준 모듈
