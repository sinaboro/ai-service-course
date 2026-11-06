# 문제 2. GET /bmi?height=175&weight=70처럼 키(cm)와 몸무게(kg)를 쿼리로 받아 BMI(소수 1자리)를 돌려주는 API를 만드세요. (BMI = 몸무게 ÷ (키/100)²)

from fastapi import FastAPI
from fastapi.testclient import TestClient

app = FastAPI()


@app.get("/bmi")
def bmi(height: float, weight: float):
    value = weight / (height / 100) ** 2
    return {"height": height, "weight": weight, "bmi": round(value, 1)}


client = TestClient(app)
print(client.get("/bmi", params={"height": 175, "weight": 70}).json())
