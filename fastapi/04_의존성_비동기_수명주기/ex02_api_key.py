from typing import Annotated
from fastapi import Depends, FastAPI, Header, HTTPException

app = FastAPI()
API_KEYS = {"team-a-123": "팀A", "team-b-456": "팀B"}     # 실제로는 환경 변수·DB 에 보관


def verify_key(x_api_key: Annotated[str | None, Header()] = None) -> str:   # 헤더 X-API-Key 읽기
    if x_api_key is None:
        raise HTTPException(status_code=401, detail="X-API-Key 헤더가 필요해요")
    if x_api_key not in API_KEYS:
        raise HTTPException(status_code=403, detail="유효하지 않은 API 키예요")
    return API_KEYS[x_api_key]


@app.get("/public")
def public():
    return {"message": "누구나 볼 수 있어요"}


@app.post("/predict")
def predict(team: Annotated[str, Depends(verify_key)]):     # 키 검사를 통과해야 실행
    return {"team": team, "prediction": "OK"}
