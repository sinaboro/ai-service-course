# 클라이언트 예제: 앱(ex02_field.py)에 실제로 요청을 보내고 응답을 출력해요 (python 으로 실행)
import json                           # 응답(JSON)을 보기 좋게 출력할 때 사용
from fastapi.testclient import TestClient
from ex02_field import app            # 같은 폴더의 앱 파일에서 app 가져오기

client = TestClient(app)              # 서버를 띄우지 않고 요청을 보내 볼 수 있는 도구


# show(제목, 응답): 요청 방식 · 주소 · 상태 코드와 응답 내용을 출력하는 도우미 함수
def show(title, res):
    print(f"[{title}] {res.request.method} {res.request.url.path} → {res.status_code}")
    # 응답 본문이 JSON 이면 들여쓰기해서 출력 (ensure_ascii=False: 한글을 그대로)
    try:
        print(json.dumps(res.json(), ensure_ascii=False, indent=2))
    # JSON 이 아니면(글자 응답 등) 그대로 출력
    except ValueError:
        print(res.text)
    print()

# 정상 입력을 하나 만들어 두고, {**good, "area": 0} 처럼 일부만 바꿔서 시험
good = {"area": 84.5, "rooms": 3, "built_year": 2015, "region": "서울"}
show("정상", client.post("/houses/check", json=good))
show("면적 0", client.post("/houses/check", json={**good, "area": 0}))
show("없는 지역", client.post("/houses/check", json={**good, "region": "제주"}))
# 여러 값이 동시에 틀리면 오류 목록에 모두 나와요
show("여러 개가 틀림", client.post("/houses/check", json={"area": -1, "rooms": 20, "built_year": 1900}))
