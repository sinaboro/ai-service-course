import pytest
from fastapi.testclient import TestClient

from app.main import create_app

# 시험용 입력: 합격할 학생(GOOD), 불합격할 학생(BAD)
GOOD = {"study_h": 5, "sleep_h": 6.5, "phone_h": 1}
BAD = {"study_h": 0.5, "sleep_h": 8.5, "phone_h": 6}


@pytest.fixture
def client():                                   # 테스트마다 새 앱 + lifespan 실행
    with TestClient(create_app()) as c:
        yield c


# 테스트 함수 이름은 test_ 로 시작 / assert 뒤의 조건이 거짓이면 테스트 실패
def test_health(client):
    res = client.get("/health")
    assert res.status_code == 200
    assert res.json() == {"status": "ok", "model_loaded": True}


def test_predict_good_student(client):
    body = client.post("/predict", json=GOOD).json()
    assert body["label"] == "합격"
    assert 0.5 <= body["pass_probability"] <= 1
    assert body["model_version"] == "1.0.0"


def test_predict_bad_student(client):
    assert client.post("/predict", json=BAD).json()["label"] == "불합격"


@pytest.mark.parametrize("field, value", [("study_h", -1), ("sleep_h", 30), ("phone_h", "많이")],
                         ids=["negative", "too_big", "not_number"])
def test_invalid_input_returns_422(client, field, value):     # 같은 테스트를 값 3개로
    res = client.post("/predict", json={**GOOD, field: value})
    assert res.status_code == 422


def test_batch(client):
    res = client.post("/predict/batch", json={"students": [GOOD, BAD, GOOD]})
    assert res.status_code == 200
    assert [p["label"] for p in res.json()["predictions"]] == ["합격", "불합격", "합격"]


# 한 번에 최대 2명으로 설정을 바꿔 413 이 나는지 시험
def test_batch_limit(client, monkeypatch):
    monkeypatch.setattr(client.app.state, "settings", type("S", (), {"max_batch": 2})())
    res = client.post("/predict/batch", json={"students": [GOOD] * 3})
    assert res.status_code == 413


# 모델 파일이 없을 때 503 이 나는지 시험
def test_missing_model_returns_503(monkeypatch):
    monkeypatch.setenv("MODEL_PATH", "no/such/model.npz")       # 환경 변수를 테스트 동안만 바꾸기
    with TestClient(create_app()) as c:
        assert c.get("/health").json()["model_loaded"] is False
        assert c.post("/predict", json=GOOD).status_code == 503
