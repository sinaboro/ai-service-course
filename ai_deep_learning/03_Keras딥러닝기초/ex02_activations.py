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

# -5 ~ 5 를 200칸으로 나눈 x 값
v = np.linspace(-5, 5, 200)
fig, axes = plt.subplots(1, 3, figsize=(12, 3.2))
axes[0].plot(v, np.maximum(0, v))
axes[0].set_title("ReLU: 음수는 0 (숨은층에 주로)")
axes[1].plot(v, 1 / (1 + np.exp(-v)), color="crimson")
axes[1].set_title("sigmoid: 0 ~ 1 (예 / 아니요)")
# softmax: 각 점수를 exp 로 키운 뒤 전체 합으로 나눠 "합이 1 인 확률"로
scores = np.array([2.0, 1.0, 0.1])
soft = np.exp(scores) / np.exp(scores).sum()
axes[2].bar(["bottle", "can", "bag"], soft, color="teal")
axes[2].set_title("softmax: 합이 1 인 확률 (여러 클래스)")
for ax in axes:
    ax.grid(alpha=0.3)
fig.savefig(IMG / "ex02_activations.png", dpi=100, bbox_inches="tight")
print("점수", scores, "→ softmax", soft.round(3), "합", soft.sum().round(3))
