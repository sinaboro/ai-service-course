import json
from fastapi.testclient import TestClient
from ex02_image import app            # 같은 폴더의 앱 파일에서 app 가져오기

client = TestClient(app)              # 서버를 띄우지 않고 요청을 보내 볼 수 있는 도구


def show(title, res):
    print(f"[{title}] {res.request.method} {res.request.url.path} → {res.status_code}")
    try:
        print(json.dumps(res.json(), ensure_ascii=False, indent=2))
    except ValueError:
        print(res.text)
    print()

from pathlib import Path
from PIL import Image
import io
S = Path(__file__).parent / "samples"
png = lambda name: {"file": (name, (S / name).read_bytes(), "image/png")}

show("이미지 정보", client.post("/image/info", files=png("blue_circle.png")))
show("흑백 이미지 정보", client.post("/image/info", files=png("digit_one.png")))
show("텍스트 파일", client.post("/image/info", files={"file": ("note.txt", b"hello", "text/plain")}))
show("가짜 PNG", client.post("/image/info", files={"file": ("fake.png", b"not image", "image/png")}))

res = client.post("/image/thumbnail?size=80&gray=true", files=png("green_circle.png"))
print("썸네일 응답:", res.status_code, res.headers["content-type"], len(res.content), "bytes")
thumb = Image.open(io.BytesIO(res.content))
print("받은 이미지:", thumb.size, thumb.mode)
thumb.save(Path(__file__).parent / "images" / "thumb_green.png")
