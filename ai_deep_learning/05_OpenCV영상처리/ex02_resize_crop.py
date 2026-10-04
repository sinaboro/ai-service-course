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

# 사진 읽기 + 높이 · 너비 꺼내기
img = imread(Path(__file__).parent / "samples" / "beach_01.png")
h, w = img.shape[:2]

small = cv2.resize(img, (240, 240))                         # (너비, 높이) 순서!
scale = 320 / max(h, w)
keep = cv2.resize(img, (round(w * scale), round(h * scale)))  # 비율 유지하며 긴 쪽 320
crop = img[100:300, 50:250]                                 # [y1:y2, x1:x2] 자르기
flip = cv2.flip(img, 1)                                     # 1 = 좌우, 0 = 상하
rot = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
# 회전 행렬 만들기: (가운데 점, 각도, 배율)
M = cv2.getRotationMatrix2D((w / 2, h / 2), 15, 1.0)        # 가운데 기준 15도
rot15 = cv2.warpAffine(img, M, (w, h))

# 바뀐 모양(shape)을 한꺼번에 출력
for name, im in [("원본", img), ("240×240", small), ("비율 유지", keep), ("자르기", crop), ("좌우 뒤집기", flip), ("90도 회전", rot), ("15도 회전", rot15)]:
    print(f"{name:8s} {im.shape}")
# 4장을 한 그림으로 저장
show([("원본", img), ("자르기 [100:300, 50:250]", crop), ("좌우 뒤집기", flip), ("15도 회전", rot15)], "ex02_transform.png")
