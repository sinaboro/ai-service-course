# 문제 1. data/store_sales.csv에서 카테고리별 연 매출을 가로 막대(큰 값이 위)로 그리세요.

import platform
from pathlib import Path
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = {"Windows": "Malgun Gothic", "Darwin": "AppleGothic"}.get(platform.system(), "NanumGothic")
plt.rcParams["axes.unicode_minus"] = False
IMG = Path("images"); IMG.mkdir(exist_ok=True)
# 이 파일은 연습문제_정답 폴더 안에 있어요 → 한 단계 위(장 폴더)의 data 폴더를 가리켜요
# (▶ 버튼 · 터미널 어디서 실행해도 CSV 를 찾을 수 있어요)
DATA = Path(__file__).parent.parent / "data"

import pandas as pd
df = pd.read_csv(DATA / "store_sales.csv")
s = df.groupby("category")["sales"].sum().sort_values()
ax = s.plot.barh(figsize=(6, 3.5), color="seagreen", title="카테고리별 연 매출")
ax.figure.savefig(IMG / "q1_category.png", dpi=100, bbox_inches="tight")
print(s)
