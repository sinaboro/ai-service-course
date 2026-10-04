from fastapi import FastAPI

app = FastAPI()

# 실습용 상품 목록 (번호: 이름)
ITEMS = {1: "노트북", 2: "마우스", 3: "키보드", 4: "모니터", 5: "스피커"}


@app.get("/items/{item_id}")                       # 경로 매개변수: 주소 안의 값
def read_item(item_id: int):                       # int 힌트 → "3" 이 3 으로 변환
    # ITEMS.get(번호, 기본값): 없는 번호면 "없는 상품"
    return {"item_id": item_id, "name": ITEMS.get(item_id, "없는 상품")}


@app.get("/items")                                 # 쿼리 매개변수: ?skip=0&limit=2
def list_items(skip: int = 0, limit: int = 3, keyword: str | None = None):
    # 상품 이름만 리스트로 꺼내기
    names = list(ITEMS.values())
    # keyword 가 있으면 그 글자가 들어간 이름만 남기기
    if keyword:
        names = [n for n in names if keyword in n]
    # names[skip: skip + limit]: skip 번째부터 limit 개만 잘라서 돌려주기 (페이지 나누기)
    return {"skip": skip, "limit": limit, "keyword": keyword, "items": names[skip: skip + limit]}


@app.get("/calc/add")
def add(a: float, b: float):                       # 기본값이 없으면 "필수" 쿼리
    return {"a": a, "b": b, "result": a + b}
