from fastapi import FastAPI
from pydantic import BaseModel, Field, field_validator, model_validator

app = FastAPI()


class Features(BaseModel):         # 모델 입력: 숫자 4개 (예: 꽃잎·꽃받침 길이)
    values: list[float] = Field(min_length=4, max_length=4)

    # field_validator: 필드 하나를 직접 검사하는 함수 (ValueError 를 내면 422 오류)
    @field_validator("values")
    @classmethod
    def no_negative(cls, v: list[float]) -> list[float]:
        if any(x < 0 for x in v):
            raise ValueError("음수 값은 넣을 수 없어요")
        return [round(x, 2) for x in v]           # 검사 + 정리(반올림)까지


# 두 필드를 비교하려면 model_validator (모든 값이 들어온 뒤 실행)
class DateRange(BaseModel):
    start: int
    end: int

    @model_validator(mode="after")             # 여러 필드를 함께 검사
    def check_order(self):
        if self.start > self.end:
            raise ValueError("start 는 end 보다 클 수 없어요")
        return self


@app.post("/features")
def features(f: Features):
    return {"values": f.values, "sum": round(sum(f.values), 2)}


@app.post("/range")
def date_range(r: DateRange):
    return {"days": r.end - r.start}
