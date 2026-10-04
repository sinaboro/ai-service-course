import platform
from pathlib import Path
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = {"Windows": "Malgun Gothic", "Darwin": "AppleGothic"}.get(platform.system(), "NanumGothic")
plt.rcParams["axes.unicode_minus"] = False
IMG = Path(__file__).parent / "images"            # 그림을 저장할 폴더
IMG.mkdir(exist_ok=True)

from ultralytics import YOLO

from cvutil import imread

HERE = Path(__file__).parent
VAL = HERE / "datasets" / "floats"
model = YOLO(HERE / "models" / "best.pt")


def iou(a, b):
    ix1, iy1, ix2, iy2 = max(a[0], b[0]), max(a[1], b[1]), min(a[2], b[2]), min(a[3], b[3])
    inter = max(0, ix2 - ix1) * max(0, iy2 - iy1)
    return inter / ((a[2] - a[0]) * (a[3] - a[1]) + (b[2] - b[0]) * (b[3] - b[1]) - inter + 1e-9)


# 검증 사진 60장을 한 번만 예측 (기준을 아주 낮게 0.01) → 기준별로 걸러서 비교
truth, preds = {}, {}
for p in sorted((VAL / "images" / "val").glob("*.jpg")):
    img = imread(p)
    H, W = img.shape[:2]
    gt = []
    for line in (VAL / "labels" / "val" / (p.stem + ".txt")).read_text().splitlines():
        c, xc, yc, w, h = map(float, line.split())
        gt.append((int(c), ((xc - w / 2) * W, (yc - h / 2) * H, (xc + w / 2) * W, (yc + h / 2) * H)))
    r = model.predict(img, conf=0.01, verbose=False)[0]
    truth[p.name] = gt
    preds[p.name] = [(float(s), int(c), b) for s, c, b in zip(r.boxes.conf.tolist(), r.boxes.cls.tolist(), r.boxes.xyxy.tolist())]

n_truth = sum(len(v) for v in truth.values())
rows = []
for thr in [0.05, 0.1, 0.25, 0.5, 0.75, 0.9]:
    tp = fp = 0
    for name, dets in preds.items():
        used = set()
        for s, c, b in sorted(dets, reverse=True):
            if s < thr:
                continue
            match = [i for i, (gc, gb) in enumerate(truth[name]) if gc == c and i not in used and iou(b, gb) >= 0.5]
            if match:
                used.add(match[0]); tp += 1
            else:
                fp += 1
    rows.append((thr, tp + fp, tp, fp, tp / max(tp + fp, 1), tp / n_truth))
print(f"검증 사진 속 실제 물체: {n_truth}개")
print(" 기준  찾은수  맞음  틀림  정밀도  재현율")
for thr, n, tp, fp, p, r in rows:
    print(f" {thr:4.2f}  {n:5d}  {tp:4d}  {fp:4d}   {p:.3f}   {r:.3f}")

fig, ax = plt.subplots(figsize=(6, 3.6))
ax.plot([r[0] for r in rows], [r[4] for r in rows], "o-", label="정밀도")
ax.plot([r[0] for r in rows], [r[5] for r in rows], "s-", label="재현율")
ax.set_xlabel("신뢰도 기준 (conf)"); ax.legend(); ax.set_title("기준을 올리면 정밀도 ↑ 재현율 ↓")
fig.savefig(IMG / "ex07_conf.png", dpi=100, bbox_inches="tight")
