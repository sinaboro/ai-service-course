import platform
from pathlib import Path
import matplotlib.pyplot as plt

# 그래프 한글 글꼴: 운영체제에 따라 알맞은 글꼴 고르기 (Windows = 맑은 고딕)
plt.rcParams["font.family"] = {"Windows": "Malgun Gothic", "Darwin": "AppleGothic"}.get(platform.system(), "NanumGothic")
# 마이너스(-) 기호가 네모로 깨지지 않게
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
# 숫자 배열의 모양(shape)과 자료형(dtype) 확인
print("모양(높이, 너비):", smile.shape, "| 자료형:", smile.dtype)
print(smile)

# 컬러 이미지는 (높이, 너비, 3) — 픽셀마다 빨강 · 초록 · 파랑 세 숫자
# 컬러: 0 으로 가득 찬 (8, 8, 3) 배열을 만들고 위 · 아래 절반을 색칠
color = np.zeros((8, 8, 3), dtype=np.uint8)
color[:4] = [255, 0, 0]     # 위쪽 절반 빨강
color[4:] = [0, 0, 255]     # 아래쪽 절반 파랑
print("컬러 모양:", color.shape, "| (0,0) 픽셀 값:", color[0, 0])

# 두 배열을 그림으로 보기: 흑백은 cmap="gray"
fig, axes = plt.subplots(1, 2, figsize=(7, 3.5))
axes[0].imshow(smile, cmap="gray")
axes[0].set_title("흑백 8×8")
axes[1].imshow(color)
axes[1].set_title("컬러 8×8×3")
# 눈금(숫자) 없애기
for ax in axes:
    ax.set_xticks([]); ax.set_yticks([])
fig.savefig(IMG / "ex02_image_is_numbers.png", dpi=100, bbox_inches="tight")
