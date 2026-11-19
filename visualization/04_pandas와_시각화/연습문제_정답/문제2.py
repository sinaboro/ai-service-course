# 문제 2. 강남점의 카테고리별 월 매출을 선 그래프로 그리세요. (pivot_table 사용)

import platform  # 운영체제 이름 알아내기 (한글 글꼴 고를 때 사용)
from pathlib import Path  # 파일 · 폴더 경로를 다루는 도구
import matplotlib.pyplot as plt  # 그래프 도구 (관례적으로 plt 라는 별명)
plt.rcParams["font.family"] = {"Windows": "Malgun Gothic", "Darwin": "AppleGothic"}.get(platform.system(), "NanumGothic")
plt.rcParams["axes.unicode_minus"] = False  # 마이너스(-) 기호가 네모로 깨지지 않게
IMG = Path("images"); IMG.mkdir(exist_ok=True)
# 이 파일은 연습문제_정답 폴더 안에 있어요 → 한 단계 위(장 폴더)의 data 폴더를 가리켜요
# (▶ 버튼 · 터미널 어디서 실행해도 CSV 를 찾을 수 있어요)
DATA = Path(__file__).parent.parent / "data"

import pandas as pd  # 판다스 (관례적으로 pd 라는 별명)
df = pd.read_csv(DATA / "store_sales.csv", parse_dates=["date"])
g = df[df["store"] == "강남"].pivot_table(index="date", columns="category", values="sales")
ax = g.plot(figsize=(8, 4), marker=".", title="강남점 카테고리별 월 매출")
ax.figure.savefig(IMG / "q2_gangnam.png", dpi=100, bbox_inches="tight")
print(g.shape)
