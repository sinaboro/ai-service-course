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

# x 축 요일 순서 (정하지 않으면 데이터에 나온 순서대로)
order = ["Thur", "Fri", "Sat", "Sun"]
fig, axes = plt.subplots(1, 2, figsize=(13, 4.5))
sns.boxplot(data=tips, x="day", y="total_bill", order=order, ax=axes[0])
axes[0].set_title("boxplot: 요일별 계산 금액")

# 바이올린: 상자 그래프 + 분포 모양. split=True 로 성별을 반쪽씩, inner="quart" 로 사분위 선
sns.violinplot(data=tips, x="day", y="total_bill", hue="sex", split=True,
               order=order, inner="quart", ax=axes[1])
axes[1].set_title("violinplot: 요일 x 성별 (split)")
fig.tight_layout()
fig.savefig(IMG / "ex03_box_violin.png", dpi=100, bbox_inches="tight")
# 요일별 계산 금액 중앙값 (상자 가운데 선과 같은 값)
print(tips.groupby("day")["total_bill"].median().reindex(order))
plt.show()
