from pathlib import Path

from ultralytics import YOLO
from ultralytics.utils import ASSETS

from cvutil import imwrite

model = YOLO("yolo11n.pt")                       # COCO(80 클래스)로 미리 학습된 가장 작은 모델
print("클래스 수:", len(model.names), "| 앞의 10개:", [model.names[i] for i in range(10)])

results = model.predict(ASSETS / "bus.jpg", conf=0.25, verbose=False)
r = results[0]                                   # 사진 한 장 = 결과 한 개
print("찾은 물체:", len(r.boxes), "개 | 사진 크기:", r.orig_shape)
for box in r.boxes:
    name = model.names[int(box.cls)]
    x1, y1, x2, y2 = box.xyxy[0].tolist()
    print(f"  {name:7s} {float(box.conf):.2f}  ({x1:.0f}, {y1:.0f}, {x2:.0f}, {y2:.0f})")
print("처리 시간(ms):", {k: round(v, 1) for k, v in r.speed.items()})

imwrite(Path(__file__).parent / "images" / "ex01_bus.png", r.plot())     # plot(): 상자를 그린 BGR 이미지
