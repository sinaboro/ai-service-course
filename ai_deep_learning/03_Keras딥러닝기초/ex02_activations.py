# ex02_activations.py : 활성화 함수(sigmoid · ReLU 등)의 모양을 그래프로 비교
import platform                                   # 운영체제 이름 알아내기 (한글 글꼴 고를 때 사용)
from pathlib import Path                          # 파일 · 폴더 경로를 다루는 도구
import matplotlib.pyplot as plt                   # 그래프 도구 (관례적으로 plt 라는 별명)

# 그래프 한글 글꼴: 운영체제에 따라 알맞은 글꼴 고르기 (Windows = 맑은 고딕)
plt.rcParams["font.family"] = {"Windows": "Malgun Gothic", "Darwin": "AppleGothic"}.get(platform.system(), "NanumGothic")
# 마이너스(-) 기호가 네모로 깨지지 않게
plt.rcParams["axes.unicode_minus"] = False        # 마이너스(-) 기호가 네모로 깨지지 않게
IMG = Path(__file__).parent / "images"            # 그림을 저장할 폴더
IMG.mkdir(exist_ok=True)                          # images 폴더 만들기 (이미 있으면 그냥 넘어가요)

import numpy as np                                # 넘파이 (관례적으로 np 라는 별명)

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
