from typing import Literal
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class HouseInput(BaseModel):       # 집값 예측 모델에 넣을 입력이라고 생각해 봐요
    area: float = Field(gt=0, le=500, description="전용면적(m2)", examples=[84.5])
    rooms: int = Field(ge=1, le=10, description="방 개수")
    built_year: int = Field(ge=1950, le=2026)
    region: Literal["서울", "경기", "부산", "기타"] = "기타"     # 정해진 값 중 하나만
    memo: str = Field(default="", max_length=20)


@app.post("/houses/check")
def check(house: HouseInput):
    age = 2026 - house.built_year
    return {"ok": True, "house_age": age, "input": house.model_dump()}
