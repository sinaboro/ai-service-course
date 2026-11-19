# ex01_convolution.py : 합성곱: 필터(3×3)를 사진 위에 밀며 세로선 · 가로선 특징 찾기
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
from ultralytics.utils import ASSETS

# 예제 사진을 흑백으로 읽고 작게 줄이기 (계산을 빠르게)
gray = cv2.imread(str(ASSETS / "bus.jpg"), cv2.IMREAD_GRAYSCALE)
gray = cv2.resize(gray, (405, 540))

# 필터(커널) 3가지: 숫자 배치에 따라 찾는 모양이 달라져요
kernels = {
    "세로 경계 찾기": np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], np.float32),
    "가로 경계 찾기": np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]], np.float32),
    "흐리게 (평균)": np.ones((5, 5), np.float32) / 25,
}
# 그림 4칸: 원본 + 필터 3개의 결과
fig, axes = plt.subplots(1, 4, figsize=(13, 4.5))
axes[0].imshow(gray, cmap="gray"); axes[0].set_title("원본 (흑백)")
# zip: 칸(ax)과 (필터 이름, 필터)를 하나씩 짝지어 꺼내요. axes[1:] 은 첫 칸(원본 사진)을 뺀 나머지 칸
for ax, (name, k) in zip(axes[1:], kernels.items()):
    out = cv2.filter2D(gray.astype(np.float32), -1, k)     # ⭐ 필터를 이미지 전체에 밀며 곱하고 더하기
    # 결과에 음수가 생기니 절댓값(abs)으로 밝기를 보여 줘요
    ax.imshow(np.abs(out), cmap="gray"); ax.set_title(name)
    print(f"{name:10s} 필터 크기 {k.shape} → 결과 크기 {out.shape}")
for ax in axes:
    ax.axis("off")
fig.savefig(IMG / "ex01_convolution.png", dpi=100, bbox_inches="tight")
