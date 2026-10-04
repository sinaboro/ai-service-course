import platform
from pathlib import Path
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = {"Windows": "Malgun Gothic", "Darwin": "AppleGothic"}.get(platform.system(), "NanumGothic")
plt.rcParams["axes.unicode_minus"] = False
IMG = Path(__file__).parent / "images"            # 그림을 저장할 폴더
IMG.mkdir(exist_ok=True)

import os
import random

import cv2
import numpy as np
from ultralytics import YOLO

from scene import make_scene

COLORS = [(0, 0, 230), (0, 140, 255), (160, 48, 112)]      # bottle, can, bag (BGR)


def draw_box(img, x1, y1, x2, y2, label, color):
    """5장 ex04 와 같은 함수: 상자 + 글자 배경 + 글자"""
    cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)
    (tw, th), base = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.45, 1)
    cv2.rectangle(img, (x1, max(0, y1 - th - base - 4)), (x1 + tw + 4, y1), color, -1)
    cv2.putText(img, label, (x1 + 2, max(th, y1 - base - 2)), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (255, 255, 255), 1, cv2.LINE_AA)

HERE = Path(__file__).parent
os.chdir(HERE)                                         # 동영상 파일은 영어 상대 경로로 (5장)
os.makedirs("videos", exist_ok=True)
model = YOLO("models/best.pt")

# ① 연습용 동영상: 장면이 천천히 옆으로 흘러가는 4초 영상
scene, _ = make_scene(random.Random(11), 320)
wide = np.concatenate([scene, cv2.flip(scene, 1)], axis=1)          # 640 × 320 띠
writer = cv2.VideoWriter("videos/beach.mp4", cv2.VideoWriter_fourcc(*"mp4v"), 15, (320, 320))
for t in range(60):
    writer.write(wide[:, t * 5:t * 5 + 320].copy())
writer.release()

# ② 장면마다 탐지해서 새 동영상으로 저장 (stream=True: 한 장면씩 결과를 받아 메모리 절약)
out = cv2.VideoWriter("videos/beach_detect.mp4", cv2.VideoWriter_fourcc(*"mp4v"), 15, (320, 320))
counts, picks = [], []
for i, r in enumerate(model.predict("videos/beach.mp4", stream=True, conf=0.25, verbose=False)):
    frame = r.orig_img.copy()
    for xyxy, conf, cls in zip(r.boxes.xyxy.tolist(), r.boxes.conf.tolist(), r.boxes.cls.tolist()):
        draw_box(frame, *map(int, xyxy), f"{model.names[int(cls)]} {conf:.2f}", COLORS[int(cls)])
    cv2.putText(frame, f"frame {i}  objects {len(r.boxes)}", (5, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (255, 255, 255), 1)
    out.write(frame)
    counts.append(len(r.boxes))
    if i in (0, 30, 59):
        picks.append((i, frame))
out.release()
print("처리한 장면:", len(counts), "| 장면별 물체 수(처음 15개):", counts[:15])
print("평균 물체 수:", round(sum(counts) / len(counts), 2), "| 저장: videos/beach_detect.mp4")

fig, axes = plt.subplots(1, 3, figsize=(11, 3.8))
for ax, (i, f) in zip(axes, picks):
    ax.imshow(cv2.cvtColor(f, cv2.COLOR_BGR2RGB)); ax.set_title(f"장면 {i}"); ax.axis("off")
fig.savefig(IMG / "ex06_video.png", dpi=100, bbox_inches="tight")
