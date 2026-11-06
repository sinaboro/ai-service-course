# 클라이언트 예제: 앱(ex02_path_query.py)에 실제로 요청을 보내고 응답을 출력해요 (python 으로 실행)
import json                           # 응답(JSON)을 보기 좋게 출력할 때 사용
from fastapi.testclient import TestClient
from ex02_path_query import app            # 같은 폴더의 앱 파일에서 app 가져오기

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

show("경로 매개변수", client.get("/items/3"))
show("쿼리 기본값", client.get("/items"))
# params= 로 쿼리를 사전으로 넘기면 ?skip=1&limit=2 로 바뀌어요
show("쿼리 지정", client.get("/items", params={"skip": 1, "limit": 2}))
show("검색", client.get("/items?keyword=마"))
show("계산", client.get("/calc/add?a=3&b=4.5"))
# 아래 두 개는 일부러 틀린 요청: FastAPI 가 422 오류와 이유를 돌려줘요
show("숫자가 아닌 id", client.get("/items/abc"))
show("필수 쿼리 빠짐", client.get("/calc/add?a=3"))
