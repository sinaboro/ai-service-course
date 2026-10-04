import platform
from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

sns.set_theme(style="whitegrid")             # seaborn 기본 스타일
# ⚠ set_theme 은 글꼴을 초기화하므로 한글 글꼴은 "그 다음에" 설정
plt.rcParams["font.family"] = {"Windows": "Malgun Gothic", "Darwin": "AppleGothic"}.get(platform.system(), "NanumGothic")
plt.rcParams["axes.unicode_minus"] = False

HERE = Path(__file__).parent
IMG = HERE / "images"; IMG.mkdir(exist_ok=True)
tips = pd.read_csv(HERE / "data" / "tips.csv")   # 식당 팁 데이터 (244건)

order = ["Thur", "Fri", "Sat", "Sun"]
fig, axes = plt.subplots(1, 2, figsize=(13, 4.5))
ax = sns.countplot(data=tips, x="day", hue="time", order=order, ax=axes[0])   # 개수 세기
for c in ax.containers:
    ax.bar_label(c)
axes[0].set_title("countplot: 요일별 손님 수")

sns.barplot(data=tips, x="day", y="tip", hue="smoker", order=order, ax=axes[1])  # 평균 + 신뢰구간
axes[1].set_title("barplot: 요일 x 흡연 평균 팁")
fig.tight_layout()
fig.savefig(IMG / "ex04_count_bar.png", dpi=100, bbox_inches="tight")
print(tips.groupby(["day", "smoker"])["tip"].mean().round(2).unstack().reindex(order))
plt.show()
