# 나의 미니 프로젝트 — 이 파일을 고쳐서 나만의 웹 서비스를 만들어요
# 실행: 이 폴더(my_project)에서  uvicorn main:app --reload  →  http://127.0.0.1:8000
#
# 만드는 순서 (교안 7장 4절)
#   1) 기획서(기획서.md)에 서비스 이름과 "API 설계표" 를 먼저 채워요
#   2) 아래 TODO ① ~ ④ 를 설계표대로 바꿔요
#   3) /docs 에서 API 를 하나씩 시험해요
#   4) index.html 화면을 꾸며요
import json
from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field

app = FastAPI(title="나의 미니 프로젝트")     # TODO ①: 서비스 이름으로 바꾸기
HERE = Path(__file__).parent
DATA_FILE = HERE / "data.json"


def load_items():
    if DATA_FILE.exists():
        return json.loads(DATA_FILE.read_text(encoding="utf-8"))
    return []


def save_items(items):
    DATA_FILE.write_text(json.dumps(items, ensure_ascii=False, indent=2), encoding="utf-8")


# TODO ②: 저장할 데이터의 모양을 정해요 (예: 맛집이면 이름·메뉴·별점)
class ItemIn(BaseModel):
    title: str = Field(min_length=1, max_length=30)
    score: int = Field(default=3, ge=1, le=5)


# TODO ③: 목록 보기 API — 필요하면 정렬·검색을 더해요
@app.get("/api/items")
def list_items():
    return load_items()


# TODO ④: 저장 API — 받은 값에 번호를 붙여 파일에 저장해요
@app.post("/api/items", status_code=201)
def add_item(item: ItemIn):
    items = load_items()
    new = {"id": len(items) + 1, **item.model_dump()}   # model_dump(): 받은 값을 딕셔너리로
    items.append(new)
    save_items(items)
    return new


# 화면
@app.get("/", include_in_schema=False)
def page():
    return FileResponse(HERE / "index.html")
