# ex06_two_styles.py : 같은 그래프를 plt 방식과 fig, ax 방식으로 각각 그려 비교하기
import platform                                   # 운영체제 이름 알아내기 (한글 글꼴 고를 때 사용)
from pathlib import Path                          # 파일 · 폴더 경로를 다루는 도구
import matplotlib.pyplot as plt                   # 그래프 도구 (관례적으로 plt 라는 별명)

# 한글 폰트 (Windows: 맑은 고딕, macOS: 애플고딕, 그 외: 나눔고딕)
plt.rcParams["font.family"] = {"Windows": "Malgun Gothic", "Darwin": "AppleGothic"}.get(platform.system(), "NanumGothic")
plt.rcParams["axes.unicode_minus"] = False        # 마이너스(-) 기호 깨짐 방지
IMG = Path(__file__).parent / "images"            # 그래프를 저장할 폴더
IMG.mkdir(exist_ok=True)                          # images 폴더 만들기 (이미 있으면 그냥 넘어가요)

# 같은 데이터로 두 방식 비교
x = [1, 2, 3, 4, 5]
y = [2, 4, 3, 6, 5]

# 방법 1: plt 방식 (간단한 그래프 1개)
plt.figure(figsize=(4, 3))
plt.plot(x, y)
plt.title("plt 방식")
plt.savefig(IMG / "ex06_plt_style.png", dpi=100, bbox_inches="tight")
# plt.close(): 다음 그림과 섞이지 않게 지금 그림 닫기
plt.close()

# 방법 2: fig, ax 방식 (여러 그래프, 세밀한 조정) ← 앞으로 주로 사용
# fig = 그림 전체(도화지), ax = 그래프 한 칸 → ax.set_title 처럼 칸에 직접 명령
fig, ax = plt.subplots(figsize=(4, 3))
ax.plot(x, y, color="purple")
ax.set_title("fig, ax 방식")
ax.set_xlabel("x 값")
ax.set_ylabel("y 값")
fig.savefig(IMG / "ex06_ax_style.png", dpi=100, bbox_inches="tight")
print(type(fig).__name__, type(ax).__name__)
plt.show()
