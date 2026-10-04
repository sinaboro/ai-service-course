import platform
from pathlib import Path
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = {"Windows": "Malgun Gothic", "Darwin": "AppleGothic"}.get(platform.system(), "NanumGothic")
plt.rcParams["axes.unicode_minus"] = False
IMG = Path(__file__).parent / "images"            # 그림을 저장할 폴더
IMG.mkdir(exist_ok=True)

import cv2
import numpy as np
from ultralytics.utils import ASSETS

gray = cv2.imread(str(ASSETS / "bus.jpg"), cv2.IMREAD_GRAYSCALE)
gray = cv2.resize(gray, (405, 540))

kernels = {
    "세로 경계 찾기": np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], np.float32),
    "가로 경계 찾기": np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]], np.float32),
    "흐리게 (평균)": np.ones((5, 5), np.float32) / 25,
}
fig, axes = plt.subplots(1, 4, figsize=(13, 4.5))
axes[0].imshow(gray, cmap="gray"); axes[0].set_title("원본 (흑백)")
for ax, (name, k) in zip(axes[1:], kernels.items()):
    out = cv2.filter2D(gray.astype(np.float32), -1, k)     # ⭐ 필터를 이미지 전체에 밀며 곱하고 더하기
    ax.imshow(np.abs(out), cmap="gray"); ax.set_title(name)
    print(f"{name:10s} 필터 크기 {k.shape} → 결과 크기 {out.shape}")
for ax in axes:
    ax.axis("off")
fig.savefig(IMG / "ex01_convolution.png", dpi=100, bbox_inches="tight")
