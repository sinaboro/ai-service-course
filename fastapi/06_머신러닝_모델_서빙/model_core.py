# 모델 불러오기·예측을 담당하는 클래스 (서빙 앱은 이 클래스만 알면 됨)
import json
from pathlib import Path
import numpy as np


class PassModel:
    def __init__(self, w, b, mean, std, features, card):
        self.w, self.b, self.mean, self.std = w, b, mean, std
        self.features = list(features)
        self.card = card

    @classmethod
    def load(cls, path: str | Path) -> "PassModel":
        path = Path(path)
        data = np.load(path)                                    # FileNotFoundError 가능
        card_path = path.with_name("model_card.json")
        card = json.loads(card_path.read_text(encoding="utf-8")) if card_path.exists() else {}
        return cls(data["w"], float(data["b"]), data["mean"], data["std"], data["features"], card)

    @property
    def version(self) -> str:
        return self.card.get("version", "unknown")

    def predict_proba(self, X: np.ndarray) -> np.ndarray:
        Z = (X - self.mean) / self.std                          # 학습 때와 같은 전처리
        return 1 / (1 + np.exp(-(Z @ self.w + self.b)))


class ColorModel:
    def __init__(self, path: str | Path):
        data = np.load(path)
        self.proto, self.classes = data["proto"], list(data["classes"])
        self.version = "color-0.1"

    def predict_proba(self, x: np.ndarray) -> np.ndarray:      # x: (N, H, W, 3), 0 ~ 1
        mean_rgb = x.mean(axis=(1, 2))                          # 이미지마다 평균 색 (N, 3)
        dist = ((mean_rgb[:, None, :] - self.proto[None]) ** 2).sum(axis=2)   # 대표 색과의 거리
        logits = -dist * 20
        e = np.exp(logits - logits.max(axis=1, keepdims=True))
        return e / e.sum(axis=1, keepdims=True)                 # softmax → 확률
