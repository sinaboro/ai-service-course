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

g = sns.pairplot(tips, vars=["total_bill", "tip", "size"], hue="time", height=2.4, corner=True)
g.figure.suptitle("pairplot: 숫자 열끼리 모든 조합", y=1.02)
g.savefig(IMG / "ex03_pairplot.png", dpi=100, bbox_inches="tight")

j = sns.jointplot(data=tips, x="total_bill", y="tip", kind="hex", height=5)    # 가운데 + 위/오른쪽 분포
j.figure.suptitle("jointplot (kind='hex')", y=1.02)
j.savefig(IMG / "ex03_jointplot.png", dpi=100, bbox_inches="tight")
print("pairplot 칸 수:", g.axes.size)
plt.show()
