import platform
from pathlib import Path
import matplotlib.pyplot as plt

# 한글 폰트 (Windows: 맑은 고딕, macOS: 애플고딕, 그 외: 나눔고딕)
plt.rcParams["font.family"] = {"Windows": "Malgun Gothic", "Darwin": "AppleGothic"}.get(platform.system(), "NanumGothic")
plt.rcParams["axes.unicode_minus"] = False        # 마이너스(-) 기호 깨짐 방지
IMG = Path(__file__).parent / "images"            # 그래프를 저장할 폴더
IMG.mkdir(exist_ok=True)

import numpy as np

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
