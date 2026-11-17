# 9장 서버: 방명록 API + 화면 파일(HTML · CSS · JS) 제공
# 실행: 이 폴더에서  uvicorn main:app --reload   → 브라우저에서 http://127.0.0.1:8000
# 필요한 것: pip install fastapi uvicorn
from datetime import datetime
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

app = FastAPI()

# CORS: 다른 주소(Live Server 의 5500 포트)에서 연 페이지가 이 서버(8000 포트)에 요청해도 허락해요
# 서버가 직접 보내 준 페이지(http://127.0.0.1:8000)로 열면 이 설정이 없어도 돼요
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500", "http://localhost:5500"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# 데이터베이스 대신 파이썬 리스트에 저장 (서버를 끄면 처음으로 돌아가요)
messages = [{"id": 1, "name": "선생님", "text": "방명록에 첫 글을 남겨 보세요!"}]
next_id = 2


# 화면에서 보낼 JSON 의 모양과 규칙: 이름 1 ~ 10자, 내용 1 ~ 100자
class MessageIn(BaseModel):
    name: str = Field(min_length=1, max_length=10)
    text: str = Field(min_length=1, max_length=100)


@app.get("/api/hello")
def hello():
    # 서버의 현재 시각을 함께 돌려줘요 (누를 때마다 바뀌는 것을 확인)
    return {"message": "안녕하세요! FastAPI 서버예요", "time": datetime.now().strftime("%H:%M:%S")}


@app.get("/api/messages")
def list_messages():
    return messages


@app.post("/api/messages", status_code=201)
def add_message(data: MessageIn):
    global next_id
    item = {"id": next_id, "name": data.name, "text": data.text}
    messages.append(item)
    next_id += 1
    return item                      # 새로 만든 글(번호 포함)을 돌려줘요


@app.delete("/api/messages/{message_id}")
def delete_message(message_id: int):
    for m in messages:
        if m["id"] == message_id:
            messages.remove(m)
            return {"deleted": message_id}
    raise HTTPException(status_code=404, detail="그 글을 찾을 수 없어요")


# static 폴더의 파일을 그대로 보내 줘요. "/" 로 열면 static/index.html
# ⚠️ API 주소보다 아래에 둬야 /api/... 요청이 가로채이지 않아요
app.mount("/", StaticFiles(directory=Path(__file__).parent / "static", html=True), name="static")
