# ex04_line_style.py : 선 모양 꾸미기: 색(color) · 선 종류(linestyle) · 점 모양(marker)
import platform                                   # 운영체제 이름 알아내기 (한글 글꼴 고를 때 사용)
from pathlib import Path                          # 파일 · 폴더 경로를 다루는 도구
import matplotlib.pyplot as plt                   # 그래프 도구 (관례적으로 plt 라는 별명)

# 한글 폰트 (Windows: 맑은 고딕, macOS: 애플고딕, 그 외: 나눔고딕)
plt.rcParams["font.family"] = {"Windows": "Malgun Gothic", "Darwin": "AppleGothic"}.get(platform.system(), "NanumGothic")
plt.rcParams["axes.unicode_minus"] = False        # 마이너스(-) 기호 깨짐 방지
IMG = Path(__file__).parent / "images"            # 그래프를 저장할 폴더
IMG.mkdir(exist_ok=True)                          # images 폴더 만들기 (이미 있으면 그냥 넘어가요)

# x = 1 ~ 10, 기울기가 다른 세 직선의 y 값
x = list(range(1, 11))
a = [v * 1 for v in x]                            # x 의 각 값 × 1
b = [v * 1.5 for v in x]                          # x 의 각 값 × 1.5
c = [v * 2 for v in x]                            # x 의 각 값 × 2

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
