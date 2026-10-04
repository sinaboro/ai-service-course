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

from cvutil import imread, imwrite

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

# 클래스별 상자 색 (OpenCV 는 BGR 순서: 빨강 = (0, 0, 230))
COLORS = {"bottle": (0, 0, 230), "can": (0, 140, 255), "bag": (160, 48, 112)}   # BGR


def draw_box(img, x1, y1, x2, y2, label, color):
    """탐지 결과 한 개 그리기: 상자 + 글자 배경 + 글자"""
    cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)
    (tw, th), base = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1)
    cv2.rectangle(img, (x1, y1 - th - base - 4), (x1 + tw + 4, y1), color, -1)   # -1 = 채우기
    # 글자 배경 상자 위에 흰 글씨 (LINE_AA: 글자 가장자리를 부드럽게)
    cv2.putText(img, label, (x1 + 2, y1 - base - 2), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)


img = imread(Path(__file__).parent / "samples" / "beach_01.png")
canvas = img.copy()                                  # 원본은 그대로 두고 복사본에 그리기
detections = [                                       # 모델이 찾았다고 가정한 결과 (이름, 신뢰도, x1, y1, x2, y2)
    ("bottle", 0.91, 163, 346, 187, 411),
    ("can", 0.84, 313, 28, 334, 55),
    ("bag", 0.77, 90, 90, 130, 129),
]
# 결과 하나씩 그리기
for name, conf, x1, y1, x2, y2 in detections:
    draw_box(canvas, x1, y1, x2, y2, f"{name} {conf:.2f}", COLORS[name])
# 상자 말고도 원 · 선 · 글자를 그릴 수 있어요
cv2.circle(canvas, (440, 440), 20, (0, 255, 255), -1)                      # 원
cv2.line(canvas, (0, 470), (479, 470), (255, 255, 255), 3)                 # 선
cv2.putText(canvas, "FloatWatch", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
# 그린 그림을 저장 (한글 경로라서 cvutil.imwrite)
imwrite(Path(__file__).parent / "images" / "ex04_boxes.png", canvas)
print("그린 상자:", len(detections), "개")
print("putText 는 한글을 못 써요 → 한글은 PIL(Pillow) 로 그려요")
