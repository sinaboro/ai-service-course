# 문제 2. PredictRequest(값 3개짜리 features: list[float])를 받아 PredictResponse(total: float, label: str)로 응답하는 POST /predict를 만드세요. 합이 10 이상이면 label "high", 아니면 "low".

from fastapi import FastAPI
from fastapi.testclient import TestClient  # 서버를 켜지 않고 코드로 요청을 보내는 도구
from pydantic import BaseModel, Field

app = FastAPI()  # 앱(서버) 만들기 — uvicorn 이 이 app 을 실행해요


class PredictRequest(BaseModel):
    features: list[float] = Field(min_length=3, max_length=3)


class PredictResponse(BaseModel):
    total: float
    label: str


@app.post("/predict", response_model=PredictResponse)
def predict(req: PredictRequest):
    total = sum(req.features)
    # 10 이상이면 "high", 아니면 "low"
    return {"total": total, "label": "high" if total >= 10 else "low"}


client = TestClient(app)  # app 에 요청을 보내는 "코드 속 브라우저"
print(client.post("/predict", json={"features": [3, 4, 5]}).json())
