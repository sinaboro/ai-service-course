# 문제 3. 요일별 계산 금액 합계를 barplot으로 그리세요. (힌트: estimator="sum", errorbar=None)

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

order = ["Thur", "Fri", "Sat", "Sun"]
ax = sns.barplot(data=tips, x="day", y="total_bill", order=order, estimator="sum", errorbar=None, color="salmon")
ax.bar_label(ax.containers[0], fmt="%.0f")
ax.set_title("요일별 계산 금액 합계 ($)")
ax.figure.savefig(IMG / "q3_day_sum.png", dpi=100, bbox_inches="tight")
print(tips.groupby("day")["total_bill"].sum().reindex(order).round(0).tolist())
