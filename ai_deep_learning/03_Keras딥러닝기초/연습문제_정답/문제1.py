# 문제 1. ex04_mnist_dense.py의 숨은층을 Dense(256, relu) 와 Dense(128, relu) 두 개로 바꾸고, 3 에폭 학습 후 테스트 정확도와 전체 가중치 수(model.count_params())를 출력하세요.

import keras
keras.utils.set_random_seed(42)
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0
model = keras.Sequential([
    keras.Input(shape=(28, 28)), keras.layers.Flatten(),
    keras.layers.Dense(256, activation="relu"),
    keras.layers.Dense(128, activation="relu"),
    keras.layers.Dense(10, activation="softmax"),
])
model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])
model.fit(x_train, y_train, epochs=3, batch_size=128, verbose=0)
print("가중치 수:", model.count_params())
print("테스트 정확도:", round(model.evaluate(x_test, y_test, verbose=0)[1], 4))
