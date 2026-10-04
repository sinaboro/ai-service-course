from typing import Annotated
from fastapi import Depends, HTTPException, Request
from app.model import PassModel


# 의존성: 앱에 불러 둔 모델 꺼내기 (없으면 503 오류)
def get_model(request: Request) -> PassModel:
    model = getattr(request.app.state, "model", None)
    if model is None:
        raise HTTPException(503, "모델이 준비되지 않았어요")
    return model


# API 함수에서 model: ModelDep 로 쓰면 이 의존성이 실행돼요
ModelDep = Annotated[PassModel, Depends(get_model)]
