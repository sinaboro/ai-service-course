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

print(tips.head())
print(tips.shape)

ax = sns.scatterplot(data=tips, x="total_bill", y="tip", hue="time")   # 열 이름만 쓰면 끝
ax.set_title("계산 금액과 팁 (점심/저녁)")
ax.set_xlabel("계산 금액 ($)")
ax.set_ylabel("팁 ($)")
ax.figure.savefig(IMG / "ex01_first_seaborn.png", dpi=100, bbox_inches="tight")
plt.show()
