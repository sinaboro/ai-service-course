import platform
from pathlib import Path
import matplotlib.pyplot as plt

# 그래프 한글 글꼴: 운영체제에 따라 알맞은 글꼴 고르기 (Windows = 맑은 고딕)
plt.rcParams["font.family"] = {"Windows": "Malgun Gothic", "Darwin": "AppleGothic"}.get(platform.system(), "NanumGothic")
# 마이너스(-) 기호가 네모로 깨지지 않게
plt.rcParams["axes.unicode_minus"] = False
IMG = Path(__file__).parent / "images"            # 그림을 저장할 폴더
IMG.mkdir(exist_ok=True)

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

# 사진 속 병의 상자 높이(픽셀)로 카메라와의 거리(m) 예측하기 (만든 데이터)
# 연습용 데이터 60개: 높이 20 ~ 200px, 거리 = 300 / 높이 + 약간의 잡음
rng = np.random.default_rng(0)
height_px = rng.uniform(20, 200, 60)
distance = 300 / height_px + rng.normal(0, 0.15, 60)      # 멀수록 작게 보임

X = (1 / height_px).reshape(-1, 1)                         # 특성: 1 / 높이
# 직선 회귀 학습 → 학습 데이터 예측
model = LinearRegression().fit(X, distance)
pred = model.predict(X)
print("평균 절대 오차 (m):", round(mean_absolute_error(distance, pred), 3))
print("상자 높이 50px → 예측 거리:", round(model.predict([[1 / 50]])[0], 2), "m")

# 선을 그릴 때 x 가 작은 순서로 정렬해야 선이 꼬이지 않아요
order = np.argsort(height_px)
fig, ax = plt.subplots(figsize=(7, 4))
ax.scatter(height_px, distance, s=15, label="데이터")
ax.plot(height_px[order], pred[order], color="crimson", label="예측")
ax.set_xlabel("상자 높이 (px)")
ax.set_ylabel("거리 (m)")
ax.legend()
fig.savefig(IMG / "ex05_regression.png", dpi=100, bbox_inches="tight")
