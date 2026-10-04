import json
from fastapi.testclient import TestClient
from ex01_body import app            # 같은 폴더의 앱 파일에서 app 가져오기

client = TestClient(app)              # 서버를 띄우지 않고 요청을 보내 볼 수 있는 도구


def show(title, res):
    print(f"[{title}] {res.request.method} {res.request.url.path} → {res.status_code}")
    try:
        print(json.dumps(res.json(), ensure_ascii=False, indent=2))
    except ValueError:
        print(res.text)
    print()

show("정상", client.post("/students", json={"name": "홍길동", "age": 20, "score": 85.5}))
show("문자열 숫자도 변환", client.post("/students", json={"name": "이순신", "age": "31", "score": "59"}))
show("나이가 글자", client.post("/students", json={"name": "유관순", "age": "열여덟", "score": 90}))
show("필수 값 빠짐", client.post("/students", json={"name": "강감찬"}))
