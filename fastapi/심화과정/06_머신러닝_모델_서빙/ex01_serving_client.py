import json
from fastapi.testclient import TestClient
from ex01_serving_app import app


# 요청 · 응답을 출력하는 도우미
def show(title, res):
    print(f"[{title}] {res.request.method} {res.request.url.path} → {res.status_code}")
    print(json.dumps(res.json(), ensure_ascii=False, indent=2))
    print()


with TestClient(app) as client:                         # lifespan 실행 (모델 불러오기)
    show("상태", client.get("/health"))
    show("모델 정보", client.get("/model/info"))
    show("열심히 하는 학생", client.post("/predict", json={"study_h": 5, "sleep_h": 6.5, "phone_h": 1}))
    show("휴대폰을 많이 하는 학생", client.post("/predict", json={"study_h": 0.5, "sleep_h": 8.5, "phone_h": 6}))
    # -1 과 "많이" 는 검사에 걸려 422
    show("잘못된 입력", client.post("/predict", json={"study_h": -1, "sleep_h": 7, "phone_h": "많이"}))
    # 공부 시간만 1 ~ 4 시간으로 바꾼 학생 4명
    batch = {"students": [{"study_h": h, "sleep_h": 7, "phone_h": 2} for h in [1, 2, 3, 4]]}
    show("여러 명 한 번에", client.post("/predict/batch", json=batch))
    print("지금까지 예측 수:", client.get("/model/info").json()["predictions_served"])
