# model.py : 모델 클래스: 저장한 가중치를 불러와 합격 확률 계산 — 직접 실행하는 파일이 아니에요
import json  # JSON 글자 ↔ 파이썬 딕셔너리 바꾸기
from pathlib import Path  # 파일 · 폴더 경로를 다루는 도구
import numpy as np  # 넘파이 (관례적으로 np 라는 별명)


# 저장된 모델 파일(.npz)을 읽어 예측하는 클래스
class PassModel:
    def __init__(self, path: Path):
        # 가중치 · 절편 · 표준화용 평균 · 표준편차 꺼내기
        data = np.load(path)
        self.w, self.b = data["w"], float(data["b"])
        self.mean, self.std = data["mean"], data["std"]
        # 설명서(model_card.json)가 있으면 버전 정보 읽기
        card = path.with_name("model_card.json")
        # 설명서가 있으면 읽고, 없으면 빈 딕셔너리
        self.card = json.loads(card.read_text(encoding="utf-8")) if card.exists() else {}
        self.version = self.card.get("version", "unknown")  # version 이 없으면 "unknown"

    # 학습 때와 똑같이 표준화한 뒤 합격 확률 계산
    def predict_proba(self, X: np.ndarray) -> np.ndarray:
        Z = (X - self.mean) / self.std
        return 1 / (1 + np.exp(-(Z @ self.w + self.b)))
