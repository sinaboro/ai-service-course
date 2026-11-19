# 문제 2. 이미지를 받아 좌우로 뒤집은 이미지를 PNG로 돌려주는 POST /flip을 만들고, 응답의 content-type과 이미지 크기를 출력하세요.

import io                                         # 메모리를 파일처럼 쓰는 도구 (BytesIO)
from pathlib import Path                          # 파일 · 폴더 경로를 다루는 도구

from fastapi import FastAPI, UploadFile
from fastapi.responses import Response
from fastapi.testclient import TestClient         # 서버를 켜지 않고 코드로 요청을 보내는 도구
from PIL import Image                             # Pillow: 이미지 열기 · 크기 바꾸기

app = FastAPI()                                   # 앱(서버) 만들기 — uvicorn 이 이 app 을 실행해요


@app.post("/flip")
async def flip(file: UploadFile):
    img = Image.open(io.BytesIO(await file.read()))
    img = img.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    return Response(buf.getvalue(), media_type="image/png")


# 정답 폴더(연습문제_정답)에서 실행해도 되도록, 한 단계 위 장 폴더의 samples 를 찾아요
SAMPLES = Path(__file__).parent.parent / "samples"

client = TestClient(app)                          # 서버를 켜지 않고 코드로 요청 보내기
data = (SAMPLES / "blue_circle.png").read_bytes() # 이미지 파일을 바이트(bytes)로 읽기
res = client.post("/flip", files={"file": ("blue_circle.png", data, "image/png")})
print(res.headers["content-type"], Image.open(io.BytesIO(res.content)).size)
