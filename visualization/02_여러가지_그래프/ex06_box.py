import platform
from pathlib import Path
import matplotlib.pyplot as plt

# 한글 폰트 (Windows: 맑은 고딕, macOS: 애플고딕, 그 외: 나눔고딕)
plt.rcParams["font.family"] = {"Windows": "Malgun Gothic", "Darwin": "AppleGothic"}.get(platform.system(), "NanumGothic")
plt.rcParams["axes.unicode_minus"] = False        # 마이너스(-) 기호 깨짐 방지
IMG = Path(__file__).parent / "images"            # 그래프를 저장할 폴더
IMG.mkdir(exist_ok=True)

import numpy as np

rng = np.random.default_rng(seed=3)
class_a = rng.normal(75, 8, 40).clip(0, 100)       # 0 ~ 100점 범위로 자르기
class_b = rng.normal(70, 15, 40).clip(0, 100)
class_c = np.append(rng.normal(80, 5, 38), [40, 45])     # 낮은 점수 2명 (이상치)

fig, ax = plt.subplots(figsize=(8, 4.5))
ax.boxplot([class_a, class_b, class_c], tick_labels=["A반", "B반", "C반"])
ax.set_title("반별 점수 분포 (상자 그래프)")
ax.set_ylabel("점수")
fig.savefig(IMG / "ex06_box.png", dpi=100, bbox_inches="tight")
for name, d in zip("ABC", [class_a, class_b, class_c]):
    print(f"{name}반 중앙값 {np.median(d):.1f}")
plt.show()
