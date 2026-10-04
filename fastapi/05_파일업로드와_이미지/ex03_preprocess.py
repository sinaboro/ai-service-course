import io
import numpy as np
from fastapi import FastAPI, HTTPException, UploadFile
from PIL import Image

app = FastAPI()


def to_model_input(img: Image.Image, size=(28, 28), gray=True) -> np.ndarray:
    """딥러닝 모델 입력 모양으로 바꾸기: (1, 높이, 너비, 채널), 값 0 ~ 1"""
    img = img.convert("L" if gray else "RGB")     # ① 색 모드 통일
    img = img.resize(size)                        # ② 모델이 학습한 크기로
    arr = np.asarray(img, dtype=np.float32) / 255.0   # ③ 0 ~ 255 → 0 ~ 1 (정규화)
    if gray:
        arr = arr[..., np.newaxis]                # (28, 28) → (28, 28, 1)
    return arr[np.newaxis, ...]                   # ④ 배치 차원 추가 → (1, 28, 28, 1)


@app.post("/preprocess")
async def preprocess(file: UploadFile, size: int = 28, gray: bool = True):
    try:
        img = Image.open(io.BytesIO(await file.read()))
    except Exception:
        raise HTTPException(400, "이미지를 읽을 수 없어요")
    x = to_model_input(img, (size, size), gray)
    return {
        "original": [img.width, img.height, img.mode],
        "input_shape": list(x.shape),
        "dtype": str(x.dtype),
        "min": round(float(x.min()), 3), "max": round(float(x.max()), 3),
        "mean": round(float(x.mean()), 4),
        "center_row": [round(float(v), 2) for v in x[0, size // 2, ::4, 0]] if gray else None,
    }
