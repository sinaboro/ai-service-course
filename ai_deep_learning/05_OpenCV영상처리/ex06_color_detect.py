# ex06_color_detect.py : 색과 윤곽선으로 물체 찾기 — 규칙 기반 탐지 (딥러닝 없이)
import platform                                   # 운영체제 이름 알아내기 (한글 글꼴 고를 때 사용)
from pathlib import Path                          # 파일 · 폴더 경로를 다루는 도구
import matplotlib.pyplot as plt                   # 그래프 도구 (관례적으로 plt 라는 별명)

# 그래프 한글 글꼴: 운영체제에 따라 알맞은 글꼴 고르기 (Windows = 맑은 고딕)
plt.rcParams["font.family"] = {"Windows": "Malgun Gothic", "Darwin": "AppleGothic"}.get(platform.system(), "NanumGothic")
# 마이너스(-) 기호가 네모로 깨지지 않게
plt.rcParams["axes.unicode_minus"] = False        # 마이너스(-) 기호가 네모로 깨지지 않게
IMG = Path(__file__).parent / "images"            # 그림을 저장할 폴더
IMG.mkdir(exist_ok=True)                          # images 폴더 만들기 (이미 있으면 그냥 넘어가요)

import cv2                                        # OpenCV: 영상 처리 도구
import numpy as np                                # 넘파이 (관례적으로 np 라는 별명)

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
    for ax, (title, im) in zip(axes.flat, items):  # zip: 칸과 (제목, 그림)을 하나씩 짝지어 꺼내기
        # 흑백(2차원)은 그대로, 컬러(BGR)는 RGB 로 바꿔서 보여 주기
        ax.imshow(im if im.ndim == 2 else cv2.cvtColor(im, cv2.COLOR_BGR2RGB), cmap="gray")
        ax.set_title(title)
    fig.savefig(IMG / name, dpi=100, bbox_inches="tight")

img = imread(Path(__file__).parent / "samples" / "beach_01.png")
# BGR → HSV: 색상(H)으로 색을 고르기 쉬워요
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# ① 초록색(병) 범위만 흰색으로 = 마스크
mask = cv2.inRange(hsv, np.array([40, 60, 60]), np.array([85, 255, 255]))
mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))   # 작은 점 지우기

# ② 흰 덩어리의 윤곽선 → 감싸는 상자
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# 결과를 그릴 복사본 + 찾은 개수
result = img.copy()
found = 0
# 윤곽선 하나씩 검사
for cnt in contours:
    if cv2.contourArea(cnt) < 100:                  # 너무 작으면 무시
        continue
    x, y, w, h = cv2.boundingRect(cnt)
    cv2.rectangle(result, (x, y), (x + w, y + h), (0, 0, 255), 2)
    found += 1
    print(f"찾은 물체 {found}: x={x}, y={y}, w={w}, h={h}, 넓이={cv2.contourArea(cnt):.0f}")
print("초록 물체 수:", found)
show([("원본", img), ("초록 마스크", mask), ("찾은 상자", result)], "ex06_color_detect.png")
