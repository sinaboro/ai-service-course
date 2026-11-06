# 04. 웹 페이지와 API

HTML 화면에서 버튼으로 API 를 부르고, 동기 · 비동기를 체험해요. 1 → 2 → 3단계 순서로 해요.

> 🧭 [초급 과정 처음으로](../README.md) · 교안: [FastAPI_초급교안.pdf](../../FastAPI_%EC%B4%88%EA%B8%89%EA%B5%90%EC%95%88.pdf)

| 파일 | 실행 (이 폴더에서) | 내용 |
|---|---|---|
| `ex01_html.py + page1.html` | `uvicorn ex01_html:app --reload` | 1단계: JSON 대신 HTML 돌려주기 |
| `ex02_fetch.py + page2.html` | `uvicorn ex02_fetch:app --reload` | 2단계: 버튼 → fetch, 동기 vs 비동기 체험 |
| `ex03_post.py + page3.html` | `uvicorn ex03_post:app --reload` | 3단계: 입력 칸 → POST, 422 표시 |
