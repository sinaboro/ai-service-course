# 클라이언트 예제: 앱(ex01_upload.py)에 실제로 요청을 보내고 응답을 출력해요 (python 으로 실행)
import json                           # 응답(JSON)을 보기 좋게 출력할 때 사용
from fastapi.testclient import TestClient
from ex01_upload import app            # 같은 폴더의 앱 파일에서 app 가져오기

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
# 실습 파일이 있는 samples 폴더
S = Path(__file__).parent / "samples"

# files= {"폼 이름": (파일 이름, 내용, 종류)} 로 업로드
with open(S / "red_circle.png", "rb") as f:                   # "rb": 바이너리로 읽기
    show("파일 하나", client.post("/upload", files={"file": ("red_circle.png", f, "image/png")}))

show("텍스트 줄 수", client.post("/upload/text-lines",
     files={"file": ("note.txt", (S / "note.txt").read_bytes(), "text/plain")}))

# 여러 파일: 같은 이름("files")으로 여러 개를 리스트로
many = [("files", (p.name, p.read_bytes(), "image/png")) for p in sorted(S.glob("*_circle.png"))]
show("여러 파일", client.post("/upload/many", files=many))
# 파일 없이 보내면 422
show("파일 없이 요청", client.post("/upload"))
