# ex04_feature_maps.py : 학습한 CNN 의 첫 층이 사진에서 뽑아낸 특징 맵 그려 보기
import platform                                          # 운영체제 이름 알아내기 (한글 글꼴 고를 때 사용)
from pathlib import Path                                 # 파일 · 폴더 경로를 다루는 도구
import matplotlib.pyplot as plt                          # 그래프 도구 (관례적으로 plt 라는 별명)

# 그래프 한글 글꼴: 운영체제에 따라 알맞은 글꼴 고르기 (Windows = 맑은 고딕)
plt.rcParams["font.family"] = {"Windows": "Malgun Gothic", "Darwin": "AppleGothic"}.get(platform.system(), "NanumGothic")
# 마이너스(-) 기호가 네모로 깨지지 않게
plt.rcParams["axes.unicode_minus"] = False               # 마이너스(-) 기호가 네모로 깨지지 않게
IMG = Path(__file__).parent / "images"            # 그림을 저장할 폴더
IMG.mkdir(exist_ok=True)                                 # images 폴더 만들기 (이미 있으면 그냥 넘어가요)

import keras                                             # 딥러닝 도구 Keras
import numpy as np                                       # 넘파이 (관례적으로 np 라는 별명)

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
# x[0, ..., 0]: 첫 사진(0)의 첫 채널(0) → (28, 28) 흑백 그림. ... 은 "가운데 차원은 전부"
axes[0, 0].imshow(x[0, ..., 0], cmap="gray"); axes[0, 0].set_title(f"입력 {y_test[0]}")
axes[1, 0].axis("off")
for i in range(8):
    axes[0, i + 1].imshow(w[:, :, 0, i], cmap="bwr"); axes[0, i + 1].set_title(f"필터 {i}")
    # maps[..., i]: 모든 칸에서 i 번째 특징 맵(필터 i 가 찾은 결과)만 꺼내기
    axes[1, i + 1].imshow(maps[..., i], cmap="viridis"); axes[1, i + 1].set_title(f"특징 맵 {i}")
for ax in axes.flat:
    ax.set_xticks([]); ax.set_yticks([])
fig.savefig(IMG / "ex04_feature_maps.png", dpi=100, bbox_inches="tight")
