# ex02_regplot.py : 회귀선(추세선): regplot(칸 하나) · lmplot(칸 나누기)
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

import numpy as np                           # 넘파이 (관례적으로 np 라는 별명)

fig, ax = plt.subplots(figsize=(8, 5))
sns.regplot(data=tips, x="total_bill", y="tip", scatter_kws={"alpha": 0.5},
            line_kws={"color": "red"}, ax=ax)               # 산점도 + 회귀선 + 신뢰구간
ax.set_title("계산 금액이 늘면 팁도 늘까?")
fig.savefig(IMG / "ex02_regplot.png", dpi=100, bbox_inches="tight")

# 같은 직선을 numpy 로 직접 구해 보기 (기울기 · 절편)
slope, intercept = np.polyfit(tips["total_bill"], tips["tip"], 1)   # 직선 y = ax + b
print(f"회귀선: 팁 = {slope:.3f} x 계산금액 + {intercept:.3f}")
print(f"계산 금액 $30 → 예상 팁 ${slope * 30 + intercept:.2f}")

# lmplot: 그룹(hue) · 칸(col) 별로 회귀선을 나눠 그리기
g = sns.lmplot(data=tips, x="total_bill", y="tip", hue="smoker", col="time", height=4)   # 그룹·칸별 회귀선
g.figure.suptitle("시간대별 · 흡연 여부별 회귀선", y=1.03)
g.savefig(IMG / "ex02_lmplot.png", dpi=100, bbox_inches="tight")
plt.show()
