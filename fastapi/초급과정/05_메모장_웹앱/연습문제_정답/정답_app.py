# 5장 연습문제 정답 (문제 1 · 2 를 모두 반영한 메모장)
# 문제 1. 메모 옆에 글자 수를 "(12자)" 처럼 표시하세요.            → 화면(정답_page.html)만 고치면 돼요
# 문제 2. [모두 지우기] 버튼을 만들고, 누르면 메모가 전부 지워지게 하세요. → API 에 DELETE /memos 추가 + 버튼
# 실행: 정답 폴더에서  uvicorn 정답_app:app --reload  →  http://127.0.0.1:8000
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field

app = FastAPI(title="메모장 웹 앱")
HERE = Path(__file__).parent


# 화면: 주소 "/" 로 들어오면 memo_page.html 을 돌려줘요 (4장 1단계)
@app.get("/", include_in_schema=False)
def page():
    return FileResponse(HERE / "정답_page.html")


# ── 아래는 3장 메모장 API 와 똑같아요 ──
# 메모를 만들거나 고칠 때 받는 모양
class MemoIn(BaseModel):
    text: str = Field(min_length=1, max_length=100)


# 메모를 저장할 곳: 번호 → 메모 글자 (서버를 끄면 사라져요)
memos = {}
next_id = 1                                   # 다음에 만들 메모 번호


# C: 메모 만들기 — status_code=201 은 "새로 만들었어요" 라는 성공 코드
@app.post("/memos", status_code=201)
def create_memo(memo: MemoIn):
    global next_id                            # 함수 밖의 next_id 를 바꾸겠다는 표시
    memos[next_id] = memo.text
    result = {"id": next_id, "text": memo.text}
    next_id += 1
    return result


# R: 메모 전체 보기
@app.get("/memos")
def list_memos():
    return [{"id": i, "text": t} for i, t in memos.items()]


# R: 메모 하나 보기 — 없는 번호면 404 오류
@app.get("/memos/{memo_id}")
def read_memo(memo_id: int):
    if memo_id not in memos:
        # raise HTTPException: "여기서 멈추고 이 오류를 응답으로 보내요"
        raise HTTPException(status_code=404, detail=f"{memo_id}번 메모가 없어요")
    return {"id": memo_id, "text": memos[memo_id]}


# U: 메모 고치기
@app.put("/memos/{memo_id}")
def update_memo(memo_id: int, memo: MemoIn):
    if memo_id not in memos:
        raise HTTPException(status_code=404, detail=f"{memo_id}번 메모가 없어요")
    memos[memo_id] = memo.text
    return {"id": memo_id, "text": memo.text}


# D: 메모 지우기
@app.delete("/memos/{memo_id}")
def delete_memo(memo_id: int):
    if memo_id not in memos:
        raise HTTPException(status_code=404, detail=f"{memo_id}번 메모가 없어요")
    del memos[memo_id]
    return {"message": f"{memo_id}번 메모를 지웠어요"}


# 문제 2: 메모 전부 지우기 — DELETE /memos (번호 없이)
@app.delete("/memos")
def delete_all():
    count = len(memos)
    memos.clear()                             # 딕셔너리 비우기
    return {"message": f"메모 {count}개를 모두 지웠어요"}
