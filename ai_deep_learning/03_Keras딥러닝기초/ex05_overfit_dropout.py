import platform
from pathlib import Path
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = {"Windows": "Malgun Gothic", "Darwin": "AppleGothic"}.get(platform.system(), "NanumGothic")
plt.rcParams["axes.unicode_minus"] = False
IMG = Path(__file__).parent / "images"            # 그림을 저장할 폴더
IMG.mkdir(exist_ok=True)

import keras

keras.utils.set_random_seed(0)
(x_train, y_train), _ = keras.datasets.mnist.load_data()
x_small = x_train[:2000].astype("float32") / 255.0      # 일부러 2000장만 → 과대적합이 잘 보여요
y_small = y_train[:2000]
x_val = x_train[50000:55000].astype("float32") / 255.0
y_val = y_train[50000:55000]


def build(dropout):
    layers = [keras.Input(shape=(28, 28)), keras.layers.Flatten(), keras.layers.Dense(512, activation="relu")]
    if dropout:
        layers.append(keras.layers.Dropout(0.5))          # 학습 때 뉴런 절반을 무작위로 쉬게 함
    layers.append(keras.layers.Dense(10, activation="softmax"))
    m = keras.Sequential(layers)
    m.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])
    return m


plain = build(dropout=False).fit(x_small, y_small, epochs=40, batch_size=64, validation_data=(x_val, y_val), verbose=0)

stop = keras.callbacks.EarlyStopping(monitor="val_loss", patience=3, restore_best_weights=True)
better = build(dropout=True).fit(x_small, y_small, epochs=40, batch_size=64, validation_data=(x_val, y_val), verbose=0, callbacks=[stop])

for name, h in [("기본", plain.history), ("드롭아웃 + 조기 종료", better.history)]:
    best = min(range(len(h["val_loss"])), key=lambda i: h["val_loss"][i])
    print(f"{name:12s} 에폭 {len(h['loss']):2d}번 | 마지막 학습 정확도 {h['accuracy'][-1]:.3f} "
          f"| 가장 낮은 검증 손실 {h['val_loss'][best]:.3f} (에폭 {best + 1}) | 마지막 검증 손실 {h['val_loss'][-1]:.3f}")

fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(plain.history["loss"], label="기본 - 학습 손실", color="tab:blue", linestyle="--")
ax.plot(plain.history["val_loss"], label="기본 - 검증 손실", color="tab:blue")
ax.plot(better.history["val_loss"], label="드롭아웃+조기종료 - 검증 손실", color="tab:red")
ax.set_xlabel("에폭"); ax.set_ylabel("손실"); ax.legend()
ax.set_title("학습 손실은 계속 줄지만 검증 손실은 다시 올라가요 (과대적합)")
fig.savefig(IMG / "ex05_overfit.png", dpi=100, bbox_inches="tight")
