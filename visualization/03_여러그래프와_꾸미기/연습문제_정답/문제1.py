# 문제 1. 1행 2열 subplots로 왼쪽에는 [10, 20, 15, 30] 선 그래프, 오른쪽에는 같은 값의 막대 그래프를 그리고 전체 제목 "같은 데이터, 다른 그래프"를 붙이세요.

import platform  # 운영체제 이름 알아내기 (한글 글꼴 고를 때 사용)
from pathlib import Path  # 파일 · 폴더 경로를 다루는 도구
import matplotlib.pyplot as plt  # 그래프 도구 (관례적으로 plt 라는 별명)
plt.rcParams["font.family"] = {"Windows": "Malgun Gothic", "Darwin": "AppleGothic"}.get(platform.system(), "NanumGothic")
plt.rcParams["axes.unicode_minus"] = False  # 마이너스(-) 기호가 네모로 깨지지 않게
IMG = Path("images"); IMG.mkdir(exist_ok=True)

labels = ["1주", "2주", "3주", "4주"]
data = [10, 20, 15, 30]
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 3.5))
ax1.plot(labels, data, marker="o")
ax1.set_title("선 그래프")
ax2.bar(labels, data, color="orange")
ax2.set_title("막대 그래프")
fig.suptitle("같은 데이터, 다른 그래프")
fig.tight_layout()
fig.savefig(IMG / "q1_same_data.png", dpi=100, bbox_inches="tight")
print("저장 완료")
