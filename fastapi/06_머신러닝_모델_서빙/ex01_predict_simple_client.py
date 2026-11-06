# 클라이언트 예제: 간단한 예측 API 에 요청을 보내 봐요 (python 으로 실행)
from fastapi.testclient import TestClient

from ex01_predict_simple import app

client = TestClient(app)

# 공부 시간만 바꿔 가며 세 학생을 예측해 보기 (수면 7시간, 휴대폰 2시간은 같게)
for study in [1, 3, 5]:
    res = client.post("/predict", json={"study_h": study, "sleep_h": 7, "phone_h": 2})
    print(f"공부 {study}시간 → {res.status_code} {res.json()}")

# 범위를 벗어난 값(공부 20시간)은 Pydantic 이 422 로 막아요
res = client.post("/predict", json={"study_h": 20, "sleep_h": 7, "phone_h": 2})
print("공부 20시간 →", res.status_code, res.json()["detail"][0]["msg"])

# "/" 는 예측 화면(HTML)
print("화면:", client.get("/").headers["content-type"])
