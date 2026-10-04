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

# 1행 × 3열 칸. seaborn 함수에 ax= 로 그릴 칸을 알려 줘요
fig, axes = plt.subplots(1, 3, figsize=(14, 4))
# ① 기본 히스토그램 (구간 20개)
sns.histplot(data=tips, x="total_bill", bins=20, ax=axes[0])
axes[0].set_title("histplot: 계산 금액 분포")

sns.histplot(data=tips, x="total_bill", hue="time", kde=True, ax=axes[1])   # 그룹별 + 부드러운 곡선
axes[1].set_title("hue + kde=True")

sns.kdeplot(data=tips, x="tip", hue="sex", fill=True, ax=axes[2])          # 밀도 곡선만
axes[2].set_title("kdeplot: 성별 팁 분포")
fig.tight_layout()
fig.savefig(IMG / "ex02_hist_kde.png", dpi=100, bbox_inches="tight")
plt.show()
