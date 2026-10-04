import platform
from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

sns.set_theme(style="whitegrid")             # seaborn 기본 스타일
# ⚠ set_theme 은 글꼴을 초기화하므로 한글 글꼴은 "그 다음에" 설정
plt.rcParams["font.family"] = {"Windows": "Malgun Gothic", "Darwin": "AppleGothic"}.get(platform.system(), "NanumGothic")
plt.rcParams["axes.unicode_minus"] = False

HERE = Path(__file__).parent
IMG = HERE / "images"; IMG.mkdir(exist_ok=True)
tips = pd.read_csv(HERE / "data" / "tips.csv")   # 식당 팁 데이터 (244건)

import numpy as np

# 연습 데이터: 지점 3곳 × 12주 × 7일. 주가 지날수록 조금씩 늘어나는 매출 + 잡음
rng = np.random.default_rng(seed=10)
rows = []
for store, base in [("강남", 120), ("홍대", 100), ("잠실", 85)]:
    for week in range(1, 13):
        for day in range(7):                   # 주마다 7일치
            rows.append({"store": store, "week": week,
                         "sales": base + week * 4 + rng.normal(0, 12)})
daily = pd.DataFrame(rows)
print(daily.shape)

# 같은 주의 7일 값을 평균한 선 + 그림자(신뢰구간)를 seaborn 이 자동으로
fig, ax = plt.subplots(figsize=(9, 4.5))
sns.lineplot(data=daily, x="week", y="sales", hue="store", marker="o", ax=ax)   # 평균 선 + 범위
ax.set_title("주차별 일 평균 매출 (그림자 = 95% 신뢰구간)")
ax.set_xlabel("주차")
ax.set_ylabel("매출 (만원)")
fig.savefig(IMG / "ex07_lineplot.png", dpi=100, bbox_inches="tight")
plt.show()
