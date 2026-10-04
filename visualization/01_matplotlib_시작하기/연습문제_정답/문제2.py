# 문제 2. 요일별 걸음 수 월 8000, 화 12000, 수 6500, 목 10000, 금 9000을 선 그래프로 그리고, 목표 10000보를 빨간 점선 가로선으로 표시하세요.

import platform
from pathlib import Path
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = {"Windows": "Malgun Gothic", "Darwin": "AppleGothic"}.get(platform.system(), "NanumGothic")
plt.rcParams["axes.unicode_minus"] = False
IMG = Path("images"); IMG.mkdir(exist_ok=True)

days = ["월", "화", "수", "목", "금"]
steps = [8000, 12000, 6500, 10000, 9000]
fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(days, steps, marker="o", label="걸음 수")
ax.axhline(10000, color="red", linestyle="--", label="목표")
ax.set_title("요일별 걸음 수")
ax.legend()
fig.savefig(IMG / "q2_steps.png", dpi=100, bbox_inches="tight")
print("저장 완료")
