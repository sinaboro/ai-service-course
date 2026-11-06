# 설정: 환경 변수로 바꿀 수 있는 값들을 한 곳에
import os
from dataclasses import dataclass, field
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent          # serving_project 폴더


# frozen=True: 만든 뒤에는 값을 바꿀 수 없는 설정 객체
@dataclass(frozen=True)
class Settings:
    # default_factory: 설정 객체를 "만들 때마다" 환경 변수를 다시 읽어요
    app_name: str = field(default_factory=lambda: os.getenv("APP_NAME", "pass-predictor-api"))
    model_path: Path = field(default_factory=lambda: Path(os.getenv("MODEL_PATH", BASE_DIR / "model" / "pass_model.npz")))
    max_batch: int = field(default_factory=lambda: int(os.getenv("MAX_BATCH", "100")))


# 설정 객체를 돌려주는 함수 (의존성 · 테스트에서 바꿔 끼우기 쉬워요)
def get_settings() -> Settings:
    return Settings()
