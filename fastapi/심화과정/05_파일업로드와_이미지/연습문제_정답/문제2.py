# 문제 2. 이미지를 받아 좌우로 뒤집은 이미지를 PNG로 돌려주는 POST /flip을 만들고, 응답의 content-type과 이미지 크기를 출력하세요.

import io
from fastapi import FastAPI, UploadFile
from fastapi.responses import Response
from fastapi.testclient import TestClient
from PIL import Image

app = FastAPI()


@app.post("/flip")
async def flip(file: UploadFile):
    img = Image.open(io.BytesIO(await file.read()))
    img = img.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    return Response(buf.getvalue(), media_type="image/png")


client = TestClient(app)
data = open("samples/blue_circle.png", "rb").read()
res = client.post("/flip", files={"file": ("blue_circle.png", data, "image/png")})
print(res.headers["content-type"], Image.open(io.BytesIO(res.content)).size)
