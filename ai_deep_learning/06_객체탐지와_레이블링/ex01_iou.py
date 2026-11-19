# ex01_iou.py : IoU: 정답 상자와 예측 상자가 얼마나 겹치는지 계산하고 그려 보기
import platform                                          # 운영체제 이름 알아내기 (한글 글꼴 고를 때 사용)
from pathlib import Path                                 # 파일 · 폴더 경로를 다루는 도구
import matplotlib.pyplot as plt                          # 그래프 도구 (관례적으로 plt 라는 별명)

# 그래프 한글 글꼴: 운영체제에 따라 알맞은 글꼴 고르기 (Windows = 맑은 고딕)
plt.rcParams["font.family"] = {"Windows": "Malgun Gothic", "Darwin": "AppleGothic"}.get(platform.system(), "NanumGothic")
# 마이너스(-) 기호가 네모로 깨지지 않게
plt.rcParams["axes.unicode_minus"] = False               # 마이너스(-) 기호가 네모로 깨지지 않게
IMG = Path(__file__).parent / "images"            # 그림을 저장할 폴더
IMG.mkdir(exist_ok=True)                                 # images 폴더 만들기 (이미 있으면 그냥 넘어가요)

import matplotlib.patches as patches


def iou(a, b):
    """상자 a, b = (x1, y1, x2, y2). 겹친 넓이 / 합친 넓이"""
    ix1, iy1 = max(a[0], b[0]), max(a[1], b[1])          # 겹친 부분의 왼쪽 위
    ix2, iy2 = min(a[2], b[2]), min(a[3], b[3])          # 겹친 부분의 오른쪽 아래
    inter = max(0, ix2 - ix1) * max(0, iy2 - iy1)        # 안 겹치면 0
    area_a = (a[2] - a[0]) * (a[3] - a[1])
    area_b = (b[2] - b[0]) * (b[3] - b[1])
    return inter / (area_a + area_b - inter)


# 정답 상자 하나와 예측 상자 세 경우를 비교
truth = (40, 40, 140, 160)                               # 정답 상자 (사람이 레이블링)
cases = {"거의 맞음": (45, 50, 145, 165), "절반쯤": (80, 70, 180, 190), "빗나감": (150, 40, 230, 150)}
fig, axes = plt.subplots(1, 3, figsize=(11, 3.6))
# 경우마다 IoU 계산 → 0.5 이상이면 맞힌 것(TP)으로 쳐요
for ax, (name, pred) in zip(axes, cases.items()):
    v = iou(truth, pred)
    print(f"{name:6s} 예측 {pred} → IoU {v:.2f}", "→ 맞힘 (TP)" if v >= 0.5 else "→ 틀림 (FP)")
    # 초록 = 정답, 빨강 = 예측 상자 그리기
    for box, color, label in [(truth, "green", "정답"), (pred, "red", "예측")]:
        ax.add_patch(patches.Rectangle(box[:2], box[2] - box[0], box[3] - box[1], fill=False, edgecolor=color, linewidth=2, label=label))
    ax.set_xlim(0, 250); ax.set_ylim(220, 0); ax.set_aspect("equal")
    ax.set_title(f"{name}: IoU = {v:.2f}"); ax.legend(loc="lower right")
fig.savefig(IMG / "ex01_iou.png", dpi=100, bbox_inches="tight")
