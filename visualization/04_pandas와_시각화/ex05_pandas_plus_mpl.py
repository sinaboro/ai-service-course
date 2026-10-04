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

# FuncFormatter: 눈금 숫자를 원하는 글자 모양으로 바꾸는 도구
from matplotlib.ticker import FuncFormatter

cat = df.pivot_table(index="date", columns="category", values="sales", aggfunc="sum")
cat.index = cat.index.strftime("%m월")                # x 눈금을 "01월" 형태로

# pandas 로 선 그래프 → 아래부터는 matplotlib 으로 꾸미기
fig, ax = plt.subplots(figsize=(10, 4.5))
cat.plot(ax=ax, linewidth=2.5, colormap="tab10")
# y 눈금: 1200 → "1,200만"
ax.yaxis.set_major_formatter(FuncFormatter(lambda v, p: f"{v:,.0f}만"))
# 음료 매출이 가장 높은 달에 화살표 + 설명 글자 (annotate)
best = cat["음료"].idxmax()
ax.annotate(f"음료 최고 {cat['음료'].max():,}만", xy=(list(cat.index).index(best), cat["음료"].max()),
            xytext=(1, cat["음료"].max() + 10), arrowprops={"arrowstyle": "->"})
ax.set_title("카테고리별 월 매출 (pandas + matplotlib 꾸미기)")
ax.set_xlabel("")
# 위 · 오른쪽 테두리 지우기, 범례는 그래프 아래로
ax.spines[["top", "right"]].set_visible(False)
ax.legend(ncol=4, loc="upper center", bbox_to_anchor=(0.5, -0.12))
fig.savefig(IMG / "ex05_pandas_plus_mpl.png", dpi=100, bbox_inches="tight")
plt.show()
