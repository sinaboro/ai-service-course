# 7장에서 학습한 모델과 샘플 사진을 이 폴더로 가져오기
import random
import shutil
import sys
from pathlib import Path

import cv2

from cvutil import imwrite
from scene import make_scene

HERE = Path(__file__).parent
# 7장 모델 위치(src)와 이 장으로 복사할 위치(dst)
src = HERE.parent / "07_YOLO학습과추론" / "models" / "best.pt"
dst = HERE / "models" / "best.pt"
dst.parent.mkdir(exist_ok=True)
# 7장 모델이 없으면 안내 문구를 보여 주고 끝내기
if not src.exists():
    sys.exit("7장 ex02_train.py 를 먼저 실행해서 best.pt 를 만들어 주세요: " + str(src.relative_to(HERE.parent)))
shutil.copy(src, dst)
print("모델 복사:", dst.relative_to(HERE).as_posix(), f"({dst.stat().st_size / 1e6:.1f} MB)")

# 웹 페이지의 [샘플 사진으로 해 보기] 에 쓸 사진 (학습에 쓰지 않은 새 장면)
img, boxes = make_scene(random.Random(116), 320)
img = cv2.resize(img, (640, 640))
imwrite(HERE / "static" / "images" / "sample.png", img)
print("샘플 사진: static/images/sample.png", img.shape, "| 실제 물체", len(boxes), "개")
