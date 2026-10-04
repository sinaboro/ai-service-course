from fastapi import FastAPI
from routers import items, models          # routers 폴더의 두 파일

app = FastAPI(title="라우터로 나눈 API")
app.include_router(items.router)            # /items ...
app.include_router(models.router)           # /models ...


@app.get("/")
def root():
    return {"routes": sorted(app.openapi()["paths"])}   # 문서(OpenAPI)에 등록된 주소 목록
