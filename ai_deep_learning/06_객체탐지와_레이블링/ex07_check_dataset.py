import platform
from pathlib import Path
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = {"Windows": "Malgun Gothic", "Darwin": "AppleGothic"}.get(platform.system(), "NanumGothic")
plt.rcParams["axes.unicode_minus"] = False
IMG = Path(__file__).parent / "images"            # 그림을 저장할 폴더
IMG.mkdir(exist_ok=True)

import random
from collections import Counter

import cv2

from cvutil import imread

ROOT = Path(__file__).parent / "datasets" / "floats"
NAMES = ["bottle", "can", "bag"]
problems = []
for split in ["train", "val"]:
    imgs = sorted((ROOT / "images" / split).glob("*.jpg"))
    labels = sorted((ROOT / "labels" / split).glob("*.txt"))
    count = Counter()
    for img_path in imgs:
        lab = ROOT / "labels" / split / (img_path.stem + ".txt")        # ⭐ 같은 이름의 .txt
        if not lab.exists():
            problems.append(f"레이블 없음: {img_path.name}")
            continue
        for line in lab.read_text(encoding="utf-8").split("\n"):
            if not line.strip():
                continue
            c, *v = line.split()
            if int(c) >= len(NAMES) or any(not 0 <= float(x) <= 1 for x in v):
                problems.append(f"잘못된 줄: {lab.name}: {line}")
            count[NAMES[int(c)]] += 1
    print(f"{split:5s} 사진 {len(imgs)}장 · 레이블 {len(labels)}개 · 물체 {dict(count)}")
print("문제:", problems if problems else "없음")

# 레이블을 그린 사진 6장 보기
picks = random.Random(0).sample(sorted((ROOT / "images" / "train").glob("*.jpg")), 6)
fig, axes = plt.subplots(1, 6, figsize=(15, 2.8))
for ax, p in zip(axes, picks):
    im = imread(p)
    H, W = im.shape[:2]
    for line in (ROOT / "labels" / "train" / (p.stem + ".txt")).read_text(encoding="utf-8").splitlines():
        c, xc, yc, w, h = map(float, line.split())
        x1, y1 = int((xc - w / 2) * W), int((yc - h / 2) * H)
        x2, y2 = int((xc + w / 2) * W), int((yc + h / 2) * H)
        cv2.rectangle(im, (x1, y1), (x2, y2), (0, 0, 255), 2)
        cv2.putText(im, NAMES[int(c)], (x1, max(10, y1 - 3)), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 255), 1)
    ax.imshow(cv2.cvtColor(im, cv2.COLOR_BGR2RGB)); ax.set_title(p.name, fontsize=9); ax.axis("off")
fig.savefig(IMG / "ex07_samples.png", dpi=100, bbox_inches="tight")
