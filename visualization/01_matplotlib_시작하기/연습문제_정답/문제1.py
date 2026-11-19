# 문제 1. 1 ~ 10의 x에 대해 y = x²(제곱) 선 그래프를 그리고 제목 "제곱 그래프"를 붙여 images/q1_square.png로 저장하세요.

import platform  # 운영체제 이름 알아내기 (한글 글꼴 고를 때 사용)
from pathlib import Path  # 파일 · 폴더 경로를 다루는 도구
import matplotlib.pyplot as plt  # 그래프 도구 (관례적으로 plt 라는 별명)
plt.rcParams["font.family"] = {"Windows": "Malgun Gothic", "Darwin": "AppleGothic"}.get(platform.system(), "NanumGothic")
plt.rcParams["axes.unicode_minus"] = False  # 마이너스(-) 기호가 네모로 깨지지 않게
IMG = Path("images"); IMG.mkdir(exist_ok=True)

x = list(range(1, 11))
y = [v ** 2 for v in x]  # x 의 각 값을 제곱
plt.plot(x, y, marker="o")
plt.title("제곱 그래프")
plt.xlabel("x")
plt.ylabel("x의 제곱")
plt.savefig(IMG / "q1_square.png", dpi=100, bbox_inches="tight")
print("저장:", (IMG / "q1_square.png").exists())
