# 문제 2. seed=7로 평균 170, 표준편차 6인 키 데이터 500개를 만들어 히스토그램(bins=20)을 그리세요.

import platform  # 운영체제 이름 알아내기 (한글 글꼴 고를 때 사용)
from pathlib import Path  # 파일 · 폴더 경로를 다루는 도구
import matplotlib.pyplot as plt  # 그래프 도구 (관례적으로 plt 라는 별명)
plt.rcParams["font.family"] = {"Windows": "Malgun Gothic", "Darwin": "AppleGothic"}.get(platform.system(), "NanumGothic")
plt.rcParams["axes.unicode_minus"] = False  # 마이너스(-) 기호가 네모로 깨지지 않게
IMG = Path("images"); IMG.mkdir(exist_ok=True)

import numpy as np  # 넘파이 (관례적으로 np 라는 별명)
rng = np.random.default_rng(seed=7)
heights = rng.normal(170, 6, 500)
fig, ax = plt.subplots(figsize=(7, 4))
ax.hist(heights, bins=20, edgecolor="white")
ax.set_title("키 분포 (500명)")
ax.set_xlabel("키 (cm)")
fig.savefig(IMG / "q2_height_hist.png", dpi=100, bbox_inches="tight")
print(f"평균 키: {heights.mean():.1f}cm")
