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

tips["tip_rate"] = tips["tip"] / tips["total_bill"] * 100

fig, ax = plt.subplots(figsize=(9, 5))
sns.scatterplot(data=tips, x="total_bill", y="tip_rate", hue="time", size="size",
                style="smoker", sizes=(20, 200), alpha=0.7, ax=ax)
ax.set_title("계산 금액과 팁 비율 (색=시간, 크기=인원, 모양=흡연)")
ax.set_ylabel("팁 비율 (%)")
ax.legend(bbox_to_anchor=(1.02, 1), loc="upper left")
fig.savefig(IMG / "ex05_scatter_hue_size.png", dpi=100, bbox_inches="tight")
print("평균 팁 비율:", round(tips["tip_rate"].mean(), 1), "%")
plt.show()
