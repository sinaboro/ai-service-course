# 문제 1. 학습한 models/best.pt 로 검증 사진 한 장을 conf=0.5 로 예측하고, 찾은 물체의 이름과 신뢰도를 신뢰도 높은 순서로 출력하세요.

from pathlib import Path
from ultralytics import YOLO
from cvutil import imread
model = YOLO("models/best.pt")
p = sorted(Path("datasets/floats/images/val").glob("*.jpg"))[3]
r = model.predict(imread(p), conf=0.5, verbose=False)[0]
pairs = sorted(zip(r.boxes.conf.tolist(), r.boxes.cls.tolist()), reverse=True)
print(p.name, "→", [(model.names[int(c)], round(s, 2)) for s, c in pairs])
