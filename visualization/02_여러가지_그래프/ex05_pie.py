# ex05_pie.py : 원 그래프: 전체에서 각 부분의 비율 (autopct 로 % 표시)
import platform                                   # 운영체제 이름 알아내기 (한글 글꼴 고를 때 사용)
from pathlib import Path                          # 파일 · 폴더 경로를 다루는 도구
import matplotlib.pyplot as plt                   # 그래프 도구 (관례적으로 plt 라는 별명)

# 한글 폰트 (Windows: 맑은 고딕, macOS: 애플고딕, 그 외: 나눔고딕)
plt.rcParams["font.family"] = {"Windows": "Malgun Gothic", "Darwin": "AppleGothic"}.get(platform.system(), "NanumGothic")
plt.rcParams["axes.unicode_minus"] = False        # 마이너스(-) 기호 깨짐 방지
IMG = Path(__file__).parent / "images"            # 그래프를 저장할 폴더
IMG.mkdir(exist_ok=True)                          # images 폴더 만들기 (이미 있으면 그냥 넘어가요)

labels = ["교통", "식비", "주거", "여가", "기타"]
money = [15, 35, 30, 12, 8]

fig, ax = plt.subplots(figsize=(6, 6))
ax.pie(money, labels=labels, autopct="%.1f%%", startangle=90,
       explode=[0, 0.08, 0, 0, 0])          # 식비 조각만 살짝 떼기
ax.set_title("한 달 지출 비율")
fig.savefig(IMG / "ex05_pie.png", dpi=100, bbox_inches="tight")
plt.show()
