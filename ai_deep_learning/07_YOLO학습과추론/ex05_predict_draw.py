import platform
from pathlib import Path
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = {"Windows": "Malgun Gothic", "Darwin": "AppleGothic"}.get(platform.system(), "NanumGothic")
plt.rcParams["axes.unicode_minus"] = False
IMG = Path(__file__).parent / "images"            # 그림을 저장할 폴더
IMG.mkdir(exist_ok=True)

import cv2
from ultralytics import YOLO

from cvutil import imread

COLORS = [(0, 0, 230), (0, 140, 255), (160, 48, 112)]      # bottle, can, bag (BGR)


def draw_box(img, x1, y1, x2, y2, label, color):
    """5장 ex04 와 같은 함수: 상자 + 글자 배경 + 글자"""
    cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)
    (tw, th), base = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.45, 1)
    cv2.rectangle(img, (x1, max(0, y1 - th - base - 4)), (x1 + tw + 4, y1), color, -1)
    cv2.putText(img, label, (x1 + 2, max(th, y1 - base - 2)), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (255, 255, 255), 1, cv2.LINE_AA)

HERE = Path(__file__).parent
model = YOLO(HERE / "models" / "best.pt")
paths = sorted((HERE / "datasets" / "floats" / "images" / "val").glob("*.jpg"))[:6]

fig, axes = plt.subplots(1, 6, figsize=(16, 3.2))
for ax, p in zip(axes, paths):
    img = imread(p)                                       # numpy 배열(BGR)을 그대로 넣어도 돼요
    r = model.predict(img, conf=0.25, verbose=False)[0]
    n_truth = len((HERE / "datasets" / "floats" / "labels" / "val" / (p.stem + ".txt")).read_text().split("\n")) - 1
    for xyxy, conf, cls in zip(r.boxes.xyxy.tolist(), r.boxes.conf.tolist(), r.boxes.cls.tolist()):
        x1, y1, x2, y2 = map(int, xyxy)
        draw_box(img, x1, y1, x2, y2, f"{model.names[int(cls)]} {conf:.2f}", COLORS[int(cls)])
    print(f"{p.name}: 정답 {n_truth}개 / 찾음 {len(r.boxes)}개 →", [model.names[int(c)] for c in r.boxes.cls.tolist()])
    ax.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)); ax.set_title(f"{p.name}\n정답 {n_truth} · 찾음 {len(r.boxes)}", fontsize=9); ax.axis("off")
fig.savefig(IMG / "ex05_predictions.png", dpi=100, bbox_inches="tight")

# 결과를 표(JSON 처럼)로 바꾸기 — 8장 서버가 돌려줄 모양
r = model.predict(imread(paths[0]), conf=0.25, verbose=False)[0]
rows = [{"class": model.names[int(b.cls)], "conf": round(float(b.conf), 2), "box": [round(v) for v in b.xyxy[0].tolist()]} for b in r.boxes]
print("JSON 모양:", rows)
