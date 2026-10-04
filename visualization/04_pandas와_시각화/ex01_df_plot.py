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

print(df.head())
print(df.shape)

monthly = df.groupby("date")["sales"].sum()          # 월별 전체 매출 (Series)
ax = monthly.plot(figsize=(8, 4), marker="o", title="월별 전체 매출 (만원)")   # Series.plot()
ax.set_xlabel("월")
ax.set_ylabel("매출")
ax.figure.savefig(IMG / "ex01_df_plot.png", dpi=100, bbox_inches="tight")
plt.show()
