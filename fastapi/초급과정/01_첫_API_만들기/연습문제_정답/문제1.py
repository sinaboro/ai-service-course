# 문제 1. 주소 /gugudan/{dan} 으로 단(dan)을 받아 그 단의 구구단 9줄을 리스트로 돌려주세요.
#        예) /gugudan/3 → {"dan": 3, "result": ["3 x 1 = 3", ..., "3 x 9 = 27"]}
# 실행: 이 폴더에서  uvicorn 문제1:app --reload  →  브라우저에서 /gugudan/3
from fastapi import FastAPI

app = FastAPI()


@app.get("/gugudan/{dan}")
def gugudan(dan: int):
    lines = [f"{dan} x {i} = {dan * i}" for i in range(1, 10)]   # 1 ~ 9 를 곱한 글자 9개
    return {"dan": dan, "result": lines}
