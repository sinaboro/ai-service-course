from fastapi import APIRouter, Request

# 상태 확인 주소만 모은 라우터
router = APIRouter(tags=["status"])


# GET /health → 서버 상태 · 모델 준비 여부
@router.get("/health")
def health(request: Request):
    return {"status": "ok", "model_loaded": getattr(request.app.state, "model", None) is not None}
