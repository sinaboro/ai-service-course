# 문제 2. 3개 지점의 분기별 매출(강남 [50, 60, 70, 65], 홍대 [40, 55, 50, 70], 잠실 [30, 35, 45, 50])을 1행 3열에 sharey=True로 그리고, 각 칸 제목을 지점 이름으로 하세요.

import platform  # 운영체제 이름 알아내기 (한글 글꼴 고를 때 사용)
from pathlib import Path  # 파일 · 폴더 경로를 다루는 도구
import matplotlib.pyplot as plt  # 그래프 도구 (관례적으로 plt 라는 별명)
plt.rcParams["font.family"] = {"Windows": "Malgun Gothic", "Darwin": "AppleGothic"}.get(platform.system(), "NanumGothic")
plt.rcParams["axes.unicode_minus"] = False  # 마이너스(-) 기호가 네모로 깨지지 않게
IMG = Path("images"); IMG.mkdir(exist_ok=True)

data = {"강남": [50, 60, 70, 65], "홍대": [40, 55, 50, 70], "잠실": [30, 35, 45, 50]}
q = ["1분기", "2분기", "3분기", "4분기"]
fig, axes = plt.subplots(1, 3, figsize=(11, 3.5), sharey=True)
for ax, (name, vals) in zip(axes, data.items()):  # 칸과 (지점, 매출)을 짝지어 꺼내기
    ax.bar(q, vals, color="slateblue")
    ax.set_title(name)
fig.supylabel("매출 (백만 원)")
fig.tight_layout()
fig.savefig(IMG / "q2_branches.png", dpi=100, bbox_inches="tight")
print("저장 완료")
