# ex01_heatmap_corr.py : heatmap: 상관계수 표와 피벗 표를 색으로 보기
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

# 숫자 열 3개만 골라 상관계수(-1 ~ 1) 표 만들기
num = tips[["total_bill", "tip", "size"]]
corr = num.corr().round(2)                        # 상관계수 표
print(corr)

fig, axes = plt.subplots(1, 2, figsize=(13, 4.5))
# heatmap: 표의 값을 색으로. annot=True 로 칸에 숫자 쓰기, vmin · vmax 로 색 범위 고정
sns.heatmap(corr, annot=True, cmap="coolwarm", vmin=-1, vmax=1, ax=axes[0])
axes[0].set_title("상관계수 히트맵")

# 피벗 표(요일 × 시간대의 평균 팁)도 히트맵으로 그릴 수 있어요
pt = tips.pivot_table(index="day", columns="time", values="tip", aggfunc="mean").reindex(["Thur", "Fri", "Sat", "Sun"])
sns.heatmap(pt, annot=True, fmt=".2f", cmap="YlGnBu", linewidths=1, ax=axes[1])
axes[1].set_title("요일 x 시간 평균 팁 (피벗 히트맵)")
fig.tight_layout()
fig.savefig(IMG / "ex01_heatmap_corr.png", dpi=100, bbox_inches="tight")
plt.show()
