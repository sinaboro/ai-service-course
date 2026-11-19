# ex04_catplot_relplot.py : catplot · relplot: col= · row= 로 그룹마다 칸 나눠 그리기
import platform                              # 운영체제 이름 알아내기 (한글 글꼴 고를 때 사용)
from pathlib import Path                     # 파일 · 폴더 경로를 다루는 도구
import matplotlib.pyplot as plt              # 그래프 도구 (관례적으로 plt 라는 별명)
import pandas as pd                          # 판다스 (관례적으로 pd 라는 별명)
import seaborn as sns                        # 시본: 통계 그래프 도구 (관례적으로 sns)

sns.set_theme(style="whitegrid")             # seaborn 기본 스타일
# ⚠ set_theme 은 글꼴을 초기화하므로 한글 글꼴은 "그 다음에" 설정
plt.rcParams["font.family"] = {"Windows": "Malgun Gothic", "Darwin": "AppleGothic"}.get(platform.system(), "NanumGothic")
plt.rcParams["axes.unicode_minus"] = False   # 마이너스(-) 기호가 네모로 깨지지 않게

HERE = Path(__file__).parent                 # 이 .py 파일이 있는 폴더 (어디서 실행해도 같은 곳)
IMG = HERE / "images"; IMG.mkdir(exist_ok=True)  # 그림 저장 폴더 (없으면 만들기)
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
