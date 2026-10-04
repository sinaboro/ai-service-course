import json
from fastapi.testclient import TestClient
from ex02_field import app            # 같은 폴더의 앱 파일에서 app 가져오기

client = TestClient(app)              # 서버를 띄우지 않고 요청을 보내 볼 수 있는 도구


def show(title, res):
    print(f"[{title}] {res.request.method} {res.request.url.path} → {res.status_code}")
    try:
        print(json.dumps(res.json(), ensure_ascii=False, indent=2))
    except ValueError:
        print(res.text)
    print()

good = {"area": 84.5, "rooms": 3, "built_year": 2015, "region": "서울"}
show("정상", client.post("/houses/check", json=good))
show("면적 0", client.post("/houses/check", json={**good, "area": 0}))
show("없는 지역", client.post("/houses/check", json={**good, "region": "제주"}))
show("여러 개가 틀림", client.post("/houses/check", json={"area": -1, "rooms": 20, "built_year": 1900}))
