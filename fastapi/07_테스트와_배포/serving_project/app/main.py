from contextlib import asynccontextmanager
from fastapi import FastAPI

from app.config import get_settings
from app.model import PassModel
from app.routers import health, predict


@asynccontextmanager
async def lifespan(app: FastAPI):
    settings = get_settings()
    app.state.settings = settings
    app.state.model = PassModel(settings.model_path) if settings.model_path.exists() else None
    yield
    app.state.model = None


def create_app() -> FastAPI:                       # 앱을 만드는 함수 (테스트에서 새로 만들기 쉬움)
    app = FastAPI(title=get_settings().app_name, version="1.0.0", lifespan=lifespan)
    app.include_router(health.router)
    app.include_router(predict.router)
    return app


app = create_app()
