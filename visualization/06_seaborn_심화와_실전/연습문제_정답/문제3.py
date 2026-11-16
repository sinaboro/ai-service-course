# 문제 3. data/students_life.csv로 catplot(kind="bar")을 이용해 학년(col)별 동아리 평균 점수를 칸으로 나눠 그리세요.

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

df = pd.read_csv(DATA / "students_life.csv")
g = sns.catplot(data=df, x="club", y="score", col="grade", kind="bar", errorbar=None,
                col_order=["1학년", "2학년", "3학년"], height=3.5)
g.set_titles("{col_name}")
g.savefig(IMG / "q3_grade_club.png", dpi=100, bbox_inches="tight")
print(df.groupby(["grade", "club"])["score"].mean().round(1).unstack())
