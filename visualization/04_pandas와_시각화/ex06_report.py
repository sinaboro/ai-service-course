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

# 날짜 → 분기 (1 ~ 4) → "Q1" 같은 글자
df["quarter"] = "Q" + df["date"].dt.quarter.astype(str)

fig, axes = plt.subplots(2, 2, figsize=(12, 8))
# ① 분기별 지점 매출 (묶음 막대)
q = df.pivot_table(index="quarter", columns="store", values="sales", aggfunc="sum")
q.plot.bar(ax=axes[0, 0], rot=0, title="분기별 지점 매출")

# ② 지점 매출 비중 (원)
share = df.groupby("store")["sales"].sum()
share.plot.pie(ax=axes[0, 1], autopct="%.1f%%", title="지점 매출 비중", ylabel="")

# ③ 전월 대비 성장률: pct_change() × 100. 줄면 빨강, 늘면 초록
growth = df.groupby("date")["sales"].sum().pct_change().mul(100)
growth.plot.bar(ax=axes[1, 0], color=["tomato" if g < 0 else "seagreen" for g in growth.fillna(0)],
                title="전월 대비 성장률 (%)")
axes[1, 0].set_xticklabels([d.strftime("%m월") for d in growth.index], rotation=0)

# ④ 지점-카테고리 조합 중 매출 상위 5개 (nlargest)
top = df.groupby(["store", "category"])["sales"].sum().nlargest(5)
top.index = [f"{s}-{c}" for s, c in top.index]
top.sort_values().plot.barh(ax=axes[1, 1], color="slateblue", title="매출 TOP 5 (지점-카테고리)")

# 전체 제목 → 간격 정리 → 저장
fig.suptitle("2026 카페 매출 보고서", fontsize=17, fontweight="bold")
fig.tight_layout()
fig.savefig(IMG / "ex06_report.png", dpi=100, bbox_inches="tight")
print(q)
plt.show()
