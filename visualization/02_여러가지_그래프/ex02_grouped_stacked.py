import platform
from pathlib import Path
import matplotlib.pyplot as plt

# 한글 폰트 (Windows: 맑은 고딕, macOS: 애플고딕, 그 외: 나눔고딕)
plt.rcParams["font.family"] = {"Windows": "Malgun Gothic", "Darwin": "AppleGothic"}.get(platform.system(), "NanumGothic")
plt.rcParams["axes.unicode_minus"] = False        # 마이너스(-) 기호 깨짐 방지
IMG = Path(__file__).parent / "images"            # 그래프를 저장할 폴더
IMG.mkdir(exist_ok=True)

import numpy as np

quarters = ["1분기", "2분기", "3분기", "4분기"]
online = np.array([120, 150, 170, 210])
offline = np.array([200, 190, 160, 150])
x = np.arange(len(quarters))          # 0, 1, 2, 3
w = 0.38                              # 막대 폭

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.5))
ax1.bar(x - w / 2, online, width=w, label="온라인")     # 왼쪽으로 반 칸
ax1.bar(x + w / 2, offline, width=w, label="오프라인")  # 오른쪽으로 반 칸
ax1.set_xticks(x, quarters)
ax1.set_title("묶음 막대 (비교)")
ax1.legend()

ax2.bar(quarters, online, label="온라인")
ax2.bar(quarters, offline, bottom=online, label="오프라인")   # 위에 쌓기
ax2.set_title("누적 막대 (전체 + 구성)")
ax2.legend()
fig.savefig(IMG / "ex02_grouped_stacked.png", dpi=100, bbox_inches="tight")
plt.show()
