import json
from fastapi.testclient import TestClient
from ex02_api_key import app            # 같은 폴더의 앱 파일에서 app 가져오기

client = TestClient(app)              # 서버를 띄우지 않고 요청을 보내 볼 수 있는 도구


def show(title, res):
    print(f"[{title}] {res.request.method} {res.request.url.path} → {res.status_code}")
    try:
        print(json.dumps(res.json(), ensure_ascii=False, indent=2))
    except ValueError:
        print(res.text)
    print()

show("공개 API", client.get("/public"))
show("키 없음", client.post("/predict"))
show("틀린 키", client.post("/predict", headers={"X-API-Key": "wrong"}))
show("올바른 키", client.post("/predict", headers={"X-API-Key": "team-a-123"}))
