import platform
from pathlib import Path
import matplotlib.pyplot as plt

# 한글 폰트 (Windows: 맑은 고딕, macOS: 애플고딕, 그 외: 나눔고딕)
plt.rcParams["font.family"] = {"Windows": "Malgun Gothic", "Darwin": "AppleGothic"}.get(platform.system(), "NanumGothic")
plt.rcParams["axes.unicode_minus"] = False        # 마이너스(-) 기호 깨짐 방지
IMG = Path(__file__).parent / "images"            # 그래프를 저장할 폴더
IMG.mkdir(exist_ok=True)

# x = 1 ~ 10, 기울기가 다른 세 직선의 y 값
x = list(range(1, 11))
a = [v * 1 for v in x]
b = [v * 1.5 for v in x]
c = [v * 2 for v in x]

# 그림 크기: 가로 8인치 × 세로 4.5인치
plt.figure(figsize=(8, 4.5))
# color 색, linestyle 선 모양("-" 실선, "--" 점선, ":" 짧은 점선), marker 점 모양, label 범례 이름
plt.plot(x, a, color="royalblue", linestyle="-", marker="o", label="실선 + 원")
plt.plot(x, b, color="tomato", linestyle="--", marker="s", label="점선 + 네모")
# "g:^" = 초록(g) + 짧은 점선(:) + 삼각형 점(^) 을 한 번에
plt.plot(x, c, "g:^", linewidth=2, markersize=8, label="'g:^' 짧게 쓰기")
plt.title("선 색 · 모양 · 점 표시")
# label 을 모아 범례 상자 만들기
plt.legend()
plt.savefig(IMG / "ex04_line_style.png", dpi=100, bbox_inches="tight")
plt.show()
