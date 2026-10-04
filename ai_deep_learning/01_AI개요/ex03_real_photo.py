import platform
from pathlib import Path
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = {"Windows": "Malgun Gothic", "Darwin": "AppleGothic"}.get(platform.system(), "NanumGothic")
plt.rcParams["axes.unicode_minus"] = False
IMG = Path(__file__).parent / "images"            # 그림을 저장할 폴더
IMG.mkdir(exist_ok=True)

import cv2
from ultralytics.utils import ASSETS     # ultralytics 에 들어 있는 예제 사진

img = cv2.imread(str(ASSETS / "bus.jpg"))           # OpenCV 로 사진 읽기 (5장에서 자세히)
print("사진 모양:", img.shape, "→ 높이", img.shape[0], "· 너비", img.shape[1], "· 채널", img.shape[2])
print("전체 숫자 개수:", img.size)
print("왼쪽 위 픽셀 (파랑, 초록, 빨강):", img[0, 0])
print("가장 작은 값:", img.min(), "/ 가장 큰 값:", img.max())

small = cv2.resize(img, (16, 20))                    # 16 × 20 으로 확 줄이기
fig, axes = plt.subplots(1, 2, figsize=(7, 4.5))
axes[0].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
axes[0].set_title(f"원본 {img.shape[1]}×{img.shape[0]}")
axes[1].imshow(cv2.cvtColor(small, cv2.COLOR_BGR2RGB))
axes[1].set_title("16×20 로 줄이면 숫자 칸이 보여요")
for ax in axes:
    ax.set_xticks([]); ax.set_yticks([])
fig.savefig(IMG / "ex03_real_photo.png", dpi=100, bbox_inches="tight")
