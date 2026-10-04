from fastapi import FastAPI
# BaseModel 을 물려받으면 "이런 모양의 JSON 을 받겠다"고 정할 수 있어요
from pydantic import BaseModel

app = FastAPI()


class Student(BaseModel):          # 요청 데이터의 "모양" 정의 (dataclass 와 비슷)
    # 각 줄 = 필드 이름: 자료형. 자료형이 맞지 않으면 FastAPI 가 422 오류로 돌려보내요
    name: str
    age: int
    score: float
    email: str | None = None       # 없어도 되는 값


@app.post("/students")             # POST: 데이터를 보내는 요청
def create_student(student: Student):           # 본문 JSON → Student 객체로 자동 변환
    # 받은 점수로 합격 여부 계산
    grade = "합격" if student.score >= 60 else "불합격"
    return {"received": student, "result": grade, "name_length": len(student.name)}
