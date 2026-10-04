import platform
from pathlib import Path
import matplotlib.pyplot as plt

# 한글 폰트 (Windows: 맑은 고딕, macOS: 애플고딕, 그 외: 나눔고딕)
plt.rcParams["font.family"] = {"Windows": "Malgun Gothic", "Darwin": "AppleGothic"}.get(platform.system(), "NanumGothic")
plt.rcParams["axes.unicode_minus"] = False        # 마이너스(-) 기호 깨짐 방지
IMG = Path(__file__).parent / "images"            # 그래프를 저장할 폴더
IMG.mkdir(exist_ok=True)

days = list(range(1, 15))
temps = [12, 14, 13, 17, 19, 22, 21, 18, 16, 20, 24, 26, 23, 21]

plt.figure(figsize=(8, 4.5))
plt.plot(days, temps, marker="o", color="darkorange")
plt.xlim(0, 15)                                   # x 축 범위
plt.ylim(0, 30)                                   # y 축 범위
plt.xticks(days)                                  # x 축 눈금 위치
plt.axhline(20, color="gray", linestyle="--")     # y=20 가로 기준선
plt.text(1, 21, "20도 기준선", color="gray")       # 원하는 위치에 글자
best = days[temps.index(max(temps))]
plt.annotate(f"최고 {max(temps)}도", xy=(best, max(temps)), xytext=(best - 4, 28),
             arrowprops={"arrowstyle": "->"})      # 화살표 주석
plt.title("2주간 최고 기온")
plt.xlabel("날짜 (일)")
plt.ylabel("기온 (도)")
plt.savefig(IMG / "ex05_axis_range_text.png", dpi=100, bbox_inches="tight")
plt.show()
