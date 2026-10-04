# 문제 2. ex01_serving_app의 /predict/batch에 공부 시간 0, 2, 4, 6시간(수면 7, 휴대폰 2)인 4명을 보내, 공부 시간과 합격 확률을 표처럼 출력하세요.

from fastapi.testclient import TestClient
from ex01_serving_app import app

hours = [0, 2, 4, 6]
with TestClient(app) as client:
    body = {"students": [{"study_h": h, "sleep_h": 7, "phone_h": 2} for h in hours]}
    preds = client.post("/predict/batch", json=body).json()["predictions"]
for h, p in zip(hours, preds):
    print(f"공부 {h}시간 → {p['pass_probability']:.1%} ({p['label']})")
