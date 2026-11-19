# ex06_palette.py : 색 조합(palette) 바꿔 보기: 범주용 · 연속값용
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

# 비교할 팔레트(색 묶음) 4가지
palettes = ["deep", "pastel", "Set2", "coolwarm"]
fig, axes = plt.subplots(1, 4, figsize=(15, 3.5), sharey=True)
# 칸마다 같은 그래프를 팔레트만 바꿔 그리기 (errorbar=None: 신뢰구간 선 숨기기)
for ax, pal in zip(axes, palettes):
    sns.barplot(data=tips, x="day", y="total_bill", hue="day", palette=pal, legend=False,
                order=["Thur", "Fri", "Sat", "Sun"], errorbar=None, ax=ax)
    ax.set_title(f'palette="{pal}"')
fig.tight_layout()
fig.savefig(IMG / "ex06_palette.png", dpi=100, bbox_inches="tight")
# 팔레트 색을 16진수 색 코드로 확인
print(sns.color_palette("Set2").as_hex()[:4])
plt.show()
