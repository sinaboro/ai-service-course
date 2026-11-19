# 실습용 해변 사진 3장 만들기 (실제 프로젝트에서는 직접 찍은 사진을 써요)
import random  # 무작위(난수) 값 만들기
from pathlib import Path  # 파일 · 폴더 경로를 다루는 도구

from cvutil import imwrite
from scene import CLASSES, make_scene

# 사진을 저장할 samples 폴더 만들기
OUT = Path(__file__).parent / "samples"
OUT.mkdir(exist_ok=True)
# 무작위 씨앗(seed) 고정: 실행할 때마다 같은 사진이 만들어져요
rng = random.Random(20)
# 480×480 해변 사진 3장 만들어 저장하고, 들어 있는 물체 이름 출력
for i in range(1, 4):
    img, boxes = make_scene(rng, size=480)
    imwrite(OUT / f"beach_{i:02d}.png", img)
    print(f"beach_{i:02d}.png", img.shape, [CLASSES[c] for c, *_ in boxes])
