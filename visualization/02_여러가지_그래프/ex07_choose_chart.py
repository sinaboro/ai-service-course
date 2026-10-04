import platform
from pathlib import Path
import matplotlib.pyplot as plt

# 한글 폰트 (Windows: 맑은 고딕, macOS: 애플고딕, 그 외: 나눔고딕)
plt.rcParams["font.family"] = {"Windows": "Malgun Gothic", "Darwin": "AppleGothic"}.get(platform.system(), "NanumGothic")
plt.rcParams["axes.unicode_minus"] = False        # 마이너스(-) 기호 깨짐 방지
IMG = Path(__file__).parent / "images"            # 그래프를 저장할 폴더
IMG.mkdir(exist_ok=True)

import numpy as np

rng = np.random.default_rng(seed=5)
# 2행 × 3열 = 그래프 6칸. axes[행, 열] 로 칸을 골라요
fig, axes = plt.subplots(2, 3, figsize=(12, 7))
# 윗줄: 선(변화) · 막대(비교) · 히스토그램(분포)
axes[0, 0].plot([1, 2, 3, 4, 5], [3, 5, 4, 7, 8], marker="o")
axes[0, 0].set_title("선: 시간에 따른 변화")
axes[0, 1].bar(["A", "B", "C"], [5, 8, 3])
axes[0, 1].set_title("막대: 항목 비교")
axes[0, 2].hist(rng.normal(0, 1, 200), bins=15)
axes[0, 2].set_title("히스토그램: 분포")
# 아랫줄: 산점도(관계) · 원(비율) · 상자(그룹별 분포)
x = rng.uniform(0, 10, 40)
axes[1, 0].scatter(x, x * 2 + rng.normal(0, 2, 40))
axes[1, 0].set_title("산점도: 두 값의 관계")
axes[1, 1].pie([40, 35, 25], labels=["가", "나", "다"], autopct="%d%%")
axes[1, 1].set_title("원: 전체 중 비율")
axes[1, 2].boxplot([rng.normal(5, 1, 50), rng.normal(6, 2, 50)])
axes[1, 2].set_title("상자: 그룹별 분포")
# 전체 제목 + 칸끼리 겹치지 않게 간격 자동 조정
fig.suptitle("데이터에 맞는 그래프 고르기", fontsize=16)
fig.tight_layout()
fig.savefig(IMG / "ex07_choose_chart.png", dpi=100, bbox_inches="tight")
plt.show()
