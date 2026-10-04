from fastapi import FastAPI

app = FastAPI()

ITEMS = {1: "노트북", 2: "마우스", 3: "키보드", 4: "모니터", 5: "스피커"}


@app.get("/items/{item_id}")                       # 경로 매개변수: 주소 안의 값
def read_item(item_id: int):                       # int 힌트 → "3" 이 3 으로 변환
    return {"item_id": item_id, "name": ITEMS.get(item_id, "없는 상품")}


@app.get("/items")                                 # 쿼리 매개변수: ?skip=0&limit=2
def list_items(skip: int = 0, limit: int = 3, keyword: str | None = None):
    names = list(ITEMS.values())
    if keyword:
        names = [n for n in names if keyword in n]
    return {"skip": skip, "limit": limit, "keyword": keyword, "items": names[skip: skip + limit]}


@app.get("/calc/add")
def add(a: float, b: float):                       # 기본값이 없으면 "필수" 쿼리
    return {"a": a, "b": b, "result": a + b}
