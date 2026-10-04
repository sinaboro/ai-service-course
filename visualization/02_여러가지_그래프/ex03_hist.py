import platform
from pathlib import Path
import matplotlib.pyplot as plt

# 한글 폰트 (Windows: 맑은 고딕, macOS: 애플고딕, 그 외: 나눔고딕)
plt.rcParams["font.family"] = {"Windows": "Malgun Gothic", "Darwin": "AppleGothic"}.get(platform.system(), "NanumGothic")
plt.rcParams["axes.unicode_minus"] = False        # 마이너스(-) 기호 깨짐 방지
IMG = Path(__file__).parent / "images"            # 그래프를 저장할 폴더
IMG.mkdir(exist_ok=True)

import numpy as np

rng = np.random.default_rng(seed=0)
scores = rng.normal(loc=72, scale=12, size=300).clip(0, 100)   # 평균 72, 표준편차 12

fig, ax = plt.subplots(figsize=(8, 4.5))
ax.hist(scores, bins=15, color="mediumseagreen", edgecolor="white")
ax.axvline(scores.mean(), color="red", linestyle="--", label=f"평균 {scores.mean():.1f}")
ax.set_title("시험 점수 분포 (300명)")
ax.set_xlabel("점수")
ax.set_ylabel("학생 수")
ax.legend()
fig.savefig(IMG / "ex03_hist.png", dpi=100, bbox_inches="tight")
print(f"평균 {scores.mean():.1f}, 최저 {scores.min():.1f}, 최고 {scores.max():.1f}")
plt.show()
