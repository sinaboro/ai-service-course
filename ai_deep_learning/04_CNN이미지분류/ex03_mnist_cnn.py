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

keras.utils.set_random_seed(42)
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
x_train = x_train[..., None].astype("float32") / 255.0     # (60000, 28, 28, 1) — 채널 1개 추가
x_test = x_test[..., None].astype("float32") / 255.0
print("입력 모양:", x_train.shape)

# 모델: [합성곱 → 풀링] 두 번 → 펴기 → 드롭아웃 → 출력층
model = keras.Sequential([
    keras.Input(shape=(28, 28, 1)),
    keras.layers.Conv2D(32, 3, activation="relu"),      # 3×3 필터 32개
    keras.layers.MaxPooling2D(2),                       # 크기 절반
    keras.layers.Conv2D(64, 3, activation="relu"),      # 3×3 필터 64개
    keras.layers.MaxPooling2D(2),
    keras.layers.Flatten(),
    keras.layers.Dropout(0.3),
    keras.layers.Dense(10, activation="softmax"),
])
# 층마다 출력 모양: 28 → 26 → 13 → 11 → 5 (가장자리 · 풀링으로 줄어들어요)
model.summary()
model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])
# 학습 3 에폭 (CNN 은 Dense 보다 계산이 많아서 조금 느려요)
model.fit(x_train, y_train, epochs=3, batch_size=128, validation_split=0.1, verbose=2)
print(f"CNN 테스트 정확도: {model.evaluate(x_test, y_test, verbose=0)[1]:.4f}  (3장 Dense 모델은 약 0.97)")
model.save("mnist_cnn.keras")
