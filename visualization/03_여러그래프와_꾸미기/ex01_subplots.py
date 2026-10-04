import platform
from pathlib import Path
import matplotlib.pyplot as plt

# 한글 폰트 (Windows: 맑은 고딕, macOS: 애플고딕, 그 외: 나눔고딕)
plt.rcParams["font.family"] = {"Windows": "Malgun Gothic", "Darwin": "AppleGothic"}.get(platform.system(), "NanumGothic")
plt.rcParams["axes.unicode_minus"] = False        # 마이너스(-) 기호 깨짐 방지
IMG = Path(__file__).parent / "images"            # 그래프를 저장할 폴더
IMG.mkdir(exist_ok=True)

import numpy as np

x = np.linspace(0, 2 * np.pi, 100)        # 0 ~ 2π 를 100 개로

fig, axes = plt.subplots(2, 2, figsize=(10, 6))   # 2행 2열
print(axes.shape)                                  # (2, 2) 배열

axes[0, 0].plot(x, np.sin(x));  axes[0, 0].set_title("sin")
axes[0, 1].plot(x, np.cos(x), color="orange");  axes[0, 1].set_title("cos")
axes[1, 0].bar(["A", "B", "C"], [3, 7, 5]);  axes[1, 0].set_title("막대")
axes[1, 1].scatter(np.random.default_rng(0).random(30), np.random.default_rng(1).random(30))
axes[1, 1].set_title("산점도")

fig.suptitle("2 x 2 subplots", fontsize=15)       # 전체 제목
fig.tight_layout()                                 # 겹치지 않게
fig.savefig(IMG / "ex01_subplots.png", dpi=100, bbox_inches="tight")
plt.show()
