# ex06_dashboard.py : 미니 대시보드: gridspec 으로 크기가 다른 칸을 자유롭게 나누기
import platform                                   # 운영체제 이름 알아내기 (한글 글꼴 고를 때 사용)
from pathlib import Path                          # 파일 · 폴더 경로를 다루는 도구
import matplotlib.pyplot as plt                   # 그래프 도구 (관례적으로 plt 라는 별명)

# 한글 폰트 (Windows: 맑은 고딕, macOS: 애플고딕, 그 외: 나눔고딕)
plt.rcParams["font.family"] = {"Windows": "Malgun Gothic", "Darwin": "AppleGothic"}.get(platform.system(), "NanumGothic")
plt.rcParams["axes.unicode_minus"] = False        # 마이너스(-) 기호 깨짐 방지
IMG = Path(__file__).parent / "images"            # 그래프를 저장할 폴더
IMG.mkdir(exist_ok=True)                          # images 폴더 만들기 (이미 있으면 그냥 넘어가요)

import numpy as np                                # 넘파이 (관례적으로 np 라는 별명)

# 대시보드에 쓸 데이터 3가지: 30일 동안의 일별 매출, 메뉴별 판매량, 주문 시각 800건
rng = np.random.default_rng(seed=2026)
days = np.arange(1, 31)
sales = (200 + days * 3 + rng.normal(0, 25, 30)).round()
menu = {"커피": 420, "라떼": 310, "티": 150, "디저트": 220}
hour = rng.normal(14, 3, 800).clip(8, 22)

# 큰 도화지 하나에 칸을 자유롭게 나누기
fig = plt.figure(figsize=(12, 7))
grid = fig.add_gridspec(2, 3)                   # 2 x 3 격자
ax_main = fig.add_subplot(grid[0, :])           # 첫 줄 전체를 차지
ax_bar = fig.add_subplot(grid[1, 0])
ax_pie = fig.add_subplot(grid[1, 1])
ax_hist = fig.add_subplot(grid[1, 2])

# 윗줄: 일별 매출 선 + 선 아래를 옅게 칠하기(fill_between)
ax_main.plot(days, sales, marker=".", color="navy")
ax_main.fill_between(days, sales, alpha=0.15, color="navy")
ax_main.set_title(f"9월 일별 매출 (합계 {sales.sum():,.0f}만원)")
ax_main.set_xlabel("일")

# 아랫줄 왼쪽: 메뉴별 막대
ax_bar.bar(list(menu), list(menu.values()), color="teal")
ax_bar.set_title("메뉴별 판매량")
# 아랫줄 가운데: 원 그래프 (autopct: 비율 글자 표시)
ax_pie.pie(list(menu.values()), labels=list(menu), autopct="%.0f%%")
ax_pie.set_title("메뉴 비율")
# 아랫줄 오른쪽: 주문 시간대 히스토그램
ax_hist.hist(hour, bins=14, color="goldenrod", edgecolor="white")
ax_hist.set_title("주문 시간대 분포")
ax_hist.set_xlabel("시")

# 전체 제목 → 간격 정리 → 저장
fig.suptitle("카페 9월 판매 대시보드", fontsize=17, fontweight="bold")
fig.tight_layout()
fig.savefig(IMG / "ex06_dashboard.png", dpi=100, bbox_inches="tight")
print("대시보드 저장 완료")
plt.show()
