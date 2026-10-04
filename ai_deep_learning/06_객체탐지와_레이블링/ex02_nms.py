import platform
from pathlib import Path
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = {"Windows": "Malgun Gothic", "Darwin": "AppleGothic"}.get(platform.system(), "NanumGothic")
plt.rcParams["axes.unicode_minus"] = False
IMG = Path(__file__).parent / "images"            # 그림을 저장할 폴더
IMG.mkdir(exist_ok=True)

import matplotlib.patches as patches


def iou(a, b):
    ix1, iy1, ix2, iy2 = max(a[0], b[0]), max(a[1], b[1]), min(a[2], b[2]), min(a[3], b[3])
    inter = max(0, ix2 - ix1) * max(0, iy2 - iy1)
    return inter / ((a[2] - a[0]) * (a[3] - a[1]) + (b[2] - b[0]) * (b[3] - b[1]) - inter)


def nms(dets, iou_thr=0.5):
    """dets = [(신뢰도, 상자), ...]. 가장 확실한 상자를 남기고, 그와 많이 겹치는 상자는 지우기"""
    dets = sorted(dets, reverse=True)                    # ① 신뢰도 높은 순서
    keep = []
    while dets:
        best = dets.pop(0)                               # ② 가장 높은 것 하나 남기기
        keep.append(best)
        dets = [d for d in dets if iou(best[1], d[1]) < iou_thr]   # ③ 많이 겹치는 것은 버리기
    return keep


# 모델이 병 2개 주변에 상자를 여러 개 낸 상황
raw = [(0.92, (50, 40, 110, 180)), (0.85, (55, 50, 118, 185)), (0.60, (40, 30, 105, 170)),
       (0.88, (170, 60, 230, 200)), (0.55, (160, 70, 225, 205)), (0.30, (100, 120, 160, 200))]
conf_thr = 0.4
step1 = [d for d in raw if d[0] >= conf_thr]             # 신뢰도 기준으로 먼저 거르기
kept = nms(step1, iou_thr=0.5)
print("모델이 낸 상자:", len(raw), "→ 신뢰도 0.4 이상:", len(step1), "→ NMS 후:", len(kept))
for conf, box in kept:
    print(f"  남은 상자 {box} 신뢰도 {conf}")

fig, axes = plt.subplots(1, 2, figsize=(10, 4))
for ax, (title, dets) in zip(axes, [("NMS 전", raw), ("NMS 후", kept)]):
    for conf, b in dets:
        ax.add_patch(patches.Rectangle(b[:2], b[2] - b[0], b[3] - b[1], fill=False, edgecolor="red", alpha=0.3 + 0.7 * conf, linewidth=2))
        ax.text(b[0], b[1] - 3, f"{conf:.2f}", color="red", fontsize=8)
    ax.set_xlim(0, 260); ax.set_ylim(230, 0); ax.set_aspect("equal"); ax.set_title(title)
fig.savefig(IMG / "ex02_nms.png", dpi=100, bbox_inches="tight")
