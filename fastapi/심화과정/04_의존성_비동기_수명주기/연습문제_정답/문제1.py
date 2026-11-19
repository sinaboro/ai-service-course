# 문제 1. 쿼리 lang(기본 "ko")을 읽는 의존성 get_lang을 만들고, /hello와 /bye 두 API가 이를 함께 써서 언어별 인사를 돌려주게 하세요.

from typing import Annotated  # 타입 힌트에 Depends 같은 정보를 덧붙이는 도구
from fastapi import Depends, FastAPI
from fastapi.testclient import TestClient  # 서버를 켜지 않고 코드로 요청을 보내는 도구

app = FastAPI()  # 앱(서버) 만들기 — uvicorn 이 이 app 을 실행해요


def get_lang(lang: str = "ko") -> str:
    return lang if lang in ("ko", "en") else "ko"  # 모르는 언어면 "ko"


Lang = Annotated[str, Depends(get_lang)]


@app.get("/hello")
def hello(lang: Lang):
    return {"msg": "안녕하세요" if lang == "ko" else "Hello"}


@app.get("/bye")
def bye(lang: Lang):
    return {"msg": "안녕히 가세요" if lang == "ko" else "Goodbye"}


client = TestClient(app)  # app 에 요청을 보내는 "코드 속 브라우저"
print(client.get("/hello").json())
print(client.get("/bye?lang=en").json())
