from typing import Annotated
from fastapi import Depends, HTTPException, Request
from app.model import PassModel


def get_model(request: Request) -> PassModel:
    model = getattr(request.app.state, "model", None)
    if model is None:
        raise HTTPException(503, "모델이 준비되지 않았어요")
    return model


ModelDep = Annotated[PassModel, Depends(get_model)]
