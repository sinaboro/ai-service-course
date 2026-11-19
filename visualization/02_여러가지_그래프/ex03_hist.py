# ex03_hist.py : 히스토그램: 값을 구간(bin)으로 나눠 분포 보기
import platform                                   # 운영체제 이름 알아내기 (한글 글꼴 고를 때 사용)
from pathlib import Path                          # 파일 · 폴더 경로를 다루는 도구
import matplotlib.pyplot as plt                   # 그래프 도구 (관례적으로 plt 라는 별명)

# 한글 폰트 (Windows: 맑은 고딕, macOS: 애플고딕, 그 외: 나눔고딕)
plt.rcParams["font.family"] = {"Windows": "Malgun Gothic", "Darwin": "AppleGothic"}.get(platform.system(), "NanumGothic")
plt.rcParams["axes.unicode_minus"] = False        # 마이너스(-) 기호 깨짐 방지
IMG = Path(__file__).parent / "images"            # 그래프를 저장할 폴더
IMG.mkdir(exist_ok=True)                          # images 폴더 만들기 (이미 있으면 그냥 넘어가요)

import numpy as np                                # 넘파이 (관례적으로 np 라는 별명)

# 평균 72, 표준편차 12 인 정규분포 점수 300개 (clip: 0 ~ 100 밖은 잘라 내기)
rng = np.random.default_rng(seed=0)
scores = rng.normal(loc=72, scale=12, size=300).clip(0, 100)   # 평균 72, 표준편차 12

fig, ax = plt.subplots(figsize=(8, 4.5))
# hist: 값을 bins(15) 개 구간으로 나눠 구간마다 몇 명인지 막대로
ax.hist(scores, bins=15, color="mediumseagreen", edgecolor="white")
# axvline: 세로 기준선 (여기서는 평균 위치에 빨간 점선)
ax.axvline(scores.mean(), color="red", linestyle="--", label=f"평균 {scores.mean():.1f}")
ax.set_title("시험 점수 분포 (300명)")
ax.set_xlabel("점수")
ax.set_ylabel("학생 수")
ax.legend()
fig.savefig(IMG / "ex03_hist.png", dpi=100, bbox_inches="tight")
print(f"평균 {scores.mean():.1f}, 최저 {scores.min():.1f}, 최고 {scores.max():.1f}")
plt.show()
