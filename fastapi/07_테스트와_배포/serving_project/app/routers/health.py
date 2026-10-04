from fastapi import APIRouter, Request

router = APIRouter(tags=["status"])


@router.get("/health")
def health(request: Request):
    return {"status": "ok", "model_loaded": getattr(request.app.state, "model", None) is not None}
