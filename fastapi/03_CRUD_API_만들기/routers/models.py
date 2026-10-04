from fastapi import APIRouter

router = APIRouter(prefix="/models", tags=["models"])

MODELS = [{"name": "house-price", "version": "1.2.0"}, {"name": "iris-classifier", "version": "0.9.1"}]


@router.get("", summary="서빙 중인 모델 목록")
def list_models():
    return MODELS
