# 문제 1. 1 ~ 10의 x에 대해 y = x²(제곱) 선 그래프를 그리고 제목 "제곱 그래프"를 붙여 images/q1_square.png로 저장하세요.

import platform
from pathlib import Path
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = {"Windows": "Malgun Gothic", "Darwin": "AppleGothic"}.get(platform.system(), "NanumGothic")
plt.rcParams["axes.unicode_minus"] = False
IMG = Path("images"); IMG.mkdir(exist_ok=True)

x = list(range(1, 11))
y = [v ** 2 for v in x]
plt.plot(x, y, marker="o")
plt.title("제곱 그래프")
plt.xlabel("x")
plt.ylabel("x의 제곱")
plt.savefig(IMG / "q1_square.png", dpi=100, bbox_inches="tight")
print("저장:", (IMG / "q1_square.png").exists())
