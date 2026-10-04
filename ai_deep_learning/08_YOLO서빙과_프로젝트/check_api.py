# 서버를 켜지 않고 API 점검하기 (TestClient)
from pathlib import Path

from fastapi.testclient import TestClient

from app import app

client = TestClient(app)
HERE = Path(__file__).parent

r = client.get("/")
print("GET /                ", r.status_code, r.headers["content-type"], "FloatWatch" in r.text)
r = client.get("/static/css/style.css")
print("GET /static/css/...  ", r.status_code, r.headers["content-type"])

png = (HERE / "static" / "images" / "sample.png").read_bytes()
r = client.post("/detect", files={"file": ("sample.png", png, "image/png")}, data={"conf": "0.25"})
data = r.json()
print("POST /detect 0.25    ", r.status_code, data["count"], "개 |", data["seconds"], "초")
for b in data["boxes"]:
    print("    ", b)
r = client.post("/detect", files={"file": ("sample.png", png, "image/png")}, data={"conf": "0.5"})
print("POST /detect 0.5     ", r.status_code, r.json()["count"], "개", [b["class"] for b in r.json()["boxes"]])
r = client.post("/detect", files={"file": ("memo.txt", b"hello", "text/plain")})
print("POST /detect (txt)   ", r.status_code, r.json())
