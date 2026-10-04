# 요청 · 응답의 모양(스키마)만 모아 둔 파일
from pydantic import BaseModel, Field


# 한 학생의 입력값 3개와 허용 범위
class StudentFeatures(BaseModel):
    study_h: float = Field(ge=0, le=16, examples=[4.5])
    sleep_h: float = Field(ge=0, le=16, examples=[7.0])
    phone_h: float = Field(ge=0, le=24, examples=[2.0])


# 응답 하나
class Prediction(BaseModel):
    pass_probability: float
    label: str
    model_version: str


# 여러 명 요청 · 응답
class BatchRequest(BaseModel):
    students: list[StudentFeatures] = Field(min_length=1)


class BatchResponse(BaseModel):
    count: int
    predictions: list[Prediction]
