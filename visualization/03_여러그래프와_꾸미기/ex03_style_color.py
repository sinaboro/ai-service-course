# ex03_style_color.py : 스타일(plt.style.use)과 색 지도(colormap) 바꾸기
import platform                                   # 운영체제 이름 알아내기 (한글 글꼴 고를 때 사용)
from pathlib import Path                          # 파일 · 폴더 경로를 다루는 도구
import matplotlib.pyplot as plt                   # 그래프 도구 (관례적으로 plt 라는 별명)

# 한글 폰트 (Windows: 맑은 고딕, macOS: 애플고딕, 그 외: 나눔고딕)
plt.rcParams["font.family"] = {"Windows": "Malgun Gothic", "Darwin": "AppleGothic"}.get(platform.system(), "NanumGothic")
plt.rcParams["axes.unicode_minus"] = False        # 마이너스(-) 기호 깨짐 방지
IMG = Path(__file__).parent / "images"            # 그래프를 저장할 폴더
IMG.mkdir(exist_ok=True)                          # images 폴더 만들기 (이미 있으면 그냥 넘어가요)

import numpy as np                                # 넘파이 (관례적으로 np 라는 별명)

print("사용 가능한 스타일 일부:", plt.style.available[:5])
x = np.arange(1, 8)

with plt.style.context("ggplot"):                 # 이 블록 안에서만 ggplot 스타일
    plt.rcParams["font.family"] = {"Windows": "Malgun Gothic", "Darwin": "AppleGothic"}.get(platform.system(), "NanumGothic")
    fig, axes = plt.subplots(1, 2, figsize=(11, 4))
    for i in range(5):
        axes[0].plot(x, x * (i + 1), label=f"선 {i + 1}")    # 기본 색 순서 C0, C1, ...
    axes[0].set_title("ggplot 스타일 + 기본 색 순서")
    axes[0].legend()

    values = np.array([3, 5, 8, 6, 9, 4, 7])
    colors = plt.cm.Blues(values / values.max())            # 값이 클수록 진한 파랑
    axes[1].bar(x, values, color=colors)
    axes[1].set_title("색 지도(Blues)로 값 강조")
    fig.savefig(IMG / "ex03_style_color.png", dpi=100, bbox_inches="tight")
plt.show()
