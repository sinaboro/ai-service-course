# 문제 1. 쿼리 lang(기본 "ko")을 읽는 의존성 get_lang을 만들고, /hello와 /bye 두 API가 이를 함께 써서 언어별 인사를 돌려주게 하세요.

from typing import Annotated
from fastapi import Depends, FastAPI
from fastapi.testclient import TestClient

app = FastAPI()


def get_lang(lang: str = "ko") -> str:
    return lang if lang in ("ko", "en") else "ko"


Lang = Annotated[str, Depends(get_lang)]


@app.get("/hello")
def hello(lang: Lang):
    return {"msg": "안녕하세요" if lang == "ko" else "Hello"}


@app.get("/bye")
def bye(lang: Lang):
    return {"msg": "안녕히 가세요" if lang == "ko" else "Goodbye"}


client = TestClient(app)
print(client.get("/hello").json())
print(client.get("/bye?lang=en").json())
