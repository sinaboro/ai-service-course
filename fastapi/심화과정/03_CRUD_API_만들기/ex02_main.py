# ex02_main.py : 메인 앱: routers 폴더의 라우터 두 개를 모아 하나의 앱으로
# 실행: 이 폴더(03_CRUD_API_만들기)에서 uvicorn ex02_main:app --reload
from fastapi import FastAPI
from routers import items, models          # routers 폴더의 두 파일

app = FastAPI(title="라우터로 나눈 API")
app.include_router(items.router)            # /items ...
app.include_router(models.router)           # /models ...


@app.get("/")
def root():
    return {"routes": sorted(app.openapi()["paths"])}   # 문서(OpenAPI)에 등록된 주소 목록
