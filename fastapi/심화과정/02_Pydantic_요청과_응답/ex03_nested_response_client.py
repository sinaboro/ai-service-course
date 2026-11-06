# 클라이언트 예제: 앱(ex03_nested_response.py)에 실제로 요청을 보내고 응답을 출력해요 (python 으로 실행)
import json                           # 응답(JSON)을 보기 좋게 출력할 때 사용
from fastapi.testclient import TestClient
from ex03_nested_response import app            # 같은 폴더의 앱 파일에서 app 가져오기

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

# 주문 안에 상품 목록(중첩 JSON)
order = {"customer": "kim", "coupon": "WELCOME",
         "items": [{"name": "마우스", "price": 15000, "qty": 2}, {"name": "패드", "price": 5000}]}
show("중첩 주문", client.post("/orders", json=order))
# items 가 비어 있으면 min_length=1 에 걸려 422
show("빈 주문", client.post("/orders", json={"customer": "lee", "items": []}))
show("가입 (비밀번호는 응답에서 빠짐)", client.post("/users", json={"username": "hong", "password": "secret1234"}))
show("짧은 비밀번호", client.post("/users", json={"username": "hong", "password": "123"}))
