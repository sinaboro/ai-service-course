# 10장 미니 프로젝트 서버: 할 일(todo) API + 화면 파일 제공
# 실행: 이 폴더에서  uvicorn app:app --reload   → 브라우저에서 http://127.0.0.1:8000
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

app = FastAPI()

# 데이터베이스 대신 리스트 (서버를 다시 켜면 이 두 개로 돌아가요)
todos = [
    {"id": 1, "title": "JavaScript 10장 읽기", "done": False},
    {"id": 2, "title": "FastAPI 서버 켜 보기", "done": True},
]
next_id = 3


class TodoIn(BaseModel):              # 새로 만들 때: 제목만 (1 ~ 50자)
    title: str = Field(min_length=1, max_length=50)


class TodoUpdate(BaseModel):          # 고칠 때: 바꾸고 싶은 것만 보내요
    title: str | None = Field(default=None, min_length=1, max_length=50)
    done: bool | None = None


def find(todo_id: int) -> dict:
    for t in todos:
        if t["id"] == todo_id:
            return t
    raise HTTPException(status_code=404, detail="그 할 일을 찾을 수 없어요")


@app.get("/api/todos")                # 목록
def list_todos():
    return todos


@app.post("/api/todos", status_code=201)   # 추가
def add_todo(data: TodoIn):
    global next_id
    todo = {"id": next_id, "title": data.title, "done": False}
    todos.append(todo)
    next_id += 1
    return todo


@app.patch("/api/todos/{todo_id}")    # 일부 고치기 (완료 표시, 제목 바꾸기)
def update_todo(todo_id: int, data: TodoUpdate):
    todo = find(todo_id)
    if data.title is not None:
        todo["title"] = data.title
    if data.done is not None:
        todo["done"] = data.done
    return todo


@app.delete("/api/todos/{todo_id}")   # 삭제
def delete_todo(todo_id: int):
    todos.remove(find(todo_id))
    return {"deleted": todo_id}


app.mount("/", StaticFiles(directory=Path(__file__).parent / "static", html=True), name="static")
