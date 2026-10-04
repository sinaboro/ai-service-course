# 클라이언트 예제: 앱(ex04_custom_validator.py)에 실제로 요청을 보내고 응답을 출력해요 (python 으로 실행)
import json                           # 응답(JSON)을 보기 좋게 출력할 때 사용
from fastapi.testclient import TestClient
from ex04_custom_validator import app            # 같은 폴더의 앱 파일에서 app 가져오기

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

show("정상", client.post("/features", json={"values": [5.123, 3.5, 1.4, 0.2]}))
# 직접 만든 검사 규칙에 걸리는 요청들
show("음수 포함", client.post("/features", json={"values": [5.1, -3.5, 1.4, 0.2]}))
show("개수 부족", client.post("/features", json={"values": [5.1, 3.5]}))
show("범위 정상", client.post("/range", json={"start": 3, "end": 10}))
show("순서 반대", client.post("/range", json={"start": 10, "end": 3}))
