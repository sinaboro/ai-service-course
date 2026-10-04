from fastapi import APIRouter

# 모델 관련 주소를 모은 라우터: 모든 주소가 /models 로 시작
router = APIRouter(prefix="/models", tags=["models"])

# 서빙 중인 모델 목록 (실습용 고정 값)
MODELS = [{"name": "house-price", "version": "1.2.0"}, {"name": "iris-classifier", "version": "0.9.1"}]


# GET /models → 목록 그대로 JSON 으로
@router.get("", summary="서빙 중인 모델 목록")
def list_models():
    return MODELS
