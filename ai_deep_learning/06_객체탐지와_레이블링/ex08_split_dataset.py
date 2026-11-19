# labelImg 로 한 폴더에 모아 둔 (사진 + .txt) 를 YOLO 구조(train 80% / val 20%)로 나누기
import random                                    # 무작위(난수) 값 만들기
import shutil                                    # 파일 · 폴더 복사 · 삭제 도구
from pathlib import Path                         # 파일 · 폴더 경로를 다루는 도구

HERE = Path(__file__).parent                     # 이 .py 파일이 있는 폴더 (어디서 실행해도 같은 곳)
SRC = HERE / "my_labeled"                        # labelImg 작업 폴더 (사진과 .txt 가 함께)
DST = HERE / "datasets" / "my_project"

# --- 연습용: datasets/floats/train 의 사진 30장을 my_labeled 로 복사해 "labelImg 작업 폴더" 흉내 ---
shutil.rmtree(SRC, ignore_errors=True)
SRC.mkdir()
floats = HERE / "datasets" / "floats"
for p in sorted((floats / "images" / "train").glob("*.jpg"))[:30]:
    shutil.copy(p, SRC / p.name)
    shutil.copy(floats / "labels" / "train" / (p.stem + ".txt"), SRC / (p.stem + ".txt"))
(SRC / "classes.txt").write_text("bottle\ncan\nbag\n", encoding="utf-8")
# ---------------------------------------------------------------------------------------------

# 사진 파일(.jpg · .jpeg · .png)만 골라 이름순 정렬
images = sorted(p for p in SRC.iterdir() if p.suffix.lower() in (".jpg", ".jpeg", ".png"))
random.Random(42).shuffle(images)                # 섞기 (순서대로 자르면 비슷한 사진이 몰려요)
n_val = max(1, round(len(images) * 0.2))
splits = {"val": images[:n_val], "train": images[n_val:]}

shutil.rmtree(DST, ignore_errors=True)
for split, files in splits.items():
    (DST / "images" / split).mkdir(parents=True)
    (DST / "labels" / split).mkdir(parents=True)
    for img in files:
        shutil.copy(img, DST / "images" / split / img.name)
        txt = img.with_suffix(".txt")
        if txt.exists():                         # 물체가 없는 사진(배경)은 .txt 가 없을 수 있어요
            shutil.copy(txt, DST / "labels" / split / txt.name)

names = (SRC / "classes.txt").read_text(encoding="utf-8").split()
(DST / "data.yaml").write_text(
    f"path: {DST.as_posix()}\ntrain: images/train\nval: images/val\nnames:\n" + "".join(f"  {i}: {n}\n" for i, n in enumerate(names)),
    encoding="utf-8")
print("전체", len(images), "장 → train", len(splits["train"]), "/ val", len(splits["val"]))
print("클래스:", names)
# DST 아래 모든 폴더를 찾아(rglob) DST 기준 경로 글자로 바꿔 정렬
print("만든 폴더:", sorted(p.relative_to(DST).as_posix() for p in DST.rglob("*") if p.is_dir()))
