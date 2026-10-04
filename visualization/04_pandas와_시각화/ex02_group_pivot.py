import platform
from pathlib import Path
import matplotlib.pyplot as plt

# 한글 폰트 (Windows: 맑은 고딕, macOS: 애플고딕, 그 외: 나눔고딕)
plt.rcParams["font.family"] = {"Windows": "Malgun Gothic", "Darwin": "AppleGothic"}.get(platform.system(), "NanumGothic")
plt.rcParams["axes.unicode_minus"] = False        # 마이너스(-) 기호 깨짐 방지
IMG = Path(__file__).parent / "images"            # 그래프를 저장할 폴더
IMG.mkdir(exist_ok=True)
import pandas as pd

DATA = Path(__file__).parent / "data"
df = pd.read_csv(DATA / "store_sales.csv", parse_dates=["date"])

# 지점별 매출 합계 → 작은 순서로 정렬 → 가로 막대 (pandas 의 .plot 이 matplotlib 을 대신 불러요)
by_store = df.groupby("store")["sales"].sum().sort_values()
ax = by_store.plot.barh(figsize=(7, 3.5), color="teal", title="지점별 연 매출")
# 막대 끝에 숫자 표시
ax.bar_label(ax.containers[0], fmt="%d")
ax.figure.savefig(IMG / "ex02_store_barh.png", dpi=100, bbox_inches="tight")

# 행 = 지점, 열 = 카테고리, 칸 = 매출 합계인 표 → 묶음 막대 (rot=0: 눈금 글자 똑바로)
pt = df.pivot_table(index="store", columns="category", values="sales", aggfunc="sum")
print(pt)
ax = pt.plot.bar(figsize=(8, 4.5), rot=0, title="지점 x 카테고리 매출 (묶음 막대)")
ax.figure.savefig(IMG / "ex02_pivot_bar.png", dpi=100, bbox_inches="tight")

# stacked=True: 같은 지점의 카테고리를 위로 쌓기
ax = pt.plot.bar(stacked=True, figsize=(8, 4.5), rot=0, title="지점별 카테고리 구성 (누적 막대)")
ax.legend(title="카테고리", bbox_to_anchor=(1.02, 1), loc="upper left")   # 범례를 그래프 밖으로
ax.figure.savefig(IMG / "ex02_pivot_stacked.png", dpi=100, bbox_inches="tight")
plt.show()
