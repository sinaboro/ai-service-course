import platform
from pathlib import Path
import matplotlib.pyplot as plt

# 한글 폰트 (Windows: 맑은 고딕, macOS: 애플고딕, 그 외: 나눔고딕)
plt.rcParams["font.family"] = {"Windows": "Malgun Gothic", "Darwin": "AppleGothic"}.get(platform.system(), "NanumGothic")
plt.rcParams["axes.unicode_minus"] = False        # 마이너스(-) 기호 깨짐 방지
IMG = Path(__file__).parent / "images"            # 그래프를 저장할 폴더
IMG.mkdir(exist_ok=True)

import numpy as np

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
