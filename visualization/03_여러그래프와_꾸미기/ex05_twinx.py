# ex05_twinx.py : 두 개의 y축(twinx): 단위가 다른 두 값을 한 그래프에
import platform                                   # 운영체제 이름 알아내기 (한글 글꼴 고를 때 사용)
from pathlib import Path                          # 파일 · 폴더 경로를 다루는 도구
import matplotlib.pyplot as plt                   # 그래프 도구 (관례적으로 plt 라는 별명)

# 한글 폰트 (Windows: 맑은 고딕, macOS: 애플고딕, 그 외: 나눔고딕)
plt.rcParams["font.family"] = {"Windows": "Malgun Gothic", "Darwin": "AppleGothic"}.get(platform.system(), "NanumGothic")
plt.rcParams["axes.unicode_minus"] = False        # 마이너스(-) 기호 깨짐 방지
IMG = Path(__file__).parent / "images"            # 그래프를 저장할 폴더
IMG.mkdir(exist_ok=True)                          # images 폴더 만들기 (이미 있으면 그냥 넘어가요)

months = [f"{m}월" for m in range(1, 7)]
visitors = [3200, 4100, 3900, 5200, 6100, 5800]     # 방문자 수 (명)
conversion = [2.1, 2.4, 2.2, 2.9, 3.4, 3.1]          # 구매 전환율 (%)

fig, ax1 = plt.subplots(figsize=(8, 4.5))
ax1.bar(months, visitors, color="lightsteelblue", label="방문자 수")
ax1.set_ylabel("방문자 수 (명)", color="steelblue")

ax2 = ax1.twinx()                                    # 같은 x 축, 오른쪽에 새 y 축
ax2.plot(months, conversion, color="crimson", marker="o", label="전환율")
ax2.set_ylabel("전환율 (%)", color="crimson")
ax2.set_ylim(0, 4)

lines = ax1.get_legend_handles_labels()
lines2 = ax2.get_legend_handles_labels()
ax1.legend(lines[0] + lines2[0], lines[1] + lines2[1], loc="upper left")   # 범례 합치기
ax1.set_title("방문자 수와 구매 전환율")
fig.savefig(IMG / "ex05_twinx.png", dpi=100, bbox_inches="tight")
plt.show()
