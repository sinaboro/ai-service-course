# ex05_scatter_hue_size.py : 관계 그래프: scatterplot 에 hue(색) · size(크기) · style(모양)로 정보 더하기
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

# 팁 비율(%) = 팁 ÷ 계산 금액 × 100 → 새 열
tips["tip_rate"] = tips["tip"] / tips["total_bill"] * 100

fig, ax = plt.subplots(figsize=(9, 5))
# 한 점에 정보 5가지: x 위치(금액), y 위치(팁 비율), 색(시간), 크기(인원), 모양(흡연)
sns.scatterplot(data=tips, x="total_bill", y="tip_rate", hue="time", size="size",
                style="smoker", sizes=(20, 200), alpha=0.7, ax=ax)
ax.set_title("계산 금액과 팁 비율 (색=시간, 크기=인원, 모양=흡연)")
ax.set_ylabel("팁 비율 (%)")
# 범례가 그래프를 가리지 않게 오른쪽 밖으로
ax.legend(bbox_to_anchor=(1.02, 1), loc="upper left")
fig.savefig(IMG / "ex05_scatter_hue_size.png", dpi=100, bbox_inches="tight")
print("평균 팁 비율:", round(tips["tip_rate"].mean(), 1), "%")
plt.show()
