from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI(title="Todo API")


class TodoCreate(BaseModel):                 # 만들 때 받는 값
    title: str = Field(min_length=1, max_length=50)
    priority: int = Field(default=3, ge=1, le=5)


class TodoUpdate(BaseModel):                 # 일부 수정 (모두 선택)
    title: str | None = Field(default=None, min_length=1, max_length=50)
    priority: int | None = Field(default=None, ge=1, le=5)
    done: bool | None = None


class Todo(TodoCreate):                      # 저장·응답 모양 (상속으로 필드 재사용)
    id: int
    done: bool = False


# 실제 서비스는 데이터베이스를 쓰지만, 여기서는 사전에 저장해요 (서버를 끄면 사라져요)
DB: dict[int, Todo] = {}                     # 실습용 "메모리 데이터베이스"
next_id = 1


# 번호로 할 일을 찾고, 없으면 404 오류를 내는 도우미 함수 (여러 곳에서 재사용)
def get_or_404(todo_id: int) -> Todo:
    if todo_id not in DB:
        raise HTTPException(status_code=404, detail=f"{todo_id}번 할 일이 없어요")
    return DB[todo_id]


@app.post("/todos", response_model=Todo, status_code=status.HTTP_201_CREATED, tags=["todos"])
def create_todo(data: TodoCreate):           # C: 만들기
    # 다음 번호를 바꿔야 하니 global 로 함수 밖의 변수를 쓰겠다고 알리기
    global next_id
    # 받은 값 + 새 번호로 Todo 만들기 → 저장 → 번호 1 증가
    todo = Todo(id=next_id, **data.model_dump())
    DB[next_id] = todo
    next_id += 1
    return todo


@app.get("/todos", response_model=list[Todo], tags=["todos"])
def list_todos(done: bool | None = None, skip: int = 0, limit: int = 10):   # R: 목록 (필터 + 페이지)
    items = list(DB.values())
    # done 쿼리가 있으면 완료 여부로 걸러 내기
    if done is not None:
        items = [t for t in items if t.done == done]
    return items[skip: skip + limit]


@app.get("/todos/{todo_id}", response_model=Todo, tags=["todos"])
def read_todo(todo_id: int):                 # R: 하나
    return get_or_404(todo_id)


@app.put("/todos/{todo_id}", response_model=Todo, tags=["todos"])
def replace_todo(todo_id: int, data: TodoCreate):    # U: 전체 바꾸기
    # 기존 done 값은 유지하고 나머지를 새 값으로 통째로 바꾸기
    old = get_or_404(todo_id)
    DB[todo_id] = Todo(id=todo_id, done=old.done, **data.model_dump())
    return DB[todo_id]


@app.patch("/todos/{todo_id}", response_model=Todo, tags=["todos"])
def update_todo(todo_id: int, data: TodoUpdate):     # U: 보낸 값만 바꾸기
    old = get_or_404(todo_id)
    changes = data.model_dump(exclude_unset=True)    # 실제로 보낸 필드만
    DB[todo_id] = old.model_copy(update=changes)
    return DB[todo_id]


@app.delete("/todos/{todo_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["todos"])
def delete_todo(todo_id: int):               # D: 삭제
    # 204 No Content: 삭제 성공, 돌려줄 본문은 없어요
    get_or_404(todo_id)
    del DB[todo_id]
