import platform
from pathlib import Path
import matplotlib.pyplot as plt

# 그래프 한글 글꼴: 운영체제에 따라 알맞은 글꼴 고르기 (Windows = 맑은 고딕)
plt.rcParams["font.family"] = {"Windows": "Malgun Gothic", "Darwin": "AppleGothic"}.get(platform.system(), "NanumGothic")
# 마이너스(-) 기호가 네모로 깨지지 않게
plt.rcParams["axes.unicode_minus"] = False
IMG = Path(__file__).parent / "images"            # 그림을 저장할 폴더
IMG.mkdir(exist_ok=True)

# labelImg 가 YOLO 형식으로 저장하는 것과 같은 파일을 만들고, 다시 읽어서 그려 보기
import random

import cv2

from cvutil import imread, imwrite
from scene import CLASSES, make_scene, to_yolo_line

DEMO = Path(__file__).parent / "labelimg_demo"           # labelImg 의 저장 폴더라고 생각하기
DEMO.mkdir(exist_ok=True)
# 장면 하나를 만들어 사진(.jpg) · 클래스 목록(classes.txt) · 레이블(.txt) 저장
img, boxes = make_scene(random.Random(7), 480)
imwrite(DEMO / "beach_007.jpg", img)
(DEMO / "classes.txt").write_text("\n".join(CLASSES) + "\n", encoding="utf-8")       # labelImg 가 함께 만드는 파일
(DEMO / "beach_007.txt").write_text("\n".join(to_yolo_line(c, *b, 480) for c, *b in boxes) + "\n", encoding="utf-8")

# 저장된 파일 내용 확인
print("classes.txt:", (DEMO / "classes.txt").read_text(encoding="utf-8").split())
print("beach_007.txt 내용:")
print((DEMO / "beach_007.txt").read_text(encoding="utf-8"))

# ⭐ 읽기: 한 줄 = 클래스번호 x중심 y중심 너비 높이 (모두 0 ~ 1)
names = (DEMO / "classes.txt").read_text(encoding="utf-8").split()
# 사진을 읽고 크기(H, W) 알아내기
pic = imread(DEMO / "beach_007.jpg")
H, W = pic.shape[:2]
for line in (DEMO / "beach_007.txt").read_text(encoding="utf-8").splitlines():
    c, xc, yc, w, h = line.split()
    xc, yc, w, h = float(xc) * W, float(yc) * H, float(w) * W, float(h) * H      # 비율 → 픽셀
    x1, y1, x2, y2 = round(xc - w / 2), round(yc - h / 2), round(xc + w / 2), round(yc + h / 2)
    print(f"{names[int(c)]:6s} → 픽셀 상자 ({x1}, {y1}, {x2}, {y2})")
    # 픽셀 상자를 사진 위에 그리고 클래스 이름 쓰기
    cv2.rectangle(pic, (x1, y1), (x2, y2), (0, 0, 255), 2)
    cv2.putText(pic, names[int(c)], (x1, y1 - 4), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
# 결과 그림 저장
fig, ax = plt.subplots(figsize=(5, 5))
ax.imshow(cv2.cvtColor(pic, cv2.COLOR_BGR2RGB)); ax.axis("off"); ax.set_title("레이블 파일을 읽어 그린 상자")
fig.savefig(IMG / "ex04_yolo_label.png", dpi=100, bbox_inches="tight")
