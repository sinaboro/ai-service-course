# ex07_check_dataset.py : 데이터셋 점검: 사진과 레이블 짝 · 클래스별 개수 · 상자 크기 확인
import platform                                   # 운영체제 이름 알아내기 (한글 글꼴 고를 때 사용)
from pathlib import Path                          # 파일 · 폴더 경로를 다루는 도구
import matplotlib.pyplot as plt                   # 그래프 도구 (관례적으로 plt 라는 별명)

# 그래프 한글 글꼴: 운영체제에 따라 알맞은 글꼴 고르기 (Windows = 맑은 고딕)
plt.rcParams["font.family"] = {"Windows": "Malgun Gothic", "Darwin": "AppleGothic"}.get(platform.system(), "NanumGothic")
# 마이너스(-) 기호가 네모로 깨지지 않게
plt.rcParams["axes.unicode_minus"] = False        # 마이너스(-) 기호가 네모로 깨지지 않게
IMG = Path(__file__).parent / "images"            # 그림을 저장할 폴더
IMG.mkdir(exist_ok=True)                          # images 폴더 만들기 (이미 있으면 그냥 넘어가요)

import random                                     # 무작위(난수) 값 만들기
from collections import Counter

import cv2                                        # OpenCV: 영상 처리 도구

from cvutil import imread

ROOT = Path(__file__).parent / "datasets" / "floats"
NAMES = ["bottle", "can", "bag"]
# 찾은 문제를 모을 목록
problems = []
# train, val 각각 사진 · 레이블 개수와 클래스별 물체 수 세기
for split in ["train", "val"]:
    imgs = sorted((ROOT / "images" / split).glob("*.jpg"))
    labels = sorted((ROOT / "labels" / split).glob("*.txt"))
    count = Counter()
    for img_path in imgs:
        lab = ROOT / "labels" / split / (img_path.stem + ".txt")        # ⭐ 같은 이름의 .txt
        if not lab.exists():
            problems.append(f"레이블 없음: {img_path.name}")
            continue
        # 레이블 파일의 줄마다: 빈 줄은 건너뛰고, 클래스 번호와 좌표 범위 검사
        for line in lab.read_text(encoding="utf-8").split("\n"):
            if not line.strip():
                continue
            c, *v = line.split()
            # 문제 조건: 클래스 번호가 클래스 수보다 크거나, 좌표 4개 중 하나라도 0~1 범위를 벗어나면
            if int(c) >= len(NAMES) or any(not 0 <= float(x) <= 1 for x in v):
                problems.append(f"잘못된 줄: {lab.name}: {line}")
            count[NAMES[int(c)]] += 1
    print(f"{split:5s} 사진 {len(imgs)}장 · 레이블 {len(labels)}개 · 물체 {dict(count)}")
print("문제:", problems if problems else "없음")      # 문제 목록이 비어 있으면 "없음"

# 레이블을 그린 사진 6장 보기
picks = random.Random(0).sample(sorted((ROOT / "images" / "train").glob("*.jpg")), 6)
fig, axes = plt.subplots(1, 6, figsize=(15, 2.8))
for ax, p in zip(axes, picks):                    # zip: 칸과 사진 경로를 하나씩 짝지어 꺼내기
    im = imread(p)
    H, W = im.shape[:2]
    # 레이블을 읽어 비율 → 픽셀로 바꾸고 상자 그리기
    for line in (ROOT / "labels" / "train" / (p.stem + ".txt")).read_text(encoding="utf-8").splitlines():
        c, xc, yc, w, h = map(float, line.split())
        x1, y1 = int((xc - w / 2) * W), int((yc - h / 2) * H)
        x2, y2 = int((xc + w / 2) * W), int((yc + h / 2) * H)
        cv2.rectangle(im, (x1, y1), (x2, y2), (0, 0, 255), 2)
        cv2.putText(im, NAMES[int(c)], (x1, max(10, y1 - 3)), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 255), 1)
    ax.imshow(cv2.cvtColor(im, cv2.COLOR_BGR2RGB)); ax.set_title(p.name, fontsize=9); ax.axis("off")
fig.savefig(IMG / "ex07_samples.png", dpi=100, bbox_inches="tight")
