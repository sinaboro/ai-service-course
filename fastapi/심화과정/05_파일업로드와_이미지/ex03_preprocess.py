# ex03_preprocess.py : 업로드한 이미지를 딥러닝 입력 배열 (1, 28, 28, 1) 로 전처리하기
# 실행: 이 폴더에서 uvicorn ex03_preprocess:app --reload (요청 예시는 ex03_preprocess_client.py)
import io                                         # 메모리를 파일처럼 쓰는 도구 (BytesIO)
import numpy as np                                # 넘파이 (관례적으로 np 라는 별명)
from fastapi import FastAPI, HTTPException, UploadFile
from PIL import Image                             # Pillow: 이미지 열기 · 크기 바꾸기

app = FastAPI()                                   # 앱(서버) 만들기 — uvicorn 이 이 app 을 실행해요


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
    # 업로드 → PIL 이미지 (읽을 수 없으면 400)
    try:
        img = Image.open(io.BytesIO(await file.read()))
    except Exception:
        raise HTTPException(400, "이미지를 읽을 수 없어요")
    # 모델 입력으로 바꾸기
    x = to_model_input(img, (size, size), gray)
    # 바뀐 결과를 숫자로 확인: 모양 · 자료형 · 최소/최대/평균 · 가운데 줄의 값 일부
    return {
        "original": [img.width, img.height, img.mode],
        "input_shape": list(x.shape),
        "dtype": str(x.dtype),
        "min": round(float(x.min()), 3), "max": round(float(x.max()), 3),
        "mean": round(float(x.mean()), 4),
        # 흑백일 때만: 가운데 줄(size // 2)에서 4칸마다(::4) 값을 뽑아 소수 2자리로 (전처리 결과 확인용)
        "center_row": [round(float(v), 2) for v in x[0, size // 2, ::4, 0]] if gray else None,
    }
