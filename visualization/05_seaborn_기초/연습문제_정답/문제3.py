# 문제 3. 요일별 계산 금액 합계를 barplot으로 그리세요. (힌트: estimator="sum", errorbar=None)

import platform
from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
sns.set_theme(style="whitegrid")
plt.rcParams["font.family"] = {"Windows": "Malgun Gothic", "Darwin": "AppleGothic"}.get(platform.system(), "NanumGothic")
plt.rcParams["axes.unicode_minus"] = False
IMG = Path("images"); IMG.mkdir(exist_ok=True)
# 이 파일은 연습문제_정답 폴더 안에 있어요 → 한 단계 위(장 폴더)의 data 폴더를 가리켜요
# (▶ 버튼 · 터미널 어디서 실행해도 CSV 를 찾을 수 있어요)
DATA = Path(__file__).parent.parent / "data"
tips = pd.read_csv(DATA / "tips.csv")

order = ["Thur", "Fri", "Sat", "Sun"]
ax = sns.barplot(data=tips, x="day", y="total_bill", order=order, estimator="sum", errorbar=None, color="salmon")
ax.bar_label(ax.containers[0], fmt="%.0f")
ax.set_title("요일별 계산 금액 합계 ($)")
ax.figure.savefig(IMG / "q3_day_sum.png", dpi=100, bbox_inches="tight")
print(tips.groupby("day")["total_bill"].sum().reindex(order).round(0).tolist())
