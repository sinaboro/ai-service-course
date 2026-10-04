# 문제 3. data/students_life.csv로 catplot(kind="bar")을 이용해 학년(col)별 동아리 평균 점수를 칸으로 나눠 그리세요.

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
g = sns.catplot(data=df, x="club", y="score", col="grade", kind="bar", errorbar=None,
                col_order=["1학년", "2학년", "3학년"], height=3.5)
g.set_titles("{col_name}")
g.savefig(IMG / "q3_grade_club.png", dpi=100, bbox_inches="tight")
print(df.groupby(["grade", "club"])["score"].mean().round(1).unstack())
