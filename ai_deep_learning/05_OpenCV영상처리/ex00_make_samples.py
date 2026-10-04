# 실습용 해변 사진 3장 만들기 (실제 프로젝트에서는 직접 찍은 사진을 써요)
import random
from pathlib import Path

from cvutil import imwrite
from scene import CLASSES, make_scene

OUT = Path(__file__).parent / "samples"
OUT.mkdir(exist_ok=True)
rng = random.Random(20)
for i in range(1, 4):
    img, boxes = make_scene(rng, size=480)
    imwrite(OUT / f"beach_{i:02d}.png", img)
    print(f"beach_{i:02d}.png", img.shape, [CLASSES[c] for c, *_ in boxes])
