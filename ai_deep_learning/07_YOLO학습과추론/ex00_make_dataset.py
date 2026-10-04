# 연습용 YOLO 데이터셋 만들기 (6장 ex06 과 같은 코드). 여러분의 데이터셋이 있으면 이 단계는 건너뛰세요
import random
import shutil
from pathlib import Path

from cvutil import imwrite
from scene import CLASSES, make_scene, to_yolo_line

# 데이터셋을 만들 폴더와 사진 크기
ROOT = Path(__file__).parent / "datasets" / "floats"
SIZE = 320
shutil.rmtree(ROOT, ignore_errors=True)          # 다시 실행해도 깨끗하게
# 무작위 씨앗 고정 + 클래스별 물체 수를 셀 사전
rng = random.Random(2026)
counts = {c: 0 for c in CLASSES}
for split, n in [("train", 240), ("val", 60)]:
    # images/train, labels/train 처럼 짝이 되는 폴더 만들기
    (ROOT / "images" / split).mkdir(parents=True)
    (ROOT / "labels" / split).mkdir(parents=True)
    for i in range(n):
        # 사진 한 장 + 정답 상자 목록 만들기
        img, boxes = make_scene(rng, SIZE)
        name = f"{split}_{i:04d}"
        imwrite(ROOT / "images" / split / f"{name}.jpg", img)
        # 상자마다 YOLO 형식 한 줄로 바꾸기
        lines = [to_yolo_line(c, x1, y1, x2, y2, SIZE) for c, x1, y1, x2, y2 in boxes]
        (ROOT / "labels" / split / f"{name}.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
        for c, *_ in boxes:
            counts[CLASSES[c]] += 1

# data.yaml 내용: 데이터 위치(path), 사진 폴더(train · val), 클래스 이름(names)
yaml = f"""# YOLO 데이터 설정 파일
path: {ROOT.as_posix()}
train: images/train
val: images/val
names:
""" + "".join(f"  {i}: {c}\n" for i, c in enumerate(CLASSES))
(ROOT / "data.yaml").write_text(yaml, encoding="utf-8")
# 결과 확인 (긴 절대 경로는 보기 쉽게 바꿔서 출력)
print("사진: train 240장, val 60장")
print("물체 수:", counts)
print((ROOT / "data.yaml").read_text(encoding="utf-8").replace(ROOT.as_posix(), "(이 폴더)/datasets/floats"))
