import platform
from pathlib import Path
import matplotlib.pyplot as plt

# 한글 폰트 (Windows: 맑은 고딕, macOS: 애플고딕, 그 외: 나눔고딕)
plt.rcParams["font.family"] = {"Windows": "Malgun Gothic", "Darwin": "AppleGothic"}.get(platform.system(), "NanumGothic")
plt.rcParams["axes.unicode_minus"] = False        # 마이너스(-) 기호 깨짐 방지
IMG = Path(__file__).parent / "images"            # 그래프를 저장할 폴더
IMG.mkdir(exist_ok=True)

labels = ["교통", "식비", "주거", "여가", "기타"]
money = [15, 35, 30, 12, 8]

fig, ax = plt.subplots(figsize=(6, 6))
ax.pie(money, labels=labels, autopct="%.1f%%", startangle=90,
       explode=[0, 0.08, 0, 0, 0])          # 식비 조각만 살짝 떼기
ax.set_title("한 달 지출 비율")
fig.savefig(IMG / "ex05_pie.png", dpi=100, bbox_inches="tight")
plt.show()
