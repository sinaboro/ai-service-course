# 문제 1. tests/test_api.py에 "/predict 응답에 pass_probability, label, model_version 세 키가 모두 있는지" 검사하는 테스트 함수를 추가한다고 생각하고, 같은 내용을 아래처럼 TestClient로 직접 확인해 보세요.

# 정답 폴더(연습문제_정답)에서 실행해도 되도록, 경로를 이 파일 기준으로 만들어요
import os                                                    # 환경 변수 · 경로 같은 운영체제 기능
import sys                                                   # 파이썬 실행 환경 (import 경로 sys.path 등)
from pathlib import Path                                     # 파일 · 폴더 경로를 다루는 도구
PROJECT = Path(__file__).parent.parent / "serving_project"   # 07 장 폴더 안의 serving_project
sys.path.insert(0, str(PROJECT))                  # "from app.main import ..." 가 app 폴더를 찾을 수 있게
os.environ["MODEL_PATH"] = str(PROJECT / "model" / "pass_model.npz")   # 앱을 불러오기 "전에" 설정

from fastapi.testclient import TestClient                    # 서버를 켜지 않고 코드로 요청을 보내는 도구
from app.main import create_app

with TestClient(create_app()) as client:
    body = client.post("/predict", json={"study_h": 3, "sleep_h": 7, "phone_h": 2}).json()
    print("키 확인:", {"pass_probability", "label", "model_version"} <= set(body))
    print(sorted(body))
