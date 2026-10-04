# FloatWatch 서버: 웹 페이지(HTML/CSS/JS) + 탐지 API
import base64
import io
import time
from pathlib import Path

from fastapi import FastAPI, File, Form, HTTPException, UploadFile
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from PIL import Image

from detector import detect, draw

HERE = Path(__file__).parent
MAX_BYTES = 5 * 1024 * 1024
app = FastAPI(title="FloatWatch")

app.mount("/static", StaticFiles(directory=HERE / "static"), name="static")   # 정적 파일


@app.get("/")
def index():
    return FileResponse(HERE / "static" / "index.html")                      # 첫 화면


@app.post("/detect")
async def detect_api(file: UploadFile = File(...), conf: float = Form(0.25)):
    if file.content_type not in ("image/png", "image/jpeg"):
        raise HTTPException(400, "PNG 또는 JPG 사진만 올릴 수 있어요")
    data = await file.read()
    if len(data) > MAX_BYTES:
        raise HTTPException(413, "5MB 이하 사진만 올릴 수 있어요")

    start = time.perf_counter()
    img = Image.open(io.BytesIO(data)).convert("RGB")
    boxes = detect(img, conf)
    result = draw(img, boxes)
    seconds = round(time.perf_counter() - start, 3)

    buf = io.BytesIO()
    result.save(buf, format="PNG")
    image_url = "data:image/png;base64," + base64.b64encode(buf.getvalue()).decode()   # 이미지를 글자로
    return {"count": len(boxes), "boxes": boxes, "seconds": seconds, "image": image_url}
