# AI 모델을 "함수 하나" 로 쓰게 해 주는 파일 — 안쪽은 몰라도 괜찮아요!
#
# 사용법:  from ai_model import predict
#          확률 = predict(공부시간, 수면시간, 휴대폰시간)     → 0 ~ 1 사이의 합격 확률
#
# 이 모델은 학생 400명의 생활 시간과 합격 여부를 보고 미리 "학습" 해 둔 거예요.
# 학습 결과(숫자 몇 개)가 model/pass_model.json 에 저장되어 있고, 이 파일은 그 숫자로 계산만 해요.
import json
import math
from pathlib import Path

# 파일을 처음 불러올 때 딱 한 번 학습 결과를 읽어 둬요
_m = json.loads((Path(__file__).parent / "model" / "pass_model.json").read_text(encoding="utf-8"))


def predict(study_h: float, sleep_h: float, phone_h: float) -> float:
    """하루 공부 · 수면 · 휴대폰 시간을 넣으면 합격 확률(0 ~ 1)을 돌려줘요."""
    values = [study_h, sleep_h, phone_h]
    # 학습 때와 같은 기준으로 값을 맞추고(평균을 빼고 나누기), 가중치를 곱해 더해요
    score = _m["bias"]
    for v, mean, std, w in zip(values, _m["mean"], _m["std"], _m["weights"]):
        score += (v - mean) / std * w
    # 점수를 0 ~ 1 사이의 확률로 바꾸기 (시그모이드 함수)
    return 1 / (1 + math.exp(-score))
