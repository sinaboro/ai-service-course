import platform
from pathlib import Path
import matplotlib.pyplot as plt

# 한글 폰트 (Windows: 맑은 고딕, macOS: 애플고딕, 그 외: 나눔고딕)
plt.rcParams["font.family"] = {"Windows": "Malgun Gothic", "Darwin": "AppleGothic"}.get(platform.system(), "NanumGothic")
plt.rcParams["axes.unicode_minus"] = False        # 마이너스(-) 기호 깨짐 방지
IMG = Path(__file__).parent / "images"            # 그래프를 저장할 폴더
IMG.mkdir(exist_ok=True)

x = list(range(1, 11))
a = [v * 1 for v in x]
b = [v * 1.5 for v in x]
c = [v * 2 for v in x]

plt.figure(figsize=(8, 4.5))
plt.plot(x, a, color="royalblue", linestyle="-", marker="o", label="실선 + 원")
plt.plot(x, b, color="tomato", linestyle="--", marker="s", label="점선 + 네모")
plt.plot(x, c, "g:^", linewidth=2, markersize=8, label="'g:^' 짧게 쓰기")
plt.title("선 색 · 모양 · 점 표시")
plt.legend()
plt.savefig(IMG / "ex04_line_style.png", dpi=100, bbox_inches="tight")
plt.show()
