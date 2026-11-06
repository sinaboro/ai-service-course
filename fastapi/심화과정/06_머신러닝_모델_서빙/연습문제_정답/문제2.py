# 문제 2. ex01_serving_app의 /predict/batch에 공부 시간 0, 2, 4, 6시간(수면 7, 휴대폰 2)인 4명을 보내, 공부 시간과 합격 확률을 표처럼 출력하세요.

# 정답 폴더에서 실행해도 되도록: 장 폴더(06_...)를 import 경로와 작업 폴더로 지정
import os
import sys
CHAPTER = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, CHAPTER)                      # model_core, ex01_serving_app 을 찾을 수 있게
os.chdir(CHAPTER)                                # "model/pass_model.npz" 같은 상대 경로가 맞도록

from fastapi.testclient import TestClient
from ex01_serving_app import app

hours = [0, 2, 4, 6]
with TestClient(app) as client:
    body = {"students": [{"study_h": h, "sleep_h": 7, "phone_h": 2} for h in hours]}
    preds = client.post("/predict/batch", json=body).json()["predictions"]
for h, p in zip(hours, preds):
    print(f"공부 {h}시간 → {p['pass_probability']:.1%} ({p['label']})")
