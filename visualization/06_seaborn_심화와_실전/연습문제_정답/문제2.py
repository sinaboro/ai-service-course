# 문제 2. data/students_life.csv로 수면 시간(sleep_h)과 점수(score) 의 regplot을 그리고 상관계수를 출력하세요.

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

df = pd.read_csv("data/students_life.csv")
ax = sns.regplot(data=df, x="sleep_h", y="score", scatter_kws={"alpha": 0.4})
ax.set_title("수면 시간과 점수")
ax.figure.savefig(IMG / "q2_sleep_score.png", dpi=100, bbox_inches="tight")
print("상관계수:", round(df["sleep_h"].corr(df["score"]), 2))
