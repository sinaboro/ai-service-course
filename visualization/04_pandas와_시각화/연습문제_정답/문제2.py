# 문제 2. 강남점의 카테고리별 월 매출을 선 그래프로 그리세요. (pivot_table 사용)

import platform
from pathlib import Path
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = {"Windows": "Malgun Gothic", "Darwin": "AppleGothic"}.get(platform.system(), "NanumGothic")
plt.rcParams["axes.unicode_minus"] = False
IMG = Path("images"); IMG.mkdir(exist_ok=True)

import pandas as pd
df = pd.read_csv("data/store_sales.csv", parse_dates=["date"])
g = df[df["store"] == "강남"].pivot_table(index="date", columns="category", values="sales")
ax = g.plot(figsize=(8, 4), marker=".", title="강남점 카테고리별 월 매출")
ax.figure.savefig(IMG / "q2_gangnam.png", dpi=100, bbox_inches="tight")
print(g.shape)
