# 10장 API 점검 (TestClient): python check_api.py
from fastapi.testclient import TestClient  # 서버를 켜지 않고 코드로 요청을 보내는 도구

from app import app

c = TestClient(app)
print("GET    /api/todos     ", c.get("/api/todos").status_code, [t["title"] for t in c.get("/api/todos").json()])
r = c.post("/api/todos", json={"title": "장보기"})
print("POST   /api/todos     ", r.status_code, r.json())
r = c.patch("/api/todos/3", json={"done": True})
print("PATCH  /api/todos/3   ", r.status_code, r.json())
r = c.patch("/api/todos/3", json={"title": "장보기 (우유, 빵)"})
print("PATCH  제목 바꾸기     ", r.status_code, r.json())
r = c.post("/api/todos", json={"title": ""})
print("POST   (빈 제목)      ", r.status_code)
r = c.delete("/api/todos/3")
print("DELETE /api/todos/3   ", r.status_code, r.json())
r = c.delete("/api/todos/3")
print("DELETE 또 지우기      ", r.status_code, r.json())
