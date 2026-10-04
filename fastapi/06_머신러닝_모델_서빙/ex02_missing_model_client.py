import os
os.environ["MODEL_PATH"] = "model/없는_모델.npz"      # 일부러 없는 경로 (앱을 불러오기 전에!)

from fastapi.testclient import TestClient
from ex01_serving_app import app

with TestClient(app) as client:
    print(client.get("/health").json())
    res = client.post("/predict", json={"study_h": 3, "sleep_h": 7, "phone_h": 2})
    print(res.status_code, res.json())
