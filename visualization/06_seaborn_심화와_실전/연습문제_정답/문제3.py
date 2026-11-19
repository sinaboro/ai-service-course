# 문제 3. data/students_life.csv로 catplot(kind="bar")을 이용해 학년(col)별 동아리 평균 점수를 칸으로 나눠 그리세요.

import platform  # 운영체제 이름 알아내기 (한글 글꼴 고를 때 사용)
from pathlib import Path  # 파일 · 폴더 경로를 다루는 도구
import matplotlib.pyplot as plt  # 그래프 도구 (관례적으로 plt 라는 별명)
import pandas as pd  # 판다스 (관례적으로 pd 라는 별명)
import seaborn as sns  # 시본: 통계 그래프 도구 (관례적으로 sns)
sns.set_theme(style="whitegrid")
plt.rcParams["font.family"] = {"Windows": "Malgun Gothic", "Darwin": "AppleGothic"}.get(platform.system(), "NanumGothic")
plt.rcParams["axes.unicode_minus"] = False  # 마이너스(-) 기호가 네모로 깨지지 않게
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
