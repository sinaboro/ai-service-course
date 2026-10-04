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

# 팁 비율(%) 열 만들기
tips["tip_rate"] = tips["tip"] / tips["total_bill"] * 100
# FacetGrid: 요일마다 칸 하나 → map_dataframe 으로 칸마다 같은 히스토그램
g = sns.FacetGrid(tips, col="day", col_order=["Thur", "Fri", "Sat", "Sun"], height=3, aspect=0.9)
g.map_dataframe(sns.histplot, x="tip_rate", bins=12, color="mediumpurple")     # 칸마다 같은 그래프
g.set_axis_labels("팁 비율 (%)", "손님 수")
g.set_titles("{col_name}")
# 칸마다 그 요일의 평균 팁 비율에 빨간 점선과 글자 추가
for ax in g.axes.flat:
    day = ax.get_title()
    m = tips.loc[tips["day"] == day, "tip_rate"].mean()
    ax.axvline(m, color="red", linestyle="--")
    ax.text(m + 0.5, ax.get_ylim()[1] * 0.85, f"평균 {m:.1f}%", color="red")
g.savefig(IMG / "ex05_facetgrid.png", dpi=100, bbox_inches="tight")
plt.show()
