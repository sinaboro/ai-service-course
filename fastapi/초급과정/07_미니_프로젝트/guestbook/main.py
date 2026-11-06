# 7장 미니 프로젝트 예시: 방명록 — 서버를 껐다 켜도 글이 남아 있어요 (posts.json 파일에 저장)
# 실행: 이 폴더(guestbook)에서  uvicorn main:app --reload
# 확인: 브라우저에서 http://127.0.0.1:8000
# 친구 폰에서 접속: uvicorn main:app --host 0.0.0.0  → 친구 폰 브라우저에 http://내컴퓨터IP:8000 (교안 7장 3절)
import json
from datetime import datetime
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field

app = FastAPI(title="방명록")
HERE = Path(__file__).parent
DATA_FILE = HERE / "posts.json"               # 글을 저장할 파일


# ── 파일 읽기 · 쓰기 (0장 4절의 JSON) ──
def load_posts():
    if DATA_FILE.exists():
        return json.loads(DATA_FILE.read_text(encoding="utf-8"))
    return []                                 # 파일이 없으면(처음) 빈 목록


def save_posts(posts):
    DATA_FILE.write_text(json.dumps(posts, ensure_ascii=False, indent=2), encoding="utf-8")


# ── 받을 데이터 모양 (2장) ──
class PostIn(BaseModel):
    name: str = Field(min_length=1, max_length=10)        # 이름 1 ~ 10글자
    message: str = Field(min_length=1, max_length=100)    # 남길 말 1 ~ 100글자


# ── API (3장) ──
@app.get("/api/posts")
def list_posts():
    return list(reversed(load_posts()))       # 최신 글이 위로 오게 뒤집어서


@app.post("/api/posts", status_code=201)
def write_post(post: PostIn):
    posts = load_posts()
    new_id = posts[-1]["id"] + 1 if posts else 1          # 마지막 번호 + 1
    new_post = {"id": new_id, "name": post.name, "message": post.message,
                "time": datetime.now().strftime("%m-%d %H:%M")}
    posts.append(new_post)
    save_posts(posts)                         # 파일에 저장 → 서버를 꺼도 남아요
    return new_post


@app.delete("/api/posts/{post_id}")
def delete_post(post_id: int):
    posts = load_posts()
    left = [p for p in posts if p["id"] != post_id]       # 그 번호만 빼고 남기기
    if len(left) == len(posts):
        raise HTTPException(status_code=404, detail=f"{post_id}번 글이 없어요")
    save_posts(left)
    return {"message": f"{post_id}번 글을 지웠어요"}


# ── 화면 (4장) ──
@app.get("/", include_in_schema=False)
def page():
    return FileResponse(HERE / "index.html")
