# 클라이언트 예제: 앱(ex02_image.py)에 실제로 요청을 보내고 응답을 출력해요 (python 으로 실행)
import json                           # 응답(JSON)을 보기 좋게 출력할 때 사용
from fastapi.testclient import TestClient
from ex02_image import app            # 같은 폴더의 앱 파일에서 app 가져오기

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

from pathlib import Path
from PIL import Image
import io
S = Path(__file__).parent / "samples"
# png("파일 이름"): 업로드용 files 사전을 만들어 주는 짧은 함수
png = lambda name: {"file": (name, (S / name).read_bytes(), "image/png")}

show("이미지 정보", client.post("/image/info", files=png("blue_circle.png")))
show("흑백 이미지 정보", client.post("/image/info", files=png("digit_one.png")))
# 오류 경우: 이미지가 아닌 종류(415), 이름만 png 인 가짜 파일(400)
show("텍스트 파일", client.post("/image/info", files={"file": ("note.txt", b"hello", "text/plain")}))
show("가짜 PNG", client.post("/image/info", files={"file": ("fake.png", b"not image", "image/png")}))

# 썸네일은 JSON 이 아니라 이미지 자체가 와요 → 바이트를 다시 이미지로 열어 확인 · 저장
res = client.post("/image/thumbnail?size=80&gray=true", files=png("green_circle.png"))
print("썸네일 응답:", res.status_code, res.headers["content-type"], len(res.content), "bytes")
thumb = Image.open(io.BytesIO(res.content))
print("받은 이미지:", thumb.size, thumb.mode)
thumb.save(Path(__file__).parent / "images" / "thumb_green.png")
