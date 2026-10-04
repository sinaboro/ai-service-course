import platform
from pathlib import Path
import matplotlib.pyplot as plt

# 한글 폰트 (Windows: 맑은 고딕, macOS: 애플고딕, 그 외: 나눔고딕)
plt.rcParams["font.family"] = {"Windows": "Malgun Gothic", "Darwin": "AppleGothic"}.get(platform.system(), "NanumGothic")
plt.rcParams["axes.unicode_minus"] = False        # 마이너스(-) 기호 깨짐 방지
IMG = Path(__file__).parent / "images"            # 그래프를 저장할 폴더
IMG.mkdir(exist_ok=True)

from matplotlib.ticker import FuncFormatter, PercentFormatter

months = [f"{m}월" for m in range(1, 13)]
revenue = [1250000, 1380000, 1520000, 1490000, 1710000, 1950000,
           2100000, 2050000, 1880000, 1760000, 1990000, 2400000]
growth = [0, 0.104, 0.101, -0.02, 0.148, 0.14, 0.077, -0.024, -0.083, -0.064, 0.131, 0.206]

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 7))
ax1.bar(months, revenue, color="slateblue")
ax1.yaxis.set_major_formatter(FuncFormatter(lambda v, pos: f"{v / 10000:,.0f}만"))  # 1,250,000 → 125만
ax1.set_title("월 매출")
ax1.spines[["top", "right"]].set_visible(False)            # 위·오른쪽 테두리 없애기

colors = ["tomato" if g < 0 else "seagreen" for g in growth]
ax2.bar(months, growth, color=colors)
ax2.yaxis.set_major_formatter(PercentFormatter(1.0))         # 0.1 → 10%
ax2.axhline(0, color="black", linewidth=0.8)
ax2.set_title("전월 대비 성장률")
ax2.spines[["top", "right"]].set_visible(False)
ax2.tick_params(axis="x", rotation=45)                       # x 눈금 글자 기울이기
fig.tight_layout()
fig.savefig(IMG / "ex04_ticks_spines.png", dpi=100, bbox_inches="tight")
plt.show()
