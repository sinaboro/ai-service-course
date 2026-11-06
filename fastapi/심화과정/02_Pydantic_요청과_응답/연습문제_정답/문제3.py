# 문제 3. Signup 모델에 password와 password_confirm을 받고, 두 값이 다르면 오류가 나도록 model_validator를 만드세요. 다른 값을 보냈을 때 오류 메시지(msg)를 출력하세요.

from fastapi import FastAPI
from fastapi.testclient import TestClient
from pydantic import BaseModel, model_validator

app = FastAPI()


class Signup(BaseModel):
    username: str
    password: str
    password_confirm: str

    @model_validator(mode="after")
    def same_password(self):
        if self.password != self.password_confirm:
            raise ValueError("비밀번호가 서로 달라요")
        return self


@app.post("/signup")
def signup(s: Signup):
    return {"username": s.username}


client = TestClient(app)
res = client.post("/signup", json={"username": "kim", "password": "abc12345", "password_confirm": "abc99999"})
print(res.json()["detail"][0]["msg"])
