# ex02_missing_model_client.py : 모델 파일이 없을 때 서버가 꺼지지 않고 503 으로 알려 주는지 확인
# 실행: python ex02_missing_model_client.py
import os                                         # 환경 변수 · 경로 같은 운영체제 기능
os.environ["MODEL_PATH"] = "model/없는_모델.npz"      # 일부러 없는 경로 (앱을 불러오기 전에!)

from fastapi.testclient import TestClient         # 서버를 켜지 않고 코드로 요청을 보내는 도구
from ex01_serving_app import app

# 모델이 없으면: /health 는 model_loaded False, /predict 는 503
with TestClient(app) as client:
    print(client.get("/health").json())
    res = client.post("/predict", json={"study_h": 3, "sleep_h": 7, "phone_h": 2})
    print(res.status_code, res.json())
