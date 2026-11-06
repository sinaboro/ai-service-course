# 1) 데이터 만들기 → 2) 학습 → 3) 평가 → 4) 저장
import json
from pathlib import Path
import numpy as np
from PIL import Image, ImageDraw

# 모델 · 샘플 이미지를 저장할 폴더 만들기
HERE = Path(__file__).parent
(HERE / "model").mkdir(exist_ok=True)
(HERE / "samples").mkdir(exist_ok=True)

# ── 1) 학생 생활 데이터 (시각화 6장과 같은 규칙) ──
rng = np.random.default_rng(seed=2026)
n = 400
# 공부 · 수면 · 휴대폰 시간으로 점수를 만드는 규칙 (공부 ↑ 점수 ↑, 휴대폰 ↑ 점수 ↓) + 잡음
study = rng.uniform(0, 6, n)
sleep = 8.5 - study * 0.35 + rng.normal(0, 0.6, n)
phone = (5 - study * 0.5 + rng.normal(0, 1, n)).clip(0.5)
score = (50 + study * 7 - phone * 2 + rng.normal(0, 6, n)).clip(0, 100)
X = np.column_stack([study, sleep, phone])          # 입력 3개
y = (score >= 60).astype(float)                     # 정답: 합격 1, 불합격 0
FEATURES = ["study_h", "sleep_h", "phone_h"]

# ── 2) 학습: 표준화 + 로지스틱 회귀 (경사하강법) ──
idx = rng.permutation(n)
train, test = idx[:320], idx[320:]                  # 80% 학습 / 20% 평가
mean, std = X[train].mean(axis=0), X[train].std(axis=0)
Z = (X - mean) / std                                # 표준화 (서빙 때도 똑같이 해야 함!)

# 경사하강법 3000번: 예측 확률과 정답의 차이(grad)만큼 가중치를 조금씩 고쳐요
w, b = np.zeros(3), 0.0
for step in range(3000):
    p = 1 / (1 + np.exp(-(Z[train] @ w + b)))       # 시그모이드 → 합격 확률
    grad = p - y[train]
    w -= 0.1 * Z[train].T @ grad / len(train)
    b -= 0.1 * grad.mean()

# ── 3) 평가 ──
# 평가 데이터로 정확도 계산: 확률 0.5 이상이면 합격으로 예측
p_test = 1 / (1 + np.exp(-(Z[test] @ w + b)))
acc = float(((p_test >= 0.5) == y[test]).mean())
print("가중치:", np.round(w, 3), "절편:", round(b, 3))
print(f"평가 정확도: {acc:.1%}  (평가 데이터 {len(test)}명)")

# ── 4) 저장: 가중치 + 전처리 정보 + 설명서 ──
np.savez(HERE / "model" / "pass_model.npz", w=w, b=b, mean=mean, std=std, features=np.array(FEATURES))
card = {"name": "pass-predictor", "version": "1.0.0", "features": FEATURES,
        "algorithm": "logistic regression (numpy)", "test_accuracy": round(acc, 4), "trained_on": 320}
(HERE / "model" / "model_card.json").write_text(json.dumps(card, ensure_ascii=False, indent=2), encoding="utf-8")
print("저장:", sorted(p.name for p in (HERE / "model").iterdir()))

# ── (이미지 분류용) 색 분류 모델과 샘플 이미지 ──
# 클래스별 대표 색(0 ~ 1 의 RGB)
CLASSES = ["red", "green", "blue"]
proto = np.array([[0.86, 0.16, 0.16], [0.16, 0.71, 0.27], [0.16, 0.31, 0.86]])   # 클래스별 대표 색
np.savez(HERE / "model" / "color_model.npz", proto=proto, classes=np.array(CLASSES))
# 샘플 이미지 4장 (보라색은 학습에 없는 색 → 모델이 어떻게 답하는지 보기)
for name, color in [("red", (220, 40, 40)), ("green", (40, 180, 70)), ("blue", (40, 80, 220)), ("purple", (140, 60, 200))]:
    img = Image.new("RGB", (160, 120), color)
    ImageDraw.Draw(img).rectangle((0, 0, 159, 20), fill="white")    # 위쪽에 흰 띠
    img.save(HERE / "samples" / f"{name}.png")
print("샘플 이미지:", sorted(p.name for p in (HERE / "samples").iterdir()))
