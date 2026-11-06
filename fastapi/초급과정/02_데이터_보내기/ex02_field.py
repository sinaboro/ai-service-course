# 2장 예제 2: Field 로 값의 규칙 정하기 — 이상한 값은 서버가 알아서 막아요
# 실행: 이 폴더에서  uvicorn ex02_field:app --reload
# 확인: /docs 에서 age 에 -5 나 200, name 에 "" 를 넣어 보내 보세요 → 422 오류
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class Member(BaseModel):
    # min_length / max_length : 글자 수 범위
    name: str = Field(min_length=1, max_length=10)
    # ge(크거나 같다) / le(작거나 같다) : 숫자 범위
    age: int = Field(ge=0, le=150)


@app.post("/join")
def join(member: Member):
    # 여기까지 왔다면 규칙을 모두 통과한 값이에요 (검사 코드를 따로 쓸 필요가 없어요)
    return {"message": f"{member.name}님, 가입을 환영해요!"}
