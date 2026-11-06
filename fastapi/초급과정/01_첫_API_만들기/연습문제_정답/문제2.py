# 문제 2. 쿼리로 키(height, cm)와 몸무게(weight, kg)를 받아 BMI 를 소수 1자리로 돌려주세요.
#        예) /bmi?height=175&weight=70 → {"bmi": 22.9}
#        BMI = 몸무게 ÷ (키 ÷ 100)²
# 실행: 이 폴더에서  uvicorn 문제2:app --reload  →  브라우저에서 /bmi?height=175&weight=70
from fastapi import FastAPI

app = FastAPI()


@app.get("/bmi")
def bmi(height: float, weight: float):       # float: 소수점이 있는 숫자도 받기
    value = weight / (height / 100) ** 2
    return {"height": height, "weight": weight, "bmi": round(value, 1)}
