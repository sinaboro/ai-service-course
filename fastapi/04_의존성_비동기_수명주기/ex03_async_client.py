import json
from fastapi.testclient import TestClient
from ex03_async import app            # 같은 폴더의 앱 파일에서 app 가져오기

client = TestClient(app)              # 서버를 띄우지 않고 요청을 보내 볼 수 있는 도구


def show(title, res):
    print(f"[{title}] {res.request.method} {res.request.url.path} → {res.status_code}")
    try:
        print(json.dumps(res.json(), ensure_ascii=False, indent=2))
    except ValueError:
        print(res.text)
    print()

show("일반 함수", client.get("/sync"))
show("비동기 함수", client.get("/async"))
show("세 가지를 동시에 기다리기", client.get("/gather"))
