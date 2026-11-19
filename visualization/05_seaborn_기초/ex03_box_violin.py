# ex03_box_violin.py : 그룹별 분포: boxplot(상자) · violinplot(바이올린)
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
