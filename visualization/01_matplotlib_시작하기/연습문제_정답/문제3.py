# 문제 3. 두 도시의 월평균 기온(서울 [-2, 1, 6, 13, 19, 23], 부산 [3, 5, 9, 14, 18, 21], 1 ~ 6월)을 한 그래프에 다른 선 모양으로 그리고 범례를 붙이세요.

import platform
from pathlib import Path
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = {"Windows": "Malgun Gothic", "Darwin": "AppleGothic"}.get(platform.system(), "NanumGothic")
plt.rcParams["axes.unicode_minus"] = False
IMG = Path("images"); IMG.mkdir(exist_ok=True)

months = [f"{m}월" for m in range(1, 7)]
seoul = [-2, 1, 6, 13, 19, 23]
busan = [3, 5, 9, 14, 18, 21]
fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(months, seoul, "o-", label="서울")
ax.plot(months, busan, "s--", label="부산")
ax.axhline(0, color="gray", linewidth=0.8)
ax.set_title("월평균 기온")
ax.set_ylabel("기온 (도)")
ax.legend()
fig.savefig(IMG / "q3_temps.png", dpi=100, bbox_inches="tight")
print("저장 완료")
