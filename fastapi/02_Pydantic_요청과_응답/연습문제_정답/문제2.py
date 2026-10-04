# 문제 2. PredictRequest(값 3개짜리 features: list[float])를 받아 PredictResponse(total: float, label: str)로 응답하는 POST /predict를 만드세요. 합이 10 이상이면 label "high", 아니면 "low".

from fastapi import FastAPI
from fastapi.testclient import TestClient
from pydantic import BaseModel, Field

app = FastAPI()


class PredictRequest(BaseModel):
    features: list[float] = Field(min_length=3, max_length=3)


class PredictResponse(BaseModel):
    total: float
    label: str


@app.post("/predict", response_model=PredictResponse)
def predict(req: PredictRequest):
    total = sum(req.features)
    return {"total": total, "label": "high" if total >= 10 else "low"}


client = TestClient(app)
print(client.post("/predict", json={"features": [3, 4, 5]}).json())
