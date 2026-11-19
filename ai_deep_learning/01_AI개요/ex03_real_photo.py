# ex03_real_photo.py : 진짜 사진도 숫자 배열 — 사진의 모양(높이, 너비, 3)과 한 칸의 색 값 확인
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
from ultralytics.utils import ASSETS     # ultralytics 에 들어 있는 예제 사진

img = cv2.imread(str(ASSETS / "bus.jpg"))           # OpenCV 로 사진 읽기 (5장에서 자세히)
# 사진 크기 · 숫자 개수 · 픽셀 값 범위 확인
print("사진 모양:", img.shape, "→ 높이", img.shape[0], "· 너비", img.shape[1], "· 채널", img.shape[2])
print("전체 숫자 개수:", img.size)
print("왼쪽 위 픽셀 (파랑, 초록, 빨강):", img[0, 0])
print("가장 작은 값:", img.min(), "/ 가장 큰 값:", img.max())

# 사진을 아주 작게 줄이면 픽셀 칸(숫자 하나하나)이 눈에 보여요
small = cv2.resize(img, (16, 20))                    # 16 × 20 으로 확 줄이기
fig, axes = plt.subplots(1, 2, figsize=(7, 4.5))
# OpenCV 는 BGR 순서라서 matplotlib(RGB)로 보여 줄 때 순서를 바꿔요
axes[0].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
axes[0].set_title(f"원본 {img.shape[1]}×{img.shape[0]}")
axes[1].imshow(cv2.cvtColor(small, cv2.COLOR_BGR2RGB))
axes[1].set_title("16×20 로 줄이면 숫자 칸이 보여요")
for ax in axes:
    ax.set_xticks([]); ax.set_yticks([])
fig.savefig(IMG / "ex03_real_photo.png", dpi=100, bbox_inches="tight")
