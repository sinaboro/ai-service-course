# 웹 페이지에서 할 일 API 쓰기 — ex01_todo_crud 의 API 에 화면(HTML)을 붙여요 (서버로 실행)
# 실행: 이 폴더에서  uvicorn ex03_todo_web:app --reload
# 확인: 브라우저에서  http://127.0.0.1:8000  → 할 일을 추가·완료·삭제해 보세요
from pathlib import Path

from fastapi.responses import FileResponse

# ex01_todo_crud.py 의 앱(할 일 API 가 모두 들어 있는)을 그대로 가져와요
from ex01_todo_crud import app

HERE = Path(__file__).parent                   # 이 파일이 있는 폴더


# 주소 "/" 로 들어오면 JSON 대신 HTML 파일(웹 페이지)을 돌려줘요
# include_in_schema=False: /docs 문서에는 보이지 않게 (API 가 아니라 화면이니까요)
@app.get("/", include_in_schema=False)
def todo_page():
    return FileResponse(HERE / "todo_page.html")
