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
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# ① 초록색(병) 범위만 흰색으로 = 마스크
mask = cv2.inRange(hsv, np.array([40, 60, 60]), np.array([85, 255, 255]))
mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))   # 작은 점 지우기

# ② 흰 덩어리의 윤곽선 → 감싸는 상자
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
result = img.copy()
found = 0
for cnt in contours:
    if cv2.contourArea(cnt) < 100:                  # 너무 작으면 무시
        continue
    x, y, w, h = cv2.boundingRect(cnt)
    cv2.rectangle(result, (x, y), (x + w, y + h), (0, 0, 255), 2)
    found += 1
    print(f"찾은 물체 {found}: x={x}, y={y}, w={w}, h={h}, 넓이={cv2.contourArea(cnt):.0f}")
print("초록 물체 수:", found)
show([("원본", img), ("초록 마스크", mask), ("찾은 상자", result)], "ex06_color_detect.png")
