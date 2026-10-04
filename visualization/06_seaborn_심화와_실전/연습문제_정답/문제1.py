# 문제 1. tips 데이터로 성별 × 흡연 여부별 평균 계산 금액 피벗 표를 만들어 히트맵(숫자 표시)으로 그리세요.

import platform
from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
sns.set_theme(style="whitegrid")
plt.rcParams["font.family"] = {"Windows": "Malgun Gothic", "Darwin": "AppleGothic"}.get(platform.system(), "NanumGothic")
plt.rcParams["axes.unicode_minus"] = False
IMG = Path("images"); IMG.mkdir(exist_ok=True)
tips = pd.read_csv("data/tips.csv")

pt = tips.pivot_table(index="sex", columns="smoker", values="total_bill", aggfunc="mean")
ax = sns.heatmap(pt, annot=True, fmt=".1f", cmap="Oranges")
ax.set_title("성별 x 흡연 평균 계산 금액")
ax.figure.savefig(IMG / "q1_sex_smoker_heat.png", dpi=100, bbox_inches="tight")
print(pt.round(1))
