from typing import Annotated
# Depends: "이 함수를 먼저 실행해서 그 결과를 넣어 줘" 라는 표시 / Query: 쿼리 값의 범위 정하기
from fastapi import Depends, FastAPI, Query

app = FastAPI()


# skip: 건너뛸 개수(0 이상), limit: 가져올 개수(1 ~ 50)
def pagination(skip: int = Query(0, ge=0), limit: int = Query(5, ge=1, le=50)):
    return {"skip": skip, "limit": limit}        # 여러 API 가 함께 쓰는 쿼리 묶음


Page = Annotated[dict, Depends(pagination)]      # 별명을 붙여 짧게 쓰기

# 1 ~ 100 숫자 목록 (실습용 데이터)
NUMBERS = list(range(1, 101))


@app.get("/numbers")
def numbers(page: Page):                          # FastAPI 가 pagination() 을 먼저 실행해 결과를 넣어 줌
    # 의존성 결과에서 skip, limit 꺼내기
    s, l = page["skip"], page["limit"]
    return {"page": page, "data": NUMBERS[s: s + l]}


@app.get("/squares")
def squares(page: Page):                          # 같은 의존성 재사용
    s, l = page["skip"], page["limit"]
    return {"page": page, "data": [n * n for n in NUMBERS[s: s + l]]}
