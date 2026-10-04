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
import numpy as np

model = keras.models.load_model("mnist_cnn.keras")       # ex03 에서 저장
(_, _), (x_test, y_test) = keras.datasets.mnist.load_data()
# 테스트 사진 첫 장을 CNN 입력 모양 (1, 28, 28, 1) 로
x = x_test[:1, ..., None].astype("float32") / 255.0

conv1 = model.layers[0]                                  # 첫 번째 Conv2D
extractor = keras.Model(inputs=model.inputs, outputs=conv1.output)
maps = extractor.predict(x, verbose=0)[0]                # (26, 26, 32)
print("첫 합성곱 층 출력 모양:", maps.shape, "→ 필터 32개가 만든 특징 맵 32장")

w = conv1.get_weights()[0]                               # (3, 3, 1, 32)
print("필터 가중치 모양:", w.shape)

# 위 줄: 필터(파랑 -, 빨강 +) / 아래 줄: 그 필터가 만든 특징 맵
fig, axes = plt.subplots(2, 9, figsize=(13, 3.4))
axes[0, 0].imshow(x[0, ..., 0], cmap="gray"); axes[0, 0].set_title(f"입력 {y_test[0]}")
axes[1, 0].axis("off")
for i in range(8):
    axes[0, i + 1].imshow(w[:, :, 0, i], cmap="bwr"); axes[0, i + 1].set_title(f"필터 {i}")
    axes[1, i + 1].imshow(maps[..., i], cmap="viridis"); axes[1, i + 1].set_title(f"특징 맵 {i}")
for ax in axes.flat:
    ax.set_xticks([]); ax.set_yticks([])
fig.savefig(IMG / "ex04_feature_maps.png", dpi=100, bbox_inches="tight")
