import json
from fastapi.testclient import TestClient
from ex01_todo_crud import app            # 같은 폴더의 앱 파일에서 app 가져오기

client = TestClient(app)              # 서버를 띄우지 않고 요청을 보내 볼 수 있는 도구


def show(title, res):
    print(f"[{title}] {res.request.method} {res.request.url.path} → {res.status_code}")
    try:
        print(json.dumps(res.json(), ensure_ascii=False, indent=2))
    except ValueError:
        print(res.text)
    print()

show("만들기 1", client.post("/todos", json={"title": "파이썬 복습", "priority": 2}))
show("만들기 2", client.post("/todos", json={"title": "판다스 과제"}))
show("만들기 3", client.post("/todos", json={"title": "모델 학습"}))
show("하나 읽기", client.get("/todos/2"))
show("일부 수정 (PATCH)", client.patch("/todos/2", json={"done": True}))
show("전체 수정 (PUT)", client.put("/todos/3", json={"title": "모델 학습 + 평가", "priority": 1}))
show("완료된 것만", client.get("/todos", params={"done": True}))
res = client.delete("/todos/1")
print(f"[삭제] DELETE /todos/1 → {res.status_code} (본문 없음: {res.text!r})\n")
show("삭제한 것 읽기", client.get("/todos/1"))
show("전체 목록", client.get("/todos"))
