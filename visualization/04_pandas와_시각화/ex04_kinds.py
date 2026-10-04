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

df["per_customer"] = (df["sales"] * 10000 / df["customers"]).round()   # 객단가 (원)

# 2행 × 3열 칸에 kind 만 바꿔 여섯 종류 그래프
fig, axes = plt.subplots(2, 3, figsize=(13, 7))
df["sales"].plot(kind="hist", bins=15, ax=axes[0, 0], title="hist: 매출 분포")
df.boxplot(column="sales", by="category", ax=axes[0, 1])                 # 그룹별 상자
axes[0, 1].set_title("box: 카테고리별 매출")
df.plot(kind="scatter", x="customers", y="sales", ax=axes[0, 2], alpha=0.6, title="scatter: 손님 수 vs 매출")
# area: 카테고리별 월 매출을 쌓은 면적 그래프
area = df.pivot_table(index="date", columns="category", values="sales", aggfunc="sum")
area.plot(kind="area", ax=axes[1, 0], title="area: 카테고리 누적")
df.groupby("category")["sales"].sum().plot(kind="pie", autopct="%.0f%%", ax=axes[1, 1], title="pie: 카테고리 비율")
# pie: 원 그래프는 y 축 이름이 필요 없어서 지워요
axes[1, 1].set_ylabel("")
df.groupby("store")["per_customer"].mean().plot(kind="bar", rot=0, ax=axes[1, 2], color="coral", title="bar: 지점별 평균 객단가")
fig.suptitle("")                 # boxplot(by=) 이 자동으로 붙이는 제목 지우기
fig.tight_layout()
fig.savefig(IMG / "ex04_kinds.png", dpi=100, bbox_inches="tight")
plt.show()
