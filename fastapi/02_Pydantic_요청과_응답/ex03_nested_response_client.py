import json
from fastapi.testclient import TestClient
from ex03_nested_response import app            # 같은 폴더의 앱 파일에서 app 가져오기

client = TestClient(app)              # 서버를 띄우지 않고 요청을 보내 볼 수 있는 도구


def show(title, res):
    print(f"[{title}] {res.request.method} {res.request.url.path} → {res.status_code}")
    try:
        print(json.dumps(res.json(), ensure_ascii=False, indent=2))
    except ValueError:
        print(res.text)
    print()

order = {"customer": "kim", "coupon": "WELCOME",
         "items": [{"name": "마우스", "price": 15000, "qty": 2}, {"name": "패드", "price": 5000}]}
show("중첩 주문", client.post("/orders", json=order))
show("빈 주문", client.post("/orders", json={"customer": "lee", "items": []}))
show("가입 (비밀번호는 응답에서 빠짐)", client.post("/users", json={"username": "hong", "password": "secret1234"}))
show("짧은 비밀번호", client.post("/users", json={"username": "hong", "password": "123"}))
