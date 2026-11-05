# 문제 2. ex03_first_server.py 를 참고해 GET /about 에 {"name": 내 이름, "course": "FastAPI"} 를
#        돌려주는 서버를 만들고, 브라우저(또는 TestClient)로 확인하세요.
from fastapi import FastAPI
from fastapi.testclient import TestClient

app = FastAPI()


@app.get("/about")
def about():
    return {"name": "홍길동", "course": "FastAPI"}


# 서버로 켤 때:  uvicorn 문제2:app --reload  →  브라우저에서 http://127.0.0.1:8000/about
# 여기서는 바로 확인할 수 있게 TestClient 로 요청을 보내요
client = TestClient(app)
print(client.get("/about").json())
