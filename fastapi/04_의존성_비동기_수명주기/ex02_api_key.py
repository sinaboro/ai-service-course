from typing import Annotated
# Header(): 요청 헤더에서 값 읽기 (이름 x_api_key → 헤더 X-API-Key)
from fastapi import Depends, FastAPI, Header, HTTPException

app = FastAPI()
API_KEYS = {"team-a-123": "팀A", "team-b-456": "팀B"}     # 실제로는 환경 변수·DB 에 보관


def verify_key(x_api_key: Annotated[str | None, Header()] = None) -> str:   # 헤더 X-API-Key 읽기
    # 키가 없으면 401(인증 필요), 틀리면 403(권한 없음)
    if x_api_key is None:
        raise HTTPException(status_code=401, detail="X-API-Key 헤더가 필요해요")
    if x_api_key not in API_KEYS:
        raise HTTPException(status_code=403, detail="유효하지 않은 API 키예요")
    # 통과하면 팀 이름을 돌려줘요 → predict 의 team 변수로 들어가요
    return API_KEYS[x_api_key]


# 키 검사가 없는 공개 API
@app.get("/public")
def public():
    return {"message": "누구나 볼 수 있어요"}


@app.post("/predict")
def predict(team: Annotated[str, Depends(verify_key)]):     # 키 검사를 통과해야 실행
    return {"team": team, "prediction": "OK"}
