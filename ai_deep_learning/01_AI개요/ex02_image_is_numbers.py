import platform
from pathlib import Path
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = {"Windows": "Malgun Gothic", "Darwin": "AppleGothic"}.get(platform.system(), "NanumGothic")
plt.rcParams["axes.unicode_minus"] = False
IMG = Path(__file__).parent / "images"            # 그림을 저장할 폴더
IMG.mkdir(exist_ok=True)

import numpy as np

# 8 × 8 흑백 이미지: 0 = 검정, 255 = 흰색
smile = np.array([
    [0,   0, 255, 255, 255, 255,   0,   0],
    [0, 255,   0,   0,   0,   0, 255,   0],
    [255, 0, 255,   0,   0, 255,   0, 255],
    [255, 0,   0,   0,   0,   0,   0, 255],
    [255, 0, 255,   0,   0, 255,   0, 255],
    [255, 0,   0, 255, 255,   0,   0, 255],
    [0, 255,   0,   0,   0,   0, 255,   0],
    [0,   0, 255, 255, 255, 255,   0,   0],
], dtype=np.uint8)
print("모양(높이, 너비):", smile.shape, "| 자료형:", smile.dtype)
print(smile)

# 컬러 이미지는 (높이, 너비, 3) — 픽셀마다 빨강 · 초록 · 파랑 세 숫자
color = np.zeros((8, 8, 3), dtype=np.uint8)
color[:4] = [255, 0, 0]     # 위쪽 절반 빨강
color[4:] = [0, 0, 255]     # 아래쪽 절반 파랑
print("컬러 모양:", color.shape, "| (0,0) 픽셀 값:", color[0, 0])

fig, axes = plt.subplots(1, 2, figsize=(7, 3.5))
axes[0].imshow(smile, cmap="gray")
axes[0].set_title("흑백 8×8")
axes[1].imshow(color)
axes[1].set_title("컬러 8×8×3")
for ax in axes:
    ax.set_xticks([]); ax.set_yticks([])
fig.savefig(IMG / "ex02_image_is_numbers.png", dpi=100, bbox_inches="tight")
