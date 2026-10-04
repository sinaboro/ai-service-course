import platform
from pathlib import Path
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = {"Windows": "Malgun Gothic", "Darwin": "AppleGothic"}.get(platform.system(), "NanumGothic")
plt.rcParams["axes.unicode_minus"] = False
IMG = Path(__file__).parent / "images"            # 그림을 저장할 폴더
IMG.mkdir(exist_ok=True)

import matplotlib.patches as patches
import numpy as np

# 같은 장면으로 세 가지 문제 비교: 분류 · 객체 탐지 · 분할
scene = np.zeros((100, 160, 3))
scene[:60] = [0.55, 0.75, 0.9]       # 바다
scene[60:] = [0.95, 0.85, 0.6]       # 모래
scene[45:80, 30:42] = [0.35, 0.7, 0.35]     # 병
scene[55:75, 100:114] = [0.75, 0.75, 0.78]  # 캔

mask = np.zeros((100, 160, 3)) + 0.15
mask[45:80, 30:42] = [1, 0.2, 0.2]
mask[55:75, 100:114] = [1, 0.6, 0]

fig, axes = plt.subplots(1, 3, figsize=(12, 3.2))
axes[0].imshow(scene)
axes[0].set_title("① 분류: '쓰레기 있음' (사진 전체에 답 하나)")
axes[1].imshow(scene)
for (x, y, w, h, name, c) in [(28, 43, 16, 39, "bottle 0.91", "red"), (98, 53, 18, 24, "can 0.84", "orange")]:
    axes[1].add_patch(patches.Rectangle((x, y), w, h, fill=False, edgecolor=c, linewidth=2))
    axes[1].text(x, y - 3, name, color=c, fontsize=9)
axes[1].set_title("② 객체 탐지: 무엇이 · 어디에 (상자)")
axes[2].imshow(mask)
axes[2].set_title("③ 분할: 픽셀마다 무엇인지")
for ax in axes:
    ax.set_xticks([]); ax.set_yticks([])
fig.savefig(IMG / "ex04_ai_tasks.png", dpi=100, bbox_inches="tight")
print("저장: images/ex04_ai_tasks.png")
