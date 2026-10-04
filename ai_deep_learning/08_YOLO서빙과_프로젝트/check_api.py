# 서버를 켜지 않고 API 점검하기 (TestClient)
from pathlib import Path

from fastapi.testclient import TestClient

from app import app

# TestClient: 서버를 켜지 않고도 브라우저처럼 요청을 보내 볼 수 있어요
client = TestClient(app)
HERE = Path(__file__).parent

# ① 첫 화면(HTML)이 오는지
r = client.get("/")
print("GET /                ", r.status_code, r.headers["content-type"], "FloatWatch" in r.text)
# ② CSS 파일이 오는지
r = client.get("/static/css/style.css")
print("GET /static/css/...  ", r.status_code, r.headers["content-type"])

# ③ 샘플 사진을 업로드해서 탐지 (브라우저 폼과 같은 모양: files + data)
png = (HERE / "static" / "images" / "sample.png").read_bytes()
r = client.post("/detect", files={"file": ("sample.png", png, "image/png")}, data={"conf": "0.25"})
data = r.json()
print("POST /detect 0.25    ", r.status_code, data["count"], "개 |", data["seconds"], "초")
for b in data["boxes"]:
    print("    ", b)
# ④ 신뢰도 기준을 올리면 결과가 줄어드는지
r = client.post("/detect", files={"file": ("sample.png", png, "image/png")}, data={"conf": "0.5"})
print("POST /detect 0.5     ", r.status_code, r.json()["count"], "개", [b["class"] for b in r.json()["boxes"]])
# ⑤ 사진이 아닌 파일은 400 오류가 나는지
r = client.post("/detect", files={"file": ("memo.txt", b"hello", "text/plain")})
print("POST /detect (txt)   ", r.status_code, r.json())
