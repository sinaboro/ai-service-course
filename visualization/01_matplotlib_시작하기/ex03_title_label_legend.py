# ex03_title_label_legend.py : 그래프 꾸미기: 제목 · 축 이름 · 범례 · 격자 · 그림 크기
import platform                                  # 운영체제 이름 알아내기 (한글 글꼴 고를 때 사용)
from pathlib import Path                         # 파일 · 폴더 경로를 다루는 도구
import matplotlib.pyplot as plt                  # 그래프 도구 (관례적으로 plt 라는 별명)

# 한글 폰트 (Windows: 맑은 고딕, macOS: 애플고딕, 그 외: 나눔고딕)
plt.rcParams["font.family"] = {"Windows": "Malgun Gothic", "Darwin": "AppleGothic"}.get(platform.system(), "NanumGothic")
plt.rcParams["axes.unicode_minus"] = False        # 마이너스(-) 기호 깨짐 방지
IMG = Path(__file__).parent / "images"            # 그래프를 저장할 폴더
IMG.mkdir(exist_ok=True)                         # images 폴더 만들기 (이미 있으면 그냥 넘어가요)

months = ["1월", "2월", "3월", "4월", "5월", "6월"]
store_a = [120, 135, 150, 145, 170, 190]
store_b = [100, 110, 130, 160, 155, 175]

plt.figure(figsize=(8, 4.5))                     # 그림 크기 (가로, 세로 인치)
plt.plot(months, store_a, label="강남점")          # label → 범례에 표시될 이름
plt.plot(months, store_b, label="홍대점")
plt.title("지점별 월 매출", fontsize=16)
plt.xlabel("월")
plt.ylabel("매출 (만원)")
plt.legend()                                     # 범례 표시
plt.grid(True, alpha=0.3)                        # 연한 격자
plt.savefig(IMG / "ex03_title_label_legend.png", dpi=100, bbox_inches="tight")
plt.show()
