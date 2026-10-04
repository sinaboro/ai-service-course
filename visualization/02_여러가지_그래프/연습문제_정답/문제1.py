# 문제 1. 과목별 평균 국어 78, 영어 85, 수학 72, 과학 80을 세로 막대로 그리고 막대 위에 값을 표시하세요.

import platform
from pathlib import Path
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = {"Windows": "Malgun Gothic", "Darwin": "AppleGothic"}.get(platform.system(), "NanumGothic")
plt.rcParams["axes.unicode_minus"] = False
IMG = Path("images"); IMG.mkdir(exist_ok=True)

subjects = ["국어", "영어", "수학", "과학"]
avg = [78, 85, 72, 80]
fig, ax = plt.subplots(figsize=(6, 4))
bars = ax.bar(subjects, avg, color="teal")
ax.bar_label(bars)
ax.set_ylim(0, 100)
ax.set_title("과목별 평균")
fig.savefig(IMG / "q1_subject_bar.png", dpi=100, bbox_inches="tight")
print("저장 완료")
