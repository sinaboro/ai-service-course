# 모델 불러오기·예측을 담당하는 클래스 (서빙 앱은 이 클래스만 알면 됨)
import json
from pathlib import Path
import numpy as np


# 학습한 값(가중치 · 절편 · 평균 · 표준편차)과 설명서(card)를 들고 있는 모델 클래스
class PassModel:
    def __init__(self, w, b, mean, std, features, card):
        self.w, self.b, self.mean, self.std = w, b, mean, std
        self.features = list(features)
        self.card = card

    # classmethod: 객체 없이 PassModel.load(경로) 로 불러서 새 객체를 만드는 함수
    @classmethod
    def load(cls, path: str | Path) -> "PassModel":
        path = Path(path)
        data = np.load(path)                                    # FileNotFoundError 가능
        # 같은 폴더의 model_card.json 이 있으면 읽고, 없으면 빈 사전
        card_path = path.with_name("model_card.json")
        card = json.loads(card_path.read_text(encoding="utf-8")) if card_path.exists() else {}
        return cls(data["w"], float(data["b"]), data["mean"], data["std"], data["features"], card)

    # property: 함수지만 model.version 처럼 괄호 없이 읽어요
    @property
    def version(self) -> str:
        return self.card.get("version", "unknown")

    # 표준화 → 가중합 → 시그모이드 = 합격 확률
    def predict_proba(self, X: np.ndarray) -> np.ndarray:
        Z = (X - self.mean) / self.std                          # 학습 때와 같은 전처리
        return 1 / (1 + np.exp(-(Z @ self.w + self.b)))


# 색 분류 모델: 이미지 평균 색이 어느 대표 색과 가장 가까운지로 분류
class ColorModel:
    def __init__(self, path: str | Path):
        data = np.load(path)
        self.proto, self.classes = data["proto"], list(data["classes"])
        self.version = "color-0.1"

    def predict_proba(self, x: np.ndarray) -> np.ndarray:      # x: (N, H, W, 3), 0 ~ 1
        mean_rgb = x.mean(axis=(1, 2))                          # 이미지마다 평균 색 (N, 3)
        dist = ((mean_rgb[:, None, :] - self.proto[None]) ** 2).sum(axis=2)   # 대표 색과의 거리
        # 거리가 가까울수록 점수가 크도록 음수로 → softmax 로 확률
        logits = -dist * 20
        e = np.exp(logits - logits.max(axis=1, keepdims=True))
        return e / e.sum(axis=1, keepdims=True)                 # softmax → 확률
