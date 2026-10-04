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
import pandas as pd

from cvutil import imread, imwrite

# 7장 ex02 가 만든 학습 결과 폴더
RUN = Path(__file__).parent / "runs" / "floats"
df = pd.read_csv(RUN / "results.csv")
df.columns = df.columns.str.strip()
print("기록된 에폭 수:", len(df))
# 몇 개의 에폭만 골라 표로 보기 (첫 에폭, 5, 10, 20, 마지막)
print(df[["epoch", "train/box_loss", "val/box_loss", "metrics/precision(B)", "metrics/recall(B)", "metrics/mAP50(B)"]].round(3).iloc[[0, 4, 9, 19, -1]].to_string(index=False))
best = df["metrics/mAP50(B)"].idxmax()
print(f"mAP50 이 가장 높은 에폭: {int(df.loc[best, 'epoch'])} ({df.loc[best, 'metrics/mAP50(B)']:.3f})")

# 왼쪽: 상자 손실 / 오른쪽: 검증 mAP 곡선
fig, axes = plt.subplots(1, 2, figsize=(11, 3.6))
axes[0].plot(df["epoch"], df["train/box_loss"], label="학습 box_loss")
axes[0].plot(df["epoch"], df["val/box_loss"], label="검증 box_loss")
axes[0].set_xlabel("에폭"); axes[0].set_title("상자 손실"); axes[0].legend()
axes[1].plot(df["epoch"], df["metrics/mAP50(B)"], label="mAP50")
axes[1].plot(df["epoch"], df["metrics/mAP50-95(B)"], label="mAP50-95")
axes[1].set_xlabel("에폭"); axes[1].set_title("검증 성적"); axes[1].legend()
fig.savefig(IMG / "ex03_curves.png", dpi=100, bbox_inches="tight")

# YOLO 가 결과 폴더에 저장한 그림 몇 장을 교안용으로 복사 (jpg → png)
print("결과 폴더의 그림:", sorted(p.name for p in RUN.glob("*.png"))[:6], "...")
for src, dst in [("confusion_matrix_normalized.png", "ex03_confusion.png"), ("val_batch0_pred.jpg", "ex03_val_pred.png"), ("labels.jpg", "ex03_labels.png")]:
    # 큰 그림은 긴 쪽 700px 로 줄여서 저장 (im 이 None 이면 파일이 없는 것)
    im = imread(RUN / src)
    if im is not None:
        imwrite(IMG / dst, cv2.resize(im, (im.shape[1] * 700 // max(im.shape[:2]), im.shape[0] * 700 // max(im.shape[:2]))))
