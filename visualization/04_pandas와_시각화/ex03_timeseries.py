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

ts = df.pivot_table(index="date", columns="store", values="sales", aggfunc="sum")
print(ts.head(3))

ax = ts.plot(figsize=(9, 4.5), marker="o", title="지점별 월 매출 추이")
ax.set_ylabel("매출 (만원)")
ax.figure.savefig(IMG / "ex03_store_trend.png", dpi=100, bbox_inches="tight")

total = ts.sum(axis=1)
ma3 = total.rolling(3).mean()                 # 3개월 이동평균
fig, ax = plt.subplots(figsize=(9, 4.5))
total.plot(ax=ax, marker="o", alpha=0.5, label="월 매출")
ma3.plot(ax=ax, linewidth=3, label="3개월 이동평균")
ax.set_title("전체 매출과 3개월 이동평균")
ax.legend()
fig.savefig(IMG / "ex03_moving_avg.png", dpi=100, bbox_inches="tight")
print(ma3.round(1).tail(3))
plt.show()
