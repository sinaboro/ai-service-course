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

num = tips[["total_bill", "tip", "size"]]
corr = num.corr().round(2)                        # 상관계수 표
print(corr)

fig, axes = plt.subplots(1, 2, figsize=(13, 4.5))
sns.heatmap(corr, annot=True, cmap="coolwarm", vmin=-1, vmax=1, ax=axes[0])
axes[0].set_title("상관계수 히트맵")

pt = tips.pivot_table(index="day", columns="time", values="tip", aggfunc="mean").reindex(["Thur", "Fri", "Sat", "Sun"])
sns.heatmap(pt, annot=True, fmt=".2f", cmap="YlGnBu", linewidths=1, ax=axes[1])
axes[1].set_title("요일 x 시간 평균 팁 (피벗 히트맵)")
fig.tight_layout()
fig.savefig(IMG / "ex01_heatmap_corr.png", dpi=100, bbox_inches="tight")
plt.show()
