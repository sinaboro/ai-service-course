# ex01_bar.py : 막대 그래프: 세로(bar) · 가로(barh), 막대 위에 값 표시
import platform                                   # 운영체제 이름 알아내기 (한글 글꼴 고를 때 사용)
from pathlib import Path                          # 파일 · 폴더 경로를 다루는 도구
import matplotlib.pyplot as plt                   # 그래프 도구 (관례적으로 plt 라는 별명)

# 한글 폰트 (Windows: 맑은 고딕, macOS: 애플고딕, 그 외: 나눔고딕)
plt.rcParams["font.family"] = {"Windows": "Malgun Gothic", "Darwin": "AppleGothic"}.get(platform.system(), "NanumGothic")
plt.rcParams["axes.unicode_minus"] = False        # 마이너스(-) 기호 깨짐 방지
IMG = Path(__file__).parent / "images"            # 그래프를 저장할 폴더
IMG.mkdir(exist_ok=True)                          # images 폴더 만들기 (이미 있으면 그냥 넘어가요)

menus = ["아메리카노", "카페라떼", "바닐라라떼", "녹차", "케이크"]
sales = [125, 88, 64, 30, 47]

fig, ax = plt.subplots(figsize=(8, 4.5))
bars = ax.bar(menus, sales, color="cornflowerblue")     # 세로 막대
ax.bar_label(bars)                                      # 막대 위에 값 표시
ax.set_title("메뉴별 판매량")
ax.set_ylabel("판매량 (잔)")
fig.savefig(IMG / "ex01_bar.png", dpi=100, bbox_inches="tight")

# 가로 막대: 이름이 길거나 항목이 많을 때, 큰 순서로 정렬해서
pairs = sorted(zip(sales, menus))
fig, ax = plt.subplots(figsize=(8, 4.5))
ax.barh([m for s, m in pairs], [s for s, m in pairs], color="salmon")  # 이름 목록, 값 목록
ax.set_title("메뉴별 판매량 (가로 막대, 정렬)")
ax.set_xlabel("판매량 (잔)")
fig.savefig(IMG / "ex01_barh.png", dpi=100, bbox_inches="tight")
plt.show()
