# 문제 1. tests/test_api.py에 "/predict 응답에 pass_probability, label, model_version 세 키가 모두 있는지" 검사하는 테스트 함수를 추가한다고 생각하고, 같은 내용을 아래처럼 TestClient로 직접 확인해 보세요.

import sys
sys.path.insert(0, "serving_project")             # 프로젝트 폴더를 import 경로에
import os
os.environ["MODEL_PATH"] = "serving_project/model/pass_model.npz"

from fastapi.testclient import TestClient
from app.main import create_app

with TestClient(create_app()) as client:
    body = client.post("/predict", json={"study_h": 3, "sleep_h": 7, "phone_h": 2}).json()
    print("키 확인:", {"pass_probability", "label", "model_version"} <= set(body))
    print(sorted(body))
