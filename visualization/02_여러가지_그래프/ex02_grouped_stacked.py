# ex02_grouped_stacked.py : 묶음 막대(나란히)와 누적 막대(쌓기)
import platform                                   # 운영체제 이름 알아내기 (한글 글꼴 고를 때 사용)
from pathlib import Path                          # 파일 · 폴더 경로를 다루는 도구
import matplotlib.pyplot as plt                   # 그래프 도구 (관례적으로 plt 라는 별명)

# 한글 폰트 (Windows: 맑은 고딕, macOS: 애플고딕, 그 외: 나눔고딕)
plt.rcParams["font.family"] = {"Windows": "Malgun Gothic", "Darwin": "AppleGothic"}.get(platform.system(), "NanumGothic")
plt.rcParams["axes.unicode_minus"] = False        # 마이너스(-) 기호 깨짐 방지
IMG = Path(__file__).parent / "images"            # 그래프를 저장할 폴더
IMG.mkdir(exist_ok=True)                          # images 폴더 만들기 (이미 있으면 그냥 넘어가요)

import numpy as np                                # 넘파이 (관례적으로 np 라는 별명)

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
