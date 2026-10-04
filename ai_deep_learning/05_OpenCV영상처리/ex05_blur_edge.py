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

img = imread(Path(__file__).parent / "samples" / "beach_01.png")
# 경계 · 이진화는 보통 흑백 사진에서 해요
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur(gray, (7, 7), 0)                    # 흐리게 → 잡음 줄이기
edges = cv2.Canny(blur, 50, 150)                            # 경계선 찾기
_, binary = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)   # 200 보다 밝으면 흰색
otsu_t, otsu = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# 결과 숫자로 확인: 경계 픽셀 수, 밝은 픽셀 비율, 오츠가 고른 기준값
print("경계 픽셀 수:", int((edges > 0).sum()))
print("밝은(>200) 픽셀 비율:", round((binary > 0).mean(), 3))
print("오츠 방법이 고른 기준값:", otsu_t)
show([("흑백", gray), ("가우시안 흐림", blur), ("Canny 경계", edges), ("이진화 >200", binary)], "ex05_blur_edge.png")
