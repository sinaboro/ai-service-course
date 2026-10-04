import json
from fastapi.testclient import TestClient
from ex02_path_query import app            # 같은 폴더의 앱 파일에서 app 가져오기

client = TestClient(app)              # 서버를 띄우지 않고 요청을 보내 볼 수 있는 도구


def show(title, res):
    print(f"[{title}] {res.request.method} {res.request.url.path} → {res.status_code}")
    try:
        print(json.dumps(res.json(), ensure_ascii=False, indent=2))
    except ValueError:
        print(res.text)
    print()

show("경로 매개변수", client.get("/items/3"))
show("쿼리 기본값", client.get("/items"))
show("쿼리 지정", client.get("/items", params={"skip": 1, "limit": 2}))
show("검색", client.get("/items?keyword=마"))
show("계산", client.get("/calc/add?a=3&b=4.5"))
show("숫자가 아닌 id", client.get("/items/abc"))
show("필수 쿼리 빠짐", client.get("/calc/add?a=3"))
