import json
from fastapi.testclient import TestClient
from ex03_preprocess import app            # 같은 폴더의 앱 파일에서 app 가져오기

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
png = lambda name: {"file": (name, (S / name).read_bytes(), "image/png")}

show("숫자 이미지 → 28x28 흑백", client.post("/preprocess", files=png("digit_one.png")))
show("컬러 이미지 → 224x224 RGB", client.post("/preprocess?size=224&gray=false", files=png("red_circle.png")))
