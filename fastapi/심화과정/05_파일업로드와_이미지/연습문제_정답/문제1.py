# 문제 1. 업로드한 이미지의 평균 밝기(흑백으로 바꾼 뒤 0 ~ 255 평균, 소수 1자리)를 돌려주는 POST /brightness를 만들고 samples/digit_one.png로 시험하세요.

import io
import numpy as np
from fastapi import FastAPI, UploadFile
from fastapi.testclient import TestClient
from PIL import Image

app = FastAPI()


@app.post("/brightness")
async def brightness(file: UploadFile):
    img = Image.open(io.BytesIO(await file.read())).convert("L")
    return {"filename": file.filename, "brightness": round(float(np.asarray(img).mean()), 1)}


client = TestClient(app)
data = open("samples/digit_one.png", "rb").read()
print(client.post("/brightness", files={"file": ("digit_one.png", data, "image/png")}).json())
