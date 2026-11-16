# 문제 1. tips 데이터에서 인원(size)별 손님 수를 countplot으로 그리고 막대 위에 개수를 표시하세요.

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

ax = sns.countplot(data=tips, x="size", color="steelblue")
ax.bar_label(ax.containers[0])
ax.set_title("인원별 손님 수")
ax.figure.savefig(IMG / "q1_size_count.png", dpi=100, bbox_inches="tight")
print(tips["size"].value_counts().sort_index().tolist())
