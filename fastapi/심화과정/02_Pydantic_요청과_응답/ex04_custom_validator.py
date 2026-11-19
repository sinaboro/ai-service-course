# ex04_custom_validator.py : 나만의 검사 규칙: field_validator(값 하나) · model_validator(여러 값 함께)
# 실행: 이 폴더에서 uvicorn ex04_custom_validator:app --reload (요청 예시는 ex04_custom_validator_client.py)
from fastapi import FastAPI
from pydantic import BaseModel, Field, field_validator, model_validator

app = FastAPI()                    # 앱(서버) 만들기 — uvicorn 이 이 app 을 실행해요


class Features(BaseModel):         # 모델 입력: 숫자 4개 (예: 꽃잎·꽃받침 길이)
    values: list[float] = Field(min_length=4, max_length=4)

    # field_validator: 필드 하나를 직접 검사하는 함수 (ValueError 를 내면 422 오류)
    @field_validator("values")
    @classmethod                   # field_validator 아래에는 꼭 @classmethod
    def no_negative(cls, v: list[float]) -> list[float]:
        if any(x < 0 for x in v):  # 값 중 하나라도 음수면
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
