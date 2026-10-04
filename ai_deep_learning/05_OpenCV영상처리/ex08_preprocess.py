import platform
from pathlib import Path
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = {"Windows": "Malgun Gothic", "Darwin": "AppleGothic"}.get(platform.system(), "NanumGothic")
plt.rcParams["axes.unicode_minus"] = False
IMG = Path(__file__).parent / "images"            # 그림을 저장할 폴더
IMG.mkdir(exist_ok=True)

import cv2
import numpy as np

from cvutil import imread


def letterbox(img, size=640, color=(114, 114, 114)):
    """비율을 지키며 size×size 정사각형에 넣고, 남는 곳은 회색으로 채우기 (YOLO 방식)"""
    h, w = img.shape[:2]
    r = size / max(h, w)
    nw, nh = round(w * r), round(h * r)
    resized = cv2.resize(img, (nw, nh))
    canvas = np.full((size, size, 3), color, np.uint8)
    top, left = (size - nh) // 2, (size - nw) // 2
    canvas[top:top + nh, left:left + nw] = resized
    return canvas, r, (left, top)


img = imread(Path(__file__).parent / "samples" / "beach_01.png")
wide = cv2.resize(img, (720, 405))                   # 16:9 가로 사진이라고 생각하기
box, r, (left, top) = letterbox(wide, 640)
print("원본:", wide.shape, "→ letterbox:", box.shape, "| 배율", round(r, 3), "| 여백 (왼쪽, 위)", (left, top))

x = cv2.cvtColor(box, cv2.COLOR_BGR2RGB)             # ① BGR → RGB
x = x.astype(np.float32) / 255.0                     # ② 0 ~ 1
keras_input = x[None]                                # ③ 배치 차원 → (1, 640, 640, 3)  Keras: 채널이 마지막
torch_input = x.transpose(2, 0, 1)[None]             # (1, 3, 640, 640)  PyTorch · YOLO: 채널이 앞
print("Keras 입력 :", keras_input.shape, keras_input.dtype)
print("YOLO 입력  :", torch_input.shape, "| 값 범위", float(torch_input.min()), "~", float(torch_input.max()))

# 모델이 letterbox 사진에서 찾은 상자 → 원래 사진 좌표로 되돌리기
bx1, by1, bx2, by2 = 100, 300, 140, 380             # 예: 640 사진에서의 상자
ox1, oy1 = (bx1 - left) / r, (by1 - top) / r
ox2, oy2 = (bx2 - left) / r, (by2 - top) / r
print("원래 사진 좌표:", [round(v) for v in (ox1, oy1, ox2, oy2)])

fig, axes = plt.subplots(1, 2, figsize=(10, 3.8))
axes[0].imshow(cv2.cvtColor(wide, cv2.COLOR_BGR2RGB)); axes[0].set_title(f"원본 {wide.shape[1]}×{wide.shape[0]}")
axes[1].imshow(cv2.cvtColor(box, cv2.COLOR_BGR2RGB)); axes[1].set_title("letterbox 640×640")
fig.savefig(IMG / "ex08_letterbox.png", dpi=100, bbox_inches="tight")
