# ex04_scatter.py : 산점도: 두 값의 관계를 점으로 (색 · 크기로 정보 더하기)
import platform                                       # 운영체제 이름 알아내기 (한글 글꼴 고를 때 사용)
from pathlib import Path                              # 파일 · 폴더 경로를 다루는 도구
import matplotlib.pyplot as plt                       # 그래프 도구 (관례적으로 plt 라는 별명)

# 한글 폰트 (Windows: 맑은 고딕, macOS: 애플고딕, 그 외: 나눔고딕)
plt.rcParams["font.family"] = {"Windows": "Malgun Gothic", "Darwin": "AppleGothic"}.get(platform.system(), "NanumGothic")
plt.rcParams["axes.unicode_minus"] = False        # 마이너스(-) 기호 깨짐 방지
IMG = Path(__file__).parent / "images"            # 그래프를 저장할 폴더
IMG.mkdir(exist_ok=True)                              # images 폴더 만들기 (이미 있으면 그냥 넘어가요)

import numpy as np                                    # 넘파이 (관례적으로 np 라는 별명)

rng = np.random.default_rng(seed=1)
hours = rng.uniform(0, 10, 60)                        # 공부 시간
score = 40 + hours * 5 + rng.normal(0, 6, 60)         # 점수 (공부할수록 높음 + 잡음)
sleep = rng.uniform(4, 9, 60)                         # 수면 시간

fig, ax = plt.subplots(figsize=(8, 5))
sc = ax.scatter(hours, score, c=sleep, s=sleep * 15, cmap="viridis", alpha=0.8)
fig.colorbar(sc, label="수면 시간")                    # 색이 뜻하는 값
ax.set_title("공부 시간과 점수의 관계")
ax.set_xlabel("공부 시간 (시간)")
ax.set_ylabel("점수")
fig.savefig(IMG / "ex04_scatter.png", dpi=100, bbox_inches="tight")
print("상관계수:", round(np.corrcoef(hours, score)[0, 1], 2))
plt.show()
