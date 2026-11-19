# 문제 3. Signup 모델에 password와 password_confirm을 받고, 두 값이 다르면 오류가 나도록 model_validator를 만드세요. 다른 값을 보냈을 때 오류 메시지(msg)를 출력하세요.

from fastapi import FastAPI
from fastapi.testclient import TestClient  # 서버를 켜지 않고 코드로 요청을 보내는 도구
from pydantic import BaseModel, model_validator

app = FastAPI()  # 앱(서버) 만들기 — uvicorn 이 이 app 을 실행해요


class Signup(BaseModel):
    username: str
    password: str
    password_confirm: str

    @model_validator(mode="after")         # mode="after": 필드 검사가 다 끝난 뒤 모델 전체를 보고 검사
    def same_password(self):
        if self.password != self.password_confirm:
            raise ValueError("비밀번호가 서로 달라요")
        return self


@app.post("/signup")
def signup(s: Signup):
    return {"username": s.username}


client = TestClient(app)  # app 에 요청을 보내는 "코드 속 브라우저"
res = client.post("/signup", json={"username": "kim", "password": "abc12345", "password_confirm": "abc99999"})
print(res.json()["detail"][0]["msg"])
