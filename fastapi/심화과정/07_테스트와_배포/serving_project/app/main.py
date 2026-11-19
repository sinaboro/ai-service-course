# main.py : 메인 앱: create_app() 으로 앱을 만들고 라우터를 연결
# 실행: serving_project 폴더에서 uvicorn app.main:app --reload
from contextlib import asynccontextmanager         # lifespan(켜질 때 · 꺼질 때 할 일)을 만드는 도구
from fastapi import FastAPI

from app.config import get_settings
from app.model import PassModel
from app.routers import health, predict


# 서버 시작: 설정 읽기 → 모델 파일이 있으면 불러오기 / 종료: 모델 해제
@asynccontextmanager
async def lifespan(app: FastAPI):
    settings = get_settings()
    app.state.settings = settings
    # 모델 파일이 있으면 불러오고, 없으면 None
    app.state.model = PassModel(settings.model_path) if settings.model_path.exists() else None
    yield                                          # yield 위 = 켜질 때, 아래 = 꺼질 때
    app.state.model = None


def create_app() -> FastAPI:                       # 앱을 만드는 함수 (테스트에서 새로 만들기 쉬움)
    app = FastAPI(title=get_settings().app_name, version="1.0.0", lifespan=lifespan)
    # 앱에 라우터 두 개 연결
    app.include_router(health.router)
    app.include_router(predict.router)
    return app


# uvicorn app.main:app 으로 실행할 때 쓰는 앱
app = create_app()
