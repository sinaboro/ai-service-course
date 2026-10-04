import json
from fastapi.testclient import TestClient
from ex01_upload import app            # 같은 폴더의 앱 파일에서 app 가져오기

client = TestClient(app)              # 서버를 띄우지 않고 요청을 보내 볼 수 있는 도구


def show(title, res):
    print(f"[{title}] {res.request.method} {res.request.url.path} → {res.status_code}")
    try:
        print(json.dumps(res.json(), ensure_ascii=False, indent=2))
    except ValueError:
        print(res.text)
    print()

from pathlib import Path
S = Path(__file__).parent / "samples"

with open(S / "red_circle.png", "rb") as f:                   # "rb": 바이너리로 읽기
    show("파일 하나", client.post("/upload", files={"file": ("red_circle.png", f, "image/png")}))

show("텍스트 줄 수", client.post("/upload/text-lines",
     files={"file": ("note.txt", (S / "note.txt").read_bytes(), "text/plain")}))

many = [("files", (p.name, p.read_bytes(), "image/png")) for p in sorted(S.glob("*_circle.png"))]
show("여러 파일", client.post("/upload/many", files=many))
show("파일 없이 요청", client.post("/upload"))
