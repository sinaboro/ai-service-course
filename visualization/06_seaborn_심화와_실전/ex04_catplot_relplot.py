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

# catplot: 범주형 그래프를 col(열) 기준으로 여러 칸에 나눠 그리기
g = sns.catplot(data=tips, x="day", y="total_bill", col="time", kind="box",
                order=["Thur", "Fri", "Sat", "Sun"], height=4, aspect=1.1)     # 시간대마다 칸
g.set_axis_labels("요일", "계산 금액 ($)")
# 칸 제목을 "Lunch", "Dinner" 처럼 값 이름만
g.set_titles("{col_name}")
g.savefig(IMG / "ex04_catplot.png", dpi=100, bbox_inches="tight")

# relplot: 관계 그래프를 행(row) × 열(col) 칸으로
r = sns.relplot(data=tips, x="total_bill", y="tip", hue="smoker",
                col="sex", row="time", height=3.2)                              # 2 x 2 칸
r.set_titles("{row_name} / {col_name}")
r.savefig(IMG / "ex04_relplot.png", dpi=100, bbox_inches="tight")
# 칸마다 손님 수 (시간대 × 성별)
print(tips.groupby(["time", "sex"]).size().unstack())
plt.show()
