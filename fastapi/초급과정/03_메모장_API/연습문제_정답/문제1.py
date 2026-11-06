# 문제 1. 메모장 API 에 "글자로 검색" 기능을 더하세요.
#        GET /search?keyword=우유 → keyword 가 들어간 메모만 리스트로 돌려주기
# 실행: 이 폴더에서  uvicorn 문제1:app --reload  →  /docs 에서 메모를 몇 개 만든 뒤 /search 시험
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class MemoIn(BaseModel):
    text: str = Field(min_length=1, max_length=100)


memos = {}
next_id = 1


@app.post("/memos", status_code=201)
def create_memo(memo: MemoIn):
    global next_id
    memos[next_id] = memo.text
    result = {"id": next_id, "text": memo.text}
    next_id += 1
    return result


# 새로 만든 검색 기능: keyword 가 들어간 메모만 골라 담기
@app.get("/search")
def search(keyword: str):
    return [{"id": i, "text": t} for i, t in memos.items() if keyword in t]
