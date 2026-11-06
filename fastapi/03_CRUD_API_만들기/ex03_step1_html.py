# 6-1단계: 서버가 JSON 대신 HTML(웹 페이지)을 돌려주기 (서버로 실행)
# 실행: 이 폴더에서  uvicorn ex03_step1_html:app --reload
# 확인: 브라우저에서 아래 세 주소를 차례로 열어 보고, 보이는 모양이 어떻게 다른지 비교해요
#   http://127.0.0.1:8000/api/hello   → JSON (데이터)
#   http://127.0.0.1:8000/inline      → 코드 안에 쓴 HTML (화면)
#   http://127.0.0.1:8000             → HTML 파일 step1_page.html (화면)
from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse, HTMLResponse

app = FastAPI()
HERE = Path(__file__).parent                   # 이 파일이 있는 폴더 (HTML 파일을 찾을 때 기준)


# ① 지금까지 만든 것과 같은 API: 딕셔너리 → JSON
@app.get("/api/hello")
def hello():
    return {"message": "안녕하세요, 저는 JSON 이에요"}


# ② HTML 을 글자로 직접 돌려주기
# response_class=HTMLResponse: "이 글자는 JSON 이 아니라 HTML 이에요" 라고 브라우저에 알려 줘요
# (이 표시가 없으면 브라우저는 태그를 그림으로 그리지 않고 글자 그대로 보여 줘요)
@app.get("/inline", response_class=HTMLResponse)
def inline_page():
    return "<h1>코드 안에 쓴 HTML</h1><p>태그가 <b>화면</b>으로 바뀌어 보여요.</p>"


# ③ HTML 파일을 통째로 돌려주기 — 화면이 길어지면 이 방법이 편해요
# include_in_schema=False: 화면용 주소라서 /docs API 문서에는 보이지 않게
@app.get("/", include_in_schema=False)
def page():
    return FileResponse(HERE / "step1_page.html")
