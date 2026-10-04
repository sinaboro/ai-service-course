import platform
from pathlib import Path
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = {"Windows": "Malgun Gothic", "Darwin": "AppleGothic"}.get(platform.system(), "NanumGothic")
plt.rcParams["axes.unicode_minus"] = False
IMG = Path(__file__).parent / "images"            # 그림을 저장할 폴더
IMG.mkdir(exist_ok=True)

import cv2

from cvutil import imread

def show(items, name, cols=None):
    """(제목, BGR 이미지) 목록을 한 장의 그림으로 저장"""
    cols = cols or len(items)
    rows = (len(items) + cols - 1) // cols
    fig, axes = plt.subplots(rows, cols, figsize=(3.6 * cols, 3.2 * rows), squeeze=False)
    for ax in axes.flat:
        ax.axis("off")
    for ax, (title, im) in zip(axes.flat, items):
        ax.imshow(im if im.ndim == 2 else cv2.cvtColor(im, cv2.COLOR_BGR2RGB), cmap="gray")
        ax.set_title(title)
    fig.savefig(IMG / name, dpi=100, bbox_inches="tight")

img = imread(Path(__file__).parent / "samples" / "beach_01.png")
h, w = img.shape[:2]

small = cv2.resize(img, (240, 240))                         # (너비, 높이) 순서!
scale = 320 / max(h, w)
keep = cv2.resize(img, (round(w * scale), round(h * scale)))  # 비율 유지하며 긴 쪽 320
crop = img[100:300, 50:250]                                 # [y1:y2, x1:x2] 자르기
flip = cv2.flip(img, 1)                                     # 1 = 좌우, 0 = 상하
rot = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
M = cv2.getRotationMatrix2D((w / 2, h / 2), 15, 1.0)        # 가운데 기준 15도
rot15 = cv2.warpAffine(img, M, (w, h))

for name, im in [("원본", img), ("240×240", small), ("비율 유지", keep), ("자르기", crop), ("좌우 뒤집기", flip), ("90도 회전", rot), ("15도 회전", rot15)]:
    print(f"{name:8s} {im.shape}")
show([("원본", img), ("자르기 [100:300, 50:250]", crop), ("좌우 뒤집기", flip), ("15도 회전", rot15)], "ex02_transform.png")
