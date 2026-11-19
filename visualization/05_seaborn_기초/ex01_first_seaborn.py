# ex01_first_seaborn.py : 첫 seaborn 그래프: data= · x= · y= · hue= 로 열 이름만 넘기기
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

# 데이터 맨 앞 5행과 (행 수, 열 수) 확인
print(tips.head())
print(tips.shape)

# data= 표, x · y = 열 이름, hue = 색으로 나눌 열 → seaborn 이 축 · 범례를 알아서 만들어요
ax = sns.scatterplot(data=tips, x="total_bill", y="tip", hue="time")   # 열 이름만 쓰면 끝
ax.set_title("계산 금액과 팁 (점심/저녁)")
ax.set_xlabel("계산 금액 ($)")
ax.set_ylabel("팁 ($)")
ax.figure.savefig(IMG / "ex01_first_seaborn.png", dpi=100, bbox_inches="tight")
plt.show()
