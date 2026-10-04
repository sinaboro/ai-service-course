import json
from fastapi.testclient import TestClient
from ex01_hello import app            # 같은 폴더의 앱 파일에서 app 가져오기

client = TestClient(app)              # 서버를 띄우지 않고 요청을 보내 볼 수 있는 도구


def show(title, res):
    print(f"[{title}] {res.request.method} {res.request.url.path} → {res.status_code}")
    try:
        print(json.dumps(res.json(), ensure_ascii=False, indent=2))
    except ValueError:
        print(res.text)
    print()

show("루트", client.get("/"))
show("인사", client.get("/hello/홍길동"))
show("상태 확인", client.get("/health"))
show("없는 주소", client.get("/nothing"))
