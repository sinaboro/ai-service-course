# 연습용 YOLO 데이터셋 만들기 (6장 ex06 과 같은 코드). 여러분의 데이터셋이 있으면 이 단계는 건너뛰세요
import random
import shutil
from pathlib import Path

from cvutil import imwrite
from scene import CLASSES, make_scene, to_yolo_line

ROOT = Path(__file__).parent / "datasets" / "floats"
SIZE = 320
shutil.rmtree(ROOT, ignore_errors=True)          # 다시 실행해도 깨끗하게
rng = random.Random(2026)
counts = {c: 0 for c in CLASSES}
for split, n in [("train", 240), ("val", 60)]:
    (ROOT / "images" / split).mkdir(parents=True)
    (ROOT / "labels" / split).mkdir(parents=True)
    for i in range(n):
        img, boxes = make_scene(rng, SIZE)
        name = f"{split}_{i:04d}"
        imwrite(ROOT / "images" / split / f"{name}.jpg", img)
        lines = [to_yolo_line(c, x1, y1, x2, y2, SIZE) for c, x1, y1, x2, y2 in boxes]
        (ROOT / "labels" / split / f"{name}.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
        for c, *_ in boxes:
            counts[CLASSES[c]] += 1

yaml = f"""# YOLO 데이터 설정 파일
path: {ROOT.as_posix()}
train: images/train
val: images/val
names:
""" + "".join(f"  {i}: {c}\n" for i, c in enumerate(CLASSES))
(ROOT / "data.yaml").write_text(yaml, encoding="utf-8")
print("사진: train 240장, val 60장")
print("물체 수:", counts)
print((ROOT / "data.yaml").read_text(encoding="utf-8").replace(ROOT.as_posix(), "(이 폴더)/datasets/floats"))
