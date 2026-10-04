# 문제 3. 광고비 [1, 2, 3, 4, 5, 6](백만 원)와 매출 [12, 15, 21, 24, 30, 31](백만 원)의 산점도를 그리고, 각 점 옆에 매출 값을 표시하세요.

import platform
from pathlib import Path
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = {"Windows": "Malgun Gothic", "Darwin": "AppleGothic"}.get(platform.system(), "NanumGothic")
plt.rcParams["axes.unicode_minus"] = False
IMG = Path("images"); IMG.mkdir(exist_ok=True)

ad = [1, 2, 3, 4, 5, 6]
sales = [12, 15, 21, 24, 30, 31]
fig, ax = plt.subplots(figsize=(6, 4))
ax.scatter(ad, sales, s=80, color="darkorange")
for x, y in zip(ad, sales):
    ax.text(x + 0.1, y, str(y))
ax.set_xlabel("광고비 (백만 원)")
ax.set_ylabel("매출 (백만 원)")
ax.set_title("광고비와 매출")
fig.savefig(IMG / "q3_ad_scatter.png", dpi=100, bbox_inches="tight")
print("저장 완료")
