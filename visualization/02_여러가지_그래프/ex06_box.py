# ex06_box.py : 상자 그래프: 반별 점수의 중앙값 · 퍼짐 · 이상치 비교
import platform                                   # 운영체제 이름 알아내기 (한글 글꼴 고를 때 사용)
from pathlib import Path                          # 파일 · 폴더 경로를 다루는 도구
import matplotlib.pyplot as plt                   # 그래프 도구 (관례적으로 plt 라는 별명)

# 한글 폰트 (Windows: 맑은 고딕, macOS: 애플고딕, 그 외: 나눔고딕)
plt.rcParams["font.family"] = {"Windows": "Malgun Gothic", "Darwin": "AppleGothic"}.get(platform.system(), "NanumGothic")
plt.rcParams["axes.unicode_minus"] = False        # 마이너스(-) 기호 깨짐 방지
IMG = Path(__file__).parent / "images"            # 그래프를 저장할 폴더
IMG.mkdir(exist_ok=True)                          # images 폴더 만들기 (이미 있으면 그냥 넘어가요)

import numpy as np                                # 넘파이 (관례적으로 np 라는 별명)

# 세 반의 점수: C반에는 일부러 아주 낮은 점수 2개(이상치)를 넣었어요
rng = np.random.default_rng(seed=3)
class_a = rng.normal(75, 8, 40).clip(0, 100)       # 0 ~ 100점 범위로 자르기
class_b = rng.normal(70, 15, 40).clip(0, 100)
class_c = np.append(rng.normal(80, 5, 38), [40, 45])     # 낮은 점수 2명 (이상치)

fig, ax = plt.subplots(figsize=(8, 4.5))
# 상자 그래프: 가운데 선 = 중앙값, 상자 = 가운데 50%, 동그라미 = 이상치
ax.boxplot([class_a, class_b, class_c], tick_labels=["A반", "B반", "C반"])
ax.set_title("반별 점수 분포 (상자 그래프)")
ax.set_ylabel("점수")
fig.savefig(IMG / "ex06_box.png", dpi=100, bbox_inches="tight")
# 반마다 중앙값 출력 ("ABC" 는 글자 A, B, C 를 차례로 꺼내요)
for name, d in zip("ABC", [class_a, class_b, class_c]):
    print(f"{name}반 중앙값 {np.median(d):.1f}")
plt.show()
