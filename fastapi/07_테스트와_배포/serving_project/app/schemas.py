from pydantic import BaseModel, Field


class StudentFeatures(BaseModel):
    study_h: float = Field(ge=0, le=16, examples=[4.5])
    sleep_h: float = Field(ge=0, le=16, examples=[7.0])
    phone_h: float = Field(ge=0, le=24, examples=[2.0])


class Prediction(BaseModel):
    pass_probability: float
    label: str
    model_version: str


class BatchRequest(BaseModel):
    students: list[StudentFeatures] = Field(min_length=1)


class BatchResponse(BaseModel):
    count: int
    predictions: list[Prediction]
