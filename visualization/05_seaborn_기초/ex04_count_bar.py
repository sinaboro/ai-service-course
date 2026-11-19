# ex04_count_bar.py : 범주 그래프: countplot(개수) · barplot(평균 + 신뢰구간)
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

order = ["Thur", "Fri", "Sat", "Sun"]
fig, axes = plt.subplots(1, 2, figsize=(13, 4.5))
ax = sns.countplot(data=tips, x="day", hue="time", order=order, ax=axes[0])   # 개수 세기
# 막대 묶음(containers)마다 끝에 개수 숫자 붙이기
for c in ax.containers:
    ax.bar_label(c)
axes[0].set_title("countplot: 요일별 손님 수")

# barplot: 막대 = 평균, 검은 선 = 신뢰구간(평균이 있을 법한 범위)
sns.barplot(data=tips, x="day", y="tip", hue="smoker", order=order, ax=axes[1])  # 평균 + 신뢰구간
axes[1].set_title("barplot: 요일 x 흡연 평균 팁")
fig.tight_layout()
fig.savefig(IMG / "ex04_count_bar.png", dpi=100, bbox_inches="tight")
# 그래프와 같은 값을 표로 확인 (unstack: 흡연 여부를 열로 펼치기)
print(tips.groupby(["day", "smoker"])["tip"].mean().round(2).unstack().reindex(order))
plt.show()
