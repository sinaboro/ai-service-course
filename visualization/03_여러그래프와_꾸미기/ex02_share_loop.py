# ex02_share_loop.py : 축 공유(sharey)와 반복문으로 칸마다 그래프 그리기
import platform                                   # 운영체제 이름 알아내기 (한글 글꼴 고를 때 사용)
from pathlib import Path                          # 파일 · 폴더 경로를 다루는 도구
import matplotlib.pyplot as plt                   # 그래프 도구 (관례적으로 plt 라는 별명)

# 한글 폰트 (Windows: 맑은 고딕, macOS: 애플고딕, 그 외: 나눔고딕)
plt.rcParams["font.family"] = {"Windows": "Malgun Gothic", "Darwin": "AppleGothic"}.get(platform.system(), "NanumGothic")
plt.rcParams["axes.unicode_minus"] = False        # 마이너스(-) 기호 깨짐 방지
IMG = Path(__file__).parent / "images"            # 그래프를 저장할 폴더
IMG.mkdir(exist_ok=True)                          # images 폴더 만들기 (이미 있으면 그냥 넘어가요)

# 도시 이름: 1 ~ 6월 기온 / x 축용 월 이름
cities = {"서울": [-2, 1, 6, 13, 19, 23], "부산": [3, 5, 9, 14, 18, 21],
          "대구": [0, 3, 8, 15, 20, 24], "강릉": [0, 2, 6, 12, 17, 21]}
months = [f"{m}월" for m in range(1, 7)]

fig, axes = plt.subplots(2, 2, figsize=(10, 6), sharex=True, sharey=True)  # 축 공유
for ax, (city, temps) in zip(axes.flat, cities.items()):                      # 칸을 하나씩
    ax.plot(months, temps, marker="o")
    # 0도 기준선 (영하인지 쉽게 보기)
    ax.axhline(0, color="gray", linewidth=0.8)
    ax.set_title(city)
# 그림 전체의 제목과 공통 y 축 이름
fig.suptitle("도시별 월평균 기온 (같은 눈금으로 비교)")
fig.supylabel("기온 (도)")
fig.tight_layout()
fig.savefig(IMG / "ex02_share_loop.png", dpi=100, bbox_inches="tight")
plt.show()
