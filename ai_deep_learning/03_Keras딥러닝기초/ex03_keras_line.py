import platform
from pathlib import Path
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = {"Windows": "Malgun Gothic", "Darwin": "AppleGothic"}.get(platform.system(), "NanumGothic")
plt.rcParams["axes.unicode_minus"] = False
IMG = Path(__file__).parent / "images"            # 그림을 저장할 폴더
IMG.mkdir(exist_ok=True)

import keras
import numpy as np

keras.utils.set_random_seed(42)          # 실행할 때마다 같은 결과가 나오게

x = np.linspace(-1, 1, 50)
y = 2 * x + 1 + np.random.default_rng(0).normal(0, 0.1, 50)   # 정답 규칙: y = 2x + 1

model = keras.Sequential([
    keras.Input(shape=(1,)),             # 입력 1개
    keras.layers.Dense(1),               # 뉴런 1개 (활성화 없음 = 직선)
])
model.compile(optimizer=keras.optimizers.SGD(learning_rate=0.1), loss="mse")
history = model.fit(x, y, epochs=60, verbose=0)

w, b = model.layers[0].get_weights()
print("배운 가중치 w =", round(float(w[0, 0]), 3), "/ 편향 b =", round(float(b[0]), 3))
print("첫 에폭 손실:", round(history.history["loss"][0], 4), "→ 마지막:", round(history.history["loss"][-1], 4))
print("x = 0.5 예측:", round(float(model.predict(np.array([[0.5]]), verbose=0)[0, 0]), 3))

fig, ax = plt.subplots(figsize=(6, 3.5))
ax.plot(history.history["loss"])
ax.set_xlabel("에폭")
ax.set_ylabel("손실 (MSE)")
ax.set_title("학습할수록 손실이 줄어요")
fig.savefig(IMG / "ex03_loss.png", dpi=100, bbox_inches="tight")
