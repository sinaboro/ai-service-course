# 클라이언트 예제: 웹 페이지가 하는 요청을 코드로 똑같이 보내 봐요 (python 으로 실행)
# 브라우저의 fetch(...) 한 줄 = TestClient 의 client.get/post/patch/delete 한 줄
from fastapi.testclient import TestClient

from ex03_todo_web import app

client = TestClient(app)

# 1) 페이지 열기: "/" 는 JSON 이 아니라 HTML 을 돌려줘요
res = client.get("/")
print("페이지:", res.status_code, res.headers["content-type"], "| 제목 포함?", "<title>할 일 목록</title>" in res.text)

# 2) [추가] 버튼 → POST /todos
print("추가:", client.post("/todos", json={"title": "FastAPI 복습", "priority": 2}).status_code)
print("추가:", client.post("/todos", json={"title": "웹 페이지 만들기"}).status_code)
print("빈 제목:", client.post("/todos", json={"title": ""}).status_code, "→ 화면에 '추가 실패' 표시")

# 3) 체크박스 → PATCH /todos/1
print("완료 표시:", client.patch("/todos/1", json={"done": True}).json())

# 4) [삭제] 버튼 → DELETE /todos/2
print("삭제:", client.delete("/todos/2").status_code)

# 5) 페이지가 다시 그리는 목록 → GET /todos
print("현재 목록:", client.get("/todos").json())
