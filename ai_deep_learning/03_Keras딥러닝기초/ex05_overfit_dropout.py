import platform
from pathlib import Path
import matplotlib.pyplot as plt

# 그래프 한글 글꼴: 운영체제에 따라 알맞은 글꼴 고르기 (Windows = 맑은 고딕)
plt.rcParams["font.family"] = {"Windows": "Malgun Gothic", "Darwin": "AppleGothic"}.get(platform.system(), "NanumGothic")
# 마이너스(-) 기호가 네모로 깨지지 않게
plt.rcParams["axes.unicode_minus"] = False
IMG = Path(__file__).parent / "images"            # 그림을 저장할 폴더
IMG.mkdir(exist_ok=True)

import keras

keras.utils.set_random_seed(0)
(x_train, y_train), _ = keras.datasets.mnist.load_data()
x_small = x_train[:2000].astype("float32") / 255.0      # 일부러 2000장만 → 과대적합이 잘 보여요
y_small = y_train[:2000]
# 검증 데이터: 학습에 쓰지 않은 5000장
x_val = x_train[50000:55000].astype("float32") / 255.0
y_val = y_train[50000:55000]


# 같은 모양의 모델을 드롭아웃 있게 / 없게 만드는 함수
def build(dropout):
    layers = [keras.Input(shape=(28, 28)), keras.layers.Flatten(), keras.layers.Dense(512, activation="relu")]
    if dropout:
        layers.append(keras.layers.Dropout(0.5))          # 학습 때 뉴런 절반을 무작위로 쉬게 함
    layers.append(keras.layers.Dense(10, activation="softmax"))
    m = keras.Sequential(layers)
    m.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])
    return m


# ① 기본 모델: 40 에폭 끝까지 학습
plain = build(dropout=False).fit(x_small, y_small, epochs=40, batch_size=64, validation_data=(x_val, y_val), verbose=0)

# ② 드롭아웃 + 조기 종료 모델
stop = keras.callbacks.EarlyStopping(monitor="val_loss", patience=3, restore_best_weights=True)
better = build(dropout=True).fit(x_small, y_small, epochs=40, batch_size=64, validation_data=(x_val, y_val), verbose=0, callbacks=[stop])

# 두 모델 비교: 검증 손실이 가장 낮았던 에폭과 마지막 에폭의 값
for name, h in [("기본", plain.history), ("드롭아웃 + 조기 종료", better.history)]:
    best = min(range(len(h["val_loss"])), key=lambda i: h["val_loss"][i])
    print(f"{name:12s} 에폭 {len(h['loss']):2d}번 | 마지막 학습 정확도 {h['accuracy'][-1]:.3f} "
          f"| 가장 낮은 검증 손실 {h['val_loss'][best]:.3f} (에폭 {best + 1}) | 마지막 검증 손실 {h['val_loss'][-1]:.3f}")

# 그래프: 점선 = 학습 손실, 실선 = 검증 손실
fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(plain.history["loss"], label="기본 - 학습 손실", color="tab:blue", linestyle="--")
ax.plot(plain.history["val_loss"], label="기본 - 검증 손실", color="tab:blue")
ax.plot(better.history["val_loss"], label="드롭아웃+조기종료 - 검증 손실", color="tab:red")
ax.set_xlabel("에폭"); ax.set_ylabel("손실"); ax.legend()
ax.set_title("학습 손실은 계속 줄지만 검증 손실은 다시 올라가요 (과대적합)")
fig.savefig(IMG / "ex05_overfit.png", dpi=100, bbox_inches="tight")
