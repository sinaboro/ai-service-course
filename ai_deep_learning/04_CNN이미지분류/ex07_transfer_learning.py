import keras

keras.utils.set_random_seed(2)
ROOT = __import__("pathlib").Path(__file__).parent / "data" / "shapes"
# 4장 ex05 가 만든 도형 데이터셋을 96×96 크기로 불러오기
train_ds = keras.utils.image_dataset_from_directory(ROOT / "train", image_size=(96, 96), batch_size=32, seed=2)
val_ds = keras.utils.image_dataset_from_directory(ROOT / "val", image_size=(96, 96), batch_size=32, shuffle=False)

# ⭐ ImageNet(사진 120만 장)으로 미리 학습된 MobileNetV2 를 가져오기 (분류층은 빼고)
base = keras.applications.MobileNetV2(input_shape=(96, 96, 3), include_top=False, weights="imagenet")
base.trainable = False                     # 이미 배운 특징 추출 능력은 그대로 얼리기
print("사전 학습 모델 층 수:", len(base.layers), "| 가중치 수:", f"{base.count_params():,}")

# 우리 모델 = 정규화 → 사전 학습 몸통(얼린 상태) → 평균 풀링 → 새 분류층
model = keras.Sequential([
    keras.Input(shape=(96, 96, 3)),
    keras.layers.Rescaling(1 / 127.5, offset=-1),   # MobileNetV2 는 -1 ~ 1 입력
    base,
    keras.layers.GlobalAveragePooling2D(),
    keras.layers.Dense(3, activation="softmax"),     # 우리 클래스 3개만 새로 배우기
])
# 새로 학습하는 가중치 수 세기 (얼린 몸통은 빠져요)
trainable = sum(keras.ops.size(w) for w in model.trainable_weights)
print("새로 학습하는 가중치 수:", int(trainable))
model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])
model.fit(train_ds, validation_data=val_ds, epochs=3, verbose=2)
print(f"전이 학습 검증 정확도 (3 에폭): {model.evaluate(val_ds, verbose=0)[1]:.3f}")
