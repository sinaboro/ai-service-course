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
import tensorflow as tf

keras.utils.set_random_seed(1)
ROOT = Path(__file__).parent / "data" / "shapes"

# ⭐ 폴더 구조에서 바로 데이터셋 만들기 (폴더 이름이 클래스)
train_ds = keras.utils.image_dataset_from_directory(ROOT / "train", image_size=(64, 64), batch_size=32, seed=1)
val_ds = keras.utils.image_dataset_from_directory(ROOT / "val", image_size=(64, 64), batch_size=32, shuffle=False)
print("클래스:", train_ds.class_names)

augment = keras.Sequential([                        # 데이터 증강: 학습할 때마다 조금씩 다른 사진
    keras.layers.RandomFlip("horizontal"),         # 좌우 뒤집기
    keras.layers.RandomRotation(0.05),             # 조금 회전 (±18도)
    keras.layers.RandomZoom(0.1),                  # 조금 확대 · 축소
])

# 모델: 증강 → 0 ~ 1 정규화 → [합성곱 → 풀링] × 3 → 펴기 → Dense
model = keras.Sequential([
    keras.Input(shape=(64, 64, 3)),
    augment,
    keras.layers.Rescaling(1 / 255),
    keras.layers.Conv2D(32, 3, activation="relu", padding="same"), keras.layers.MaxPooling2D(),
    keras.layers.Conv2D(64, 3, activation="relu", padding="same"), keras.layers.MaxPooling2D(),
    keras.layers.Conv2D(64, 3, activation="relu", padding="same"), keras.layers.MaxPooling2D(),
    keras.layers.Flatten(),
    keras.layers.Dense(64, activation="relu"),
    keras.layers.Dense(3, activation="softmax"),
])
model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])
# 학습: 검증 데이터로 매 에폭 실력을 확인하며 15 에폭
history = model.fit(train_ds, validation_data=val_ds, epochs=15, verbose=2)
print(f"검증 정확도: {model.evaluate(val_ds, verbose=0)[1]:.3f}")

# 증강된 모습 보기: 같은 사진 한 장을 8번 변형
# 학습 데이터에서 사진 묶음 하나 꺼내기
images, _ = next(iter(train_ds))
fig, axes = plt.subplots(1, 8, figsize=(13, 2))
for ax in axes:
    ax.imshow(tf.cast(augment(images[:1], training=True)[0], "uint8")); ax.axis("off")
fig.savefig(IMG / "ex06_augment.png", dpi=100, bbox_inches="tight")

# 학습 · 검증 정확도 곡선
h = history.history
fig, ax = plt.subplots(figsize=(7, 3.5))
ax.plot(h["accuracy"], label="학습"); ax.plot(h["val_accuracy"], label="검증")
ax.set_xlabel("에폭"); ax.set_ylabel("정확도"); ax.legend()
fig.savefig(IMG / "ex06_curve.png", dpi=100, bbox_inches="tight")
