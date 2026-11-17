# 9장 API 점검: 서버를 켜지 않고도 TestClient 로 API 를 차례로 불러 봐요
# 실행: 이 폴더에서  python check_api.py   (pip install httpx 필요)
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

r = client.get("/api/hello")
print("GET    /api/hello       ", r.status_code, r.json()["message"])

r = client.get("/api/messages")
print("GET    /api/messages    ", r.status_code, len(r.json()), "개")

r = client.post("/api/messages", json={"name": "민지", "text": "반가워요"})
print("POST   /api/messages    ", r.status_code, r.json())

r = client.post("/api/messages", json={"name": "", "text": "이름이 비었어요"})
print("POST   (이름 빈칸)      ", r.status_code, r.json()["detail"][0]["type"])

r = client.delete("/api/messages/2")
print("DELETE /api/messages/2  ", r.status_code, r.json())

r = client.delete("/api/messages/99")
print("DELETE /api/messages/99 ", r.status_code, r.json())

r = client.get("/")
print("GET    /  (화면)         ", r.status_code, r.headers["content-type"])
