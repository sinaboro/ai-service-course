# 문제 2. 점심/저녁(time)별 팁 분포를 boxplot으로 그리고, 흡연 여부(smoker)를 hue로 나누세요.

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

ax = sns.boxplot(data=tips, x="time", y="tip", hue="smoker")
ax.set_title("시간대 x 흡연 여부별 팁")
ax.figure.savefig(IMG / "q2_time_box.png", dpi=100, bbox_inches="tight")
print(tips.groupby(["time", "smoker"])["tip"].median().round(2).to_dict())
