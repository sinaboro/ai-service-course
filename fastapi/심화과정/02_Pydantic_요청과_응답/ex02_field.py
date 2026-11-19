# ex02_field.py : Field 로 값의 범위 · 글자 수를 정하고, 어기면 422 오류
# 실행: 이 폴더에서 uvicorn ex02_field:app --reload (요청 예시는 ex02_field_client.py)
from typing import Literal
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()                    # 앱(서버) 만들기 — uvicorn 이 이 app 을 실행해요


class HouseInput(BaseModel):       # 집값 예측 모델에 넣을 입력이라고 생각해 봐요
    # Field: 값의 범위 · 길이 · 설명을 정하기 (gt 초과, ge 이상, le 이하)
    area: float = Field(gt=0, le=500, description="전용면적(m2)", examples=[84.5])
    rooms: int = Field(ge=1, le=10, description="방 개수")
    built_year: int = Field(ge=1950, le=2026)
    # Literal: 적어 둔 값 중 하나만 허용
    region: Literal["서울", "경기", "부산", "기타"] = "기타"     # 정해진 값 중 하나만
    memo: str = Field(default="", max_length=20)


@app.post("/houses/check")
def check(house: HouseInput):
    # 건물 나이 계산 / model_dump(): 모델 → 사전
    age = 2026 - house.built_year
    return {"ok": True, "house_age": age, "input": house.model_dump()}
