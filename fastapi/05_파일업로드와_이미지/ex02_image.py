import io
from fastapi import FastAPI, HTTPException, UploadFile
from fastapi.responses import Response
from PIL import Image, UnidentifiedImageError

app = FastAPI()
# 허용하는 이미지 종류와 최대 크기
ALLOWED = {"image/png", "image/jpeg"}
MAX_BYTES = 2 * 1024 * 1024                              # 2MB


# 업로드 파일 → PIL 이미지 (세 가지 검사를 차례로)
async def read_image(file: UploadFile) -> Image.Image:
    if file.content_type not in ALLOWED:                 # ① 종류 검사
        raise HTTPException(415, f"PNG/JPEG 만 가능해요 (받은 종류: {file.content_type})")
    data = await file.read()
    if len(data) > MAX_BYTES:                            # ② 크기 검사
        raise HTTPException(413, "파일이 너무 커요 (최대 2MB)")
    try:
        return Image.open(io.BytesIO(data))              # ③ 진짜 이미지인지
    except UnidentifiedImageError:
        raise HTTPException(400, "이미지 파일을 읽을 수 없어요")


# 이미지 정보: 형식 · 색 모드 · 크기
@app.post("/image/info")
async def image_info(file: UploadFile):
    img = await read_image(file)
    return {"filename": file.filename, "format": img.format, "mode": img.mode, "width": img.width, "height": img.height}


# 썸네일 만들기 → PNG 바이트로 저장 → 이미지 그대로 응답
@app.post("/image/thumbnail")
async def thumbnail(file: UploadFile, size: int = 64, gray: bool = False):
    img = await read_image(file)
    img.thumbnail((size, size))                          # 비율을 지키며 줄이기
    if gray:
        img = img.convert("L")                           # 흑백
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    return Response(content=buf.getvalue(), media_type="image/png")   # 이미지 자체를 응답
