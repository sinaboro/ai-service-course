# 도형 이미지 데이터셋 만들기: 원 · 사각형 · 삼각형 (폴더 이름 = 클래스 이름)
import random
from pathlib import Path

import cv2
import numpy as np

from cvutil import imwrite

ROOT = Path(__file__).parent / "data" / "shapes"
CLASSES = ["circle", "square", "triangle"]
rng = random.Random(0)


# 도형 하나 그리기: 밝은 배경 + 어두운 색 도형, 위치 · 크기 · 색은 무작위
def draw(shape):
    img = np.full((64, 64, 3), rng.randint(180, 255), np.uint8)              # 밝은 배경
    color = tuple(rng.randint(0, 150) for _ in range(3))
    cx, cy, r = rng.randint(22, 42), rng.randint(22, 42), rng.randint(10, 18)
    if shape == "circle":
        cv2.circle(img, (cx, cy), r, color, -1)
    elif shape == "square":
        cv2.rectangle(img, (cx - r, cy - r), (cx + r, cy + r), color, -1)
    else:
        # 삼각형: 꼭짓점 3개를 numpy 배열로 주고 채우기
        pts = np.array([[cx, cy - r], [cx - r, cy + r], [cx + r, cy + r]], np.int32)
        cv2.fillPoly(img, [pts], color)
    return img


# train 200장 · val 50장씩, 폴더 이름 = 클래스 이름 (data/shapes/train/circle/...)
count = 0
for split, n in [("train", 200), ("val", 50)]:
    for c in CLASSES:
        folder = ROOT / split / c
        folder.mkdir(parents=True, exist_ok=True)
        for i in range(n):
            imwrite(folder / f"{c}_{i:03d}.png", draw(c))
            count += 1
print("만든 이미지:", count, "장")
# 클래스별로 만든 장수 확인
for split in ["train", "val"]:
    print(split, {c: len(list((ROOT / split / c).glob("*.png"))) for c in CLASSES})
