import json
from fastapi.testclient import TestClient
from ex02_main import app            # 같은 폴더의 앱 파일에서 app 가져오기

client = TestClient(app)              # 서버를 띄우지 않고 요청을 보내 볼 수 있는 도구


def show(title, res):
    print(f"[{title}] {res.request.method} {res.request.url.path} → {res.status_code}")
    try:
        print(json.dumps(res.json(), ensure_ascii=False, indent=2))
    except ValueError:
        print(res.text)
    print()

show("등록된 주소", client.get("/"))
show("상품 목록", client.get("/items"))
show("상품 하나", client.get("/items/2"))
show("없는 상품", client.get("/items/9"))
show("모델 목록", client.get("/models"))
