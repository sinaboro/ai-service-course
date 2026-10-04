import platform
from pathlib import Path
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = {"Windows": "Malgun Gothic", "Darwin": "AppleGothic"}.get(platform.system(), "NanumGothic")
plt.rcParams["axes.unicode_minus"] = False
IMG = Path(__file__).parent / "images"            # 그림을 저장할 폴더
IMG.mkdir(exist_ok=True)

import keras
import numpy as np

keras.utils.set_random_seed(42)

# 1. 데이터: 28×28 손글씨 숫자 (학습 60000장, 테스트 10000장)
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
print("학습:", x_train.shape, y_train.shape, "| 테스트:", x_test.shape)
print("픽셀 범위:", x_train.min(), "~", x_train.max(), "| 첫 정답:", y_train[0])
x_train = x_train.astype("float32") / 255.0     # 0 ~ 1 로 (정규화)
x_test = x_test.astype("float32") / 255.0

# 2. 모델
model = keras.Sequential([
    keras.Input(shape=(28, 28)),
    keras.layers.Flatten(),                       # 28×28 → 784 한 줄로
    keras.layers.Dense(128, activation="relu"),   # 숨은층
    keras.layers.Dense(10, activation="softmax"), # 숫자 0 ~ 9 확률
])
model.summary()

# 3. 컴파일: 손실 · 옵티마이저 · 지표
model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])

# 4. 학습: 학습 데이터의 10% 를 검증용으로
history = model.fit(x_train, y_train, epochs=5, batch_size=128, validation_split=0.1, verbose=2)

# 5. 평가 · 저장
loss, acc = model.evaluate(x_test, y_test, verbose=0)
print(f"테스트 정확도: {acc:.4f}")
model.save("mnist_dense.keras")

# 학습 곡선
h = history.history
fig, axes = plt.subplots(1, 2, figsize=(11, 3.5))
axes[0].plot(h["loss"], "o-", label="학습"); axes[0].plot(h["val_loss"], "s-", label="검증")
axes[0].set_title("손실 (loss)"); axes[0].set_xlabel("에폭"); axes[0].legend()
axes[1].plot(h["accuracy"], "o-", label="학습"); axes[1].plot(h["val_accuracy"], "s-", label="검증")
axes[1].set_title("정확도 (accuracy)"); axes[1].set_xlabel("에폭"); axes[1].legend()
fig.savefig(IMG / "ex04_curves.png", dpi=100, bbox_inches="tight")

# 예측 12장 보기
probs = model.predict(x_test[:12], verbose=0)
fig, axes = plt.subplots(2, 6, figsize=(11, 4))
for i, ax in enumerate(axes.flat):
    p = probs[i].argmax()
    ax.imshow(x_test[i], cmap="gray")
    ax.set_title(f"예측 {p} ({probs[i][p]:.0%})", color="green" if p == y_test[i] else "red")
    ax.axis("off")
fig.savefig(IMG / "ex04_predictions.png", dpi=100, bbox_inches="tight")
