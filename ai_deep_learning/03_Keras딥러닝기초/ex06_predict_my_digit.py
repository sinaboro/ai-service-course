import platform
from pathlib import Path
import matplotlib.pyplot as plt

# 그래프 한글 글꼴: 운영체제에 따라 알맞은 글꼴 고르기 (Windows = 맑은 고딕)
plt.rcParams["font.family"] = {"Windows": "Malgun Gothic", "Darwin": "AppleGothic"}.get(platform.system(), "NanumGothic")
# 마이너스(-) 기호가 네모로 깨지지 않게
plt.rcParams["axes.unicode_minus"] = False
IMG = Path(__file__).parent / "images"            # 그림을 저장할 폴더
IMG.mkdir(exist_ok=True)

import cv2
import keras
import numpy as np

from cvutil import imread, imwrite     # 한글 경로용 (5장에서 자세히)

model = keras.models.load_model("mnist_dense.keras")   # ex04 에서 저장한 모델

# "내 손글씨" 만들기: 흰 종이에 검은 펜으로 3 쓰기 (실제로는 사진을 cv2.imread 로 읽어요)
# 흰 종이(255) 200×200 에 검은(0) 굵은 숫자 3 을 쓰고 저장
paper = np.full((200, 200), 255, np.uint8)
cv2.putText(paper, "3", (45, 170), cv2.FONT_HERSHEY_SIMPLEX, 6, 0, 18)
imwrite(IMG / "my_digit.png", paper)

# MNIST 와 같은 모양으로 맞추기: 28×28, 검은 배경에 흰 글씨, 0 ~ 1
# 저장한 그림을 흑백으로 다시 읽기 → MNIST 와 같은 28×28 로 줄이기
img = imread(IMG / "my_digit.png", cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img, (28, 28), interpolation=cv2.INTER_AREA)
img = 255 - img                                  # 색 뒤집기
x = img.astype("float32")[None] / 255.0          # (1, 28, 28) — 맨 앞은 "사진 장수"
print("모델 입력 모양:", x.shape)

# 확률이 높은 순서로 3개 출력 (argsort 는 작은 순서라서 [::-1] 로 뒤집기)
probs = model.predict(x, verbose=0)[0]
top3 = probs.argsort()[::-1][:3]
for k in top3:
    print(f"숫자 {k}: {probs[k]:.1%}")

fig, axes = plt.subplots(1, 2, figsize=(7, 3))
axes[0].imshow(paper, cmap="gray"); axes[0].set_title("내 손글씨"); axes[0].axis("off")
axes[1].bar(range(10), probs); axes[1].set_xticks(range(10)); axes[1].set_title("숫자별 확률")
fig.savefig(IMG / "ex06_my_digit.png", dpi=100, bbox_inches="tight")
