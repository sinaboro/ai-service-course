# 모델 학습 → model/ 폴더에 저장 (06장 ex00 과 같은 방법)
import json
from pathlib import Path
import numpy as np

OUT = Path(__file__).parent / "model"
OUT.mkdir(exist_ok=True)
rng = np.random.default_rng(seed=2026)
n = 400
study = rng.uniform(0, 6, n)
sleep = 8.5 - study * 0.35 + rng.normal(0, 0.6, n)
phone = (5 - study * 0.5 + rng.normal(0, 1, n)).clip(0.5)
score = (50 + study * 7 - phone * 2 + rng.normal(0, 6, n)).clip(0, 100)
X, y = np.column_stack([study, sleep, phone]), (score >= 60).astype(float)

idx = rng.permutation(n)
tr, te = idx[:320], idx[320:]
mean, std = X[tr].mean(axis=0), X[tr].std(axis=0)
Z = (X - mean) / std
w, b = np.zeros(3), 0.0
for _ in range(3000):
    p = 1 / (1 + np.exp(-(Z[tr] @ w + b)))
    w -= 0.1 * Z[tr].T @ (p - y[tr]) / len(tr)
    b -= 0.1 * (p - y[tr]).mean()
acc = float(((1 / (1 + np.exp(-(Z[te] @ w + b))) >= 0.5) == y[te]).mean())

np.savez(OUT / "pass_model.npz", w=w, b=b, mean=mean, std=std)
(OUT / "model_card.json").write_text(json.dumps(
    {"name": "pass-predictor", "version": "1.0.0", "test_accuracy": round(acc, 4)}, indent=2), encoding="utf-8")
print(f"학습 완료: 정확도 {acc:.1%} → {sorted(p.name for p in OUT.iterdir())}")
