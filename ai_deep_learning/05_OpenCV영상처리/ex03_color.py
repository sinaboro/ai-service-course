import platform
from pathlib import Path
import matplotlib.pyplot as plt

# 그래프 한글 글꼴: 운영체제에 따라 알맞은 글꼴 고르기 (Windows = 맑은 고딕)
plt.rcParams["font.family"] = {"Windows": "Malgun Gothic", "Darwin": "AppleGothic"}.get(platform.system(), "NanumGothic")
# 마이너스(-) 기호가 네모로 깨지지 않게
plt.rcParams["axes.unicode_minus"] = False
IMG = Path(__file__).parent / "images"            # 그림을 저장할 폴더
IMG.mkdir(exist_ok=True)

import cv2
import numpy as np

from cvutil import imread

def show(items, name, cols=None):
    """(제목, BGR 이미지) 목록을 한 장의 그림으로 저장"""
    cols = cols or len(items)
    # 행 수 = 그림 개수를 열 수로 나눠 올림
    rows = (len(items) + cols - 1) // cols
    fig, axes = plt.subplots(rows, cols, figsize=(3.6 * cols, 3.2 * rows), squeeze=False)
    # 먼저 모든 칸의 눈금을 끄고, 그림이 있는 칸만 채우기
    for ax in axes.flat:
        ax.axis("off")
    for ax, (title, im) in zip(axes.flat, items):
        # 흑백(2차원)은 그대로, 컬러(BGR)는 RGB 로 바꿔서 보여 주기
        ax.imshow(im if im.ndim == 2 else cv2.cvtColor(im, cv2.COLOR_BGR2RGB), cmap="gray")
        ax.set_title(title)
    fig.savefig(IMG / name, dpi=100, bbox_inches="tight")

img = imread(Path(__file__).parent / "samples" / "beach_01.png")
# 같은 사진을 여러 색 공간으로 바꿔 보기
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)                  # 색상(H) · 채도(S) · 명도(V)
b, g, r = cv2.split(img)                                    # 채널 나누기
bright = cv2.convertScaleAbs(img, alpha=1.0, beta=60)       # 밝게 (+60)
dark = cv2.convertScaleAbs(img, alpha=0.6, beta=0)          # 어둡게 (×0.6)

# 바다 픽셀 하나의 BGR 값과 HSV 값 비교
print("HSV 범위: H 0 ~", hsv[..., 0].max(), "(OpenCV 는 0 ~ 179) / S, V 0 ~ 255")
print("바다 픽셀 BGR", img[5, 5], "→ HSV", hsv[5, 5])
print("평균 밝기: 원본", round(gray.mean(), 1), "/ 밝게", round(cv2.cvtColor(bright, cv2.COLOR_BGR2GRAY).mean(), 1), "/ 어둡게", round(cv2.cvtColor(dark, cv2.COLOR_BGR2GRAY).mean(), 1))
show([("원본", img), ("흑백", gray), ("H (색상) 채널", hsv[..., 0]), ("밝게 +60", bright), ("어둡게 ×0.6", dark), ("빨강(R) 채널", r)], "ex03_color.png", cols=3)
