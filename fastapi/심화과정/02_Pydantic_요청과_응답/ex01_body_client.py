# 클라이언트 예제: 앱(ex01_body.py)에 실제로 요청을 보내고 응답을 출력해요 (python 으로 실행)
import json                           # 응답(JSON)을 보기 좋게 출력할 때 사용
from fastapi.testclient import TestClient
from ex01_body import app            # 같은 폴더의 앱 파일에서 app 가져오기

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

# json= 에 사전을 넣으면 JSON 본문으로 보내요
show("정상", client.post("/students", json={"name": "홍길동", "age": 20, "score": 85.5}))
# "31" 같은 숫자 글자는 int 로 바꿔 줘요
show("문자열 숫자도 변환", client.post("/students", json={"name": "이순신", "age": "31", "score": "59"}))
# 바꿀 수 없는 값, 빠진 값은 422 오류
show("나이가 글자", client.post("/students", json={"name": "유관순", "age": "열여덟", "score": 90}))
show("필수 값 빠짐", client.post("/students", json={"name": "강감찬"}))
