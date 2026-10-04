import numpy as np
from fastapi import APIRouter, HTTPException, Request

from app.deps import ModelDep
from app.schemas import BatchRequest, BatchResponse, Prediction, StudentFeatures

router = APIRouter(prefix="/predict", tags=["predict"])


def _to_array(items: list[StudentFeatures]) -> np.ndarray:
    return np.array([[s.study_h, s.sleep_h, s.phone_h] for s in items])


def _pred(p: float, version: str) -> Prediction:
    return Prediction(pass_probability=round(float(p), 4), label="합격" if p >= 0.5 else "불합격", model_version=version)


@router.post("", response_model=Prediction)
def predict(student: StudentFeatures, model: ModelDep):
    return _pred(model.predict_proba(_to_array([student]))[0], model.version)


@router.post("/batch", response_model=BatchResponse)
def predict_batch(req: BatchRequest, model: ModelDep, request: Request):
    limit = request.app.state.settings.max_batch
    if len(req.students) > limit:
        raise HTTPException(413, f"한 번에 최대 {limit}명까지 예측할 수 있어요")
    probs = model.predict_proba(_to_array(req.students))
    return BatchResponse(count=len(probs), predictions=[_pred(p, model.version) for p in probs])
