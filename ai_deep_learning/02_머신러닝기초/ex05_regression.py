import platform
from pathlib import Path
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = {"Windows": "Malgun Gothic", "Darwin": "AppleGothic"}.get(platform.system(), "NanumGothic")
plt.rcParams["axes.unicode_minus"] = False
IMG = Path(__file__).parent / "images"            # 그림을 저장할 폴더
IMG.mkdir(exist_ok=True)

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

# 사진 속 병의 상자 높이(픽셀)로 카메라와의 거리(m) 예측하기 (만든 데이터)
rng = np.random.default_rng(0)
height_px = rng.uniform(20, 200, 60)
distance = 300 / height_px + rng.normal(0, 0.15, 60)      # 멀수록 작게 보임

X = (1 / height_px).reshape(-1, 1)                         # 특성: 1 / 높이
model = LinearRegression().fit(X, distance)
pred = model.predict(X)
print("평균 절대 오차 (m):", round(mean_absolute_error(distance, pred), 3))
print("상자 높이 50px → 예측 거리:", round(model.predict([[1 / 50]])[0], 2), "m")

order = np.argsort(height_px)
fig, ax = plt.subplots(figsize=(7, 4))
ax.scatter(height_px, distance, s=15, label="데이터")
ax.plot(height_px[order], pred[order], color="crimson", label="예측")
ax.set_xlabel("상자 높이 (px)")
ax.set_ylabel("거리 (m)")
ax.legend()
fig.savefig(IMG / "ex05_regression.png", dpi=100, bbox_inches="tight")
