# 문제 1. tips 데이터에서 인원(size)별 손님 수를 countplot으로 그리고 막대 위에 개수를 표시하세요.

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

ax = sns.countplot(data=tips, x="size", color="steelblue")
ax.bar_label(ax.containers[0])
ax.set_title("인원별 손님 수")
ax.figure.savefig(IMG / "q1_size_count.png", dpi=100, bbox_inches="tight")
print(tips["size"].value_counts().sort_index().tolist())
