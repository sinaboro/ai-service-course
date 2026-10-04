# 문제 2. seed=7로 평균 170, 표준편차 6인 키 데이터 500개를 만들어 히스토그램(bins=20)을 그리세요.

import platform
from pathlib import Path
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = {"Windows": "Malgun Gothic", "Darwin": "AppleGothic"}.get(platform.system(), "NanumGothic")
plt.rcParams["axes.unicode_minus"] = False
IMG = Path("images"); IMG.mkdir(exist_ok=True)

import numpy as np
rng = np.random.default_rng(seed=7)
heights = rng.normal(170, 6, 500)
fig, ax = plt.subplots(figsize=(7, 4))
ax.hist(heights, bins=20, edgecolor="white")
ax.set_title("키 분포 (500명)")
ax.set_xlabel("키 (cm)")
fig.savefig(IMG / "q2_height_hist.png", dpi=100, bbox_inches="tight")
print(f"평균 키: {heights.mean():.1f}cm")
