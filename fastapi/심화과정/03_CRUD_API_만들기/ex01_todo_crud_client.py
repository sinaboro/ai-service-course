# 클라이언트 예제: 앱(ex01_todo_crud.py)에 실제로 요청을 보내고 응답을 출력해요 (python 으로 실행)
import json                           # 응답(JSON)을 보기 좋게 출력할 때 사용
from fastapi.testclient import TestClient
from ex01_todo_crud import app            # 같은 폴더의 앱 파일에서 app 가져오기

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

# C(만들기) → R(읽기) → U(수정) → D(삭제) 순서로 시험
show("만들기 1", client.post("/todos", json={"title": "파이썬 복습", "priority": 2}))
show("만들기 2", client.post("/todos", json={"title": "판다스 과제"}))
show("만들기 3", client.post("/todos", json={"title": "모델 학습"}))
show("하나 읽기", client.get("/todos/2"))
show("일부 수정 (PATCH)", client.patch("/todos/2", json={"done": True}))
show("전체 수정 (PUT)", client.put("/todos/3", json={"title": "모델 학습 + 평가", "priority": 1}))
show("완료된 것만", client.get("/todos", params={"done": True}))
# DELETE 는 본문이 없어서 show 대신 상태 코드만 출력
res = client.delete("/todos/1")
print(f"[삭제] DELETE /todos/1 → {res.status_code} (본문 없음: {res.text!r})\n")
# 지운 것을 다시 읽으면 404
show("삭제한 것 읽기", client.get("/todos/1"))
show("전체 목록", client.get("/todos"))
