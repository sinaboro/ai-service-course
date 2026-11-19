# 문제 3. 문제 2의 API에 height=abc를 보내면 상태 코드가 무엇인지 출력하세요.

from fastapi import FastAPI
from fastapi.testclient import TestClient  # 서버를 켜지 않고 코드로 요청을 보내는 도구

app = FastAPI()  # 앱(서버) 만들기 — uvicorn 이 이 app 을 실행해요


@app.get("/bmi")
def bmi(height: float, weight: float):
    return {"bmi": round(weight / (height / 100) ** 2, 1)}


client = TestClient(app)  # app 에 요청을 보내는 "코드 속 브라우저"
print(client.get("/bmi?height=abc&weight=70").status_code)
