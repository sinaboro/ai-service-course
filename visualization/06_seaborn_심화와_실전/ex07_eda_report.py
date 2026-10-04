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

df = pd.read_csv(HERE / "data" / "students_life.csv")
print(df.describe().round(1))

fig = plt.figure(figsize=(14, 10))
grid = fig.add_gridspec(3, 3)

ax = fig.add_subplot(grid[0, 0])
sns.histplot(data=df, x="score", bins=15, kde=True, ax=ax)
ax.set_title("① 점수 분포")

ax = fig.add_subplot(grid[0, 1])
sns.boxplot(data=df, x="grade", y="score", order=["1학년", "2학년", "3학년"], ax=ax)
ax.set_title("② 학년별 점수")

ax = fig.add_subplot(grid[0, 2])
club_order = df.groupby("club")["score"].mean().sort_values(ascending=False).index
sns.barplot(data=df, x="club", y="score", order=club_order, errorbar=None, ax=ax)
ax.set_title("③ 동아리별 평균 점수")

ax = fig.add_subplot(grid[1, :2])
sns.regplot(data=df, x="study_h", y="score", scatter_kws={"alpha": 0.4}, line_kws={"color": "red"}, ax=ax)
ax.set_title("④ 공부 시간과 점수")
ax.set_xlabel("하루 공부 시간 (h)")

ax = fig.add_subplot(grid[1, 2])
sns.heatmap(df[["study_h", "sleep_h", "phone_h", "score"]].corr(), annot=True, fmt=".2f",
            cmap="coolwarm", vmin=-1, vmax=1, ax=ax)
ax.set_title("⑤ 상관계수")

ax = fig.add_subplot(grid[2, :])
df["phone_group"] = pd.cut(df["phone_h"], bins=[0, 2, 4, 10], labels=["2시간 이하", "2~4시간", "4시간 초과"])
sns.violinplot(data=df, x="phone_group", y="score", hue="phone_group", legend=False, inner="quart", ax=ax)
ax.set_title("⑥ 휴대폰 사용 시간 그룹별 점수")
ax.set_xlabel("")

fig.suptitle("학생 생활 데이터 탐색적 분석(EDA) 보고서", fontsize=18, fontweight="bold")
fig.tight_layout()
fig.savefig(IMG / "ex07_eda_report.png", dpi=100, bbox_inches="tight")

corr = df[["study_h", "phone_h", "score"]].corr()["score"]
print(f"\n[요약] 공부 시간-점수 상관 {corr['study_h']:.2f}, 휴대폰-점수 상관 {corr['phone_h']:.2f}")
print(df.groupby("phone_group", observed=True)["score"].mean().round(1))
plt.show()
