import platform
from pathlib import Path
import matplotlib.pyplot as plt

# 그래프 한글 글꼴: 운영체제에 따라 알맞은 글꼴 고르기 (Windows = 맑은 고딕)
plt.rcParams["font.family"] = {"Windows": "Malgun Gothic", "Darwin": "AppleGothic"}.get(platform.system(), "NanumGothic")
# 마이너스(-) 기호가 네모로 깨지지 않게
plt.rcParams["axes.unicode_minus"] = False
IMG = Path(__file__).parent / "images"            # 그림을 저장할 폴더
IMG.mkdir(exist_ok=True)

import os

import cv2
import numpy as np

os.chdir(Path(__file__).parent)       # ⭐ 이 파일이 있는 폴더로 이동 → 아래는 영어 상대 경로만 사용

# ① 동영상 만들기: 병이 왼쪽에서 오른쪽으로 떠내려가는 3초 영상 (30fps)
writer = cv2.VideoWriter("videos/float.mp4", cv2.VideoWriter_fourcc(*"mp4v"), 30, (320, 240))
# 장면 90개(30fps × 3초)를 하나씩 그려 동영상에 쓰기
for t in range(90):
    frame = np.zeros((240, 320, 3), np.uint8)
    frame[:] = (200, 150, 80)                                 # 바다
    # 병의 x 위치가 장면마다 3픽셀씩 오른쪽으로
    x = 10 + t * 3
    cv2.rectangle(frame, (x, 120), (x + 18, 170), (90, 170, 90), -1)
    writer.write(frame)
# 저장을 끝내고 파일 닫기 (안 하면 동영상이 깨져요)
writer.release()

# ② 한 장면(frame)씩 읽으며 처리하기
cap = cv2.VideoCapture("videos/float.mp4")
print("열렸나요?", cap.isOpened(), "| fps:", cap.get(cv2.CAP_PROP_FPS), "| 장면 수:", int(cap.get(cv2.CAP_PROP_FRAME_COUNT)))
# 처리한 장면을 저장할 새 동영상
out = cv2.VideoWriter("videos/float_boxed.mp4", cv2.VideoWriter_fourcc(*"mp4v"), 30, (320, 240))
n, picks = 0, []
while True:
    ok, frame = cap.read()                          # ok 가 False 면 끝
    if not ok:
        break
    # 장면마다: 초록색 영역을 찾아 상자 · 장면 번호 그리기
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, (40, 60, 60), (85, 255, 255))
    x, y, w, h = cv2.boundingRect(mask)             # 초록 영역 전체를 감싸는 상자
    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
    cv2.putText(frame, f"frame {n}", (5, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)
    out.write(frame)
    # 처음 · 가운데 · 마지막 장면은 그림으로 보여 주려고 따로 보관
    if n in (0, 45, 89):
        picks.append((f"장면 {n}", frame.copy()))
    n += 1
cap.release()
out.release()
print("처리한 장면:", n, "| 저장: videos/float_boxed.mp4")

# 고른 장면 3개를 나란히 저장
fig, axes = plt.subplots(1, 3, figsize=(11, 3))
for ax, (title, im) in zip(axes, picks):
    ax.imshow(cv2.cvtColor(im, cv2.COLOR_BGR2RGB)); ax.set_title(title); ax.axis("off")
fig.savefig(IMG / "ex07_video.png", dpi=100, bbox_inches="tight")
