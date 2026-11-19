# ex03_pair_joint.py : pairplot(모든 열 조합) · jointplot(두 변수 + 각자의 분포)
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

# pairplot: 고른 열들의 모든 짝을 산점도로 (corner=True: 겹치는 위쪽 절반은 생략)
g = sns.pairplot(tips, vars=["total_bill", "tip", "size"], hue="time", height=2.4, corner=True)
g.figure.suptitle("pairplot: 숫자 열끼리 모든 조합", y=1.02)
g.savefig(IMG / "ex03_pairplot.png", dpi=100, bbox_inches="tight")

# jointplot: 가운데는 육각형 칸(hex)으로 점의 밀도, 위 · 오른쪽에는 각 값의 분포
j = sns.jointplot(data=tips, x="total_bill", y="tip", kind="hex", height=5)    # 가운데 + 위/오른쪽 분포
j.figure.suptitle("jointplot (kind='hex')", y=1.02)
j.savefig(IMG / "ex03_jointplot.png", dpi=100, bbox_inches="tight")
print("pairplot 칸 수:", g.axes.size)
plt.show()
