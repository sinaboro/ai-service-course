import json
from fastapi.testclient import TestClient
from ex01_depends import app            # 같은 폴더의 앱 파일에서 app 가져오기

client = TestClient(app)              # 서버를 띄우지 않고 요청을 보내 볼 수 있는 도구


def show(title, res):
    print(f"[{title}] {res.request.method} {res.request.url.path} → {res.status_code}")
    try:
        print(json.dumps(res.json(), ensure_ascii=False, indent=2))
    except ValueError:
        print(res.text)
    print()

show("기본값", client.get("/numbers"))
show("페이지 지정", client.get("/squares?skip=10&limit=3"))
show("limit 범위 초과", client.get("/numbers?limit=100"))
