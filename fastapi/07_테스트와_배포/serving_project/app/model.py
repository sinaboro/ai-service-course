import json
from pathlib import Path
import numpy as np


class PassModel:
    def __init__(self, path: Path):
        data = np.load(path)
        self.w, self.b = data["w"], float(data["b"])
        self.mean, self.std = data["mean"], data["std"]
        card = path.with_name("model_card.json")
        self.card = json.loads(card.read_text(encoding="utf-8")) if card.exists() else {}
        self.version = self.card.get("version", "unknown")

    def predict_proba(self, X: np.ndarray) -> np.ndarray:
        Z = (X - self.mean) / self.std
        return 1 / (1 + np.exp(-(Z @ self.w + self.b)))
