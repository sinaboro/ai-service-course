import json
from fastapi.testclient import TestClient
from ex04_custom_validator import app            # 같은 폴더의 앱 파일에서 app 가져오기

client = TestClient(app)              # 서버를 띄우지 않고 요청을 보내 볼 수 있는 도구


def show(title, res):
    print(f"[{title}] {res.request.method} {res.request.url.path} → {res.status_code}")
    try:
        print(json.dumps(res.json(), ensure_ascii=False, indent=2))
    except ValueError:
        print(res.text)
    print()

show("정상", client.post("/features", json={"values": [5.123, 3.5, 1.4, 0.2]}))
show("음수 포함", client.post("/features", json={"values": [5.1, -3.5, 1.4, 0.2]}))
show("개수 부족", client.post("/features", json={"values": [5.1, 3.5]}))
show("범위 정상", client.post("/range", json={"start": 3, "end": 10}))
show("순서 반대", client.post("/range", json={"start": 10, "end": 3}))
