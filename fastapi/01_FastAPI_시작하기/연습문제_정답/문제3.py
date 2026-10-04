# 문제 3. 문제 2의 API에 height=abc를 보내면 상태 코드가 무엇인지 출력하세요.

from fastapi import FastAPI
from fastapi.testclient import TestClient

app = FastAPI()


@app.get("/bmi")
def bmi(height: float, weight: float):
    return {"bmi": round(weight / (height / 100) ** 2, 1)}


client = TestClient(app)
print(client.get("/bmi?height=abc&weight=70").status_code)
