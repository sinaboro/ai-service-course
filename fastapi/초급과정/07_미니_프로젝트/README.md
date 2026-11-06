# 07. 미니 프로젝트

배운 것을 조립해 나만의 웹 서비스를 만들고, 친구 폰에서 접속해 발표해요.

> 🧭 [초급 과정 처음으로](../README.md) · 교안: [FastAPI_초급교안.pdf](../../FastAPI_%EC%B4%88%EA%B8%89%EA%B5%90%EC%95%88.pdf)

| 파일 | 실행 (이 폴더에서) | 내용 |
|---|---|---|
| `guestbook/main.py + index.html` | `cd guestbook → uvicorn main:app --reload` | 방명록 예시 — 글을 posts.json 에 저장 |
| `(친구 폰 접속)` | `uvicorn main:app --host 0.0.0.0` | 같은 와이파이의 휴대폰에서 http://내컴퓨터IP:8000 |
| `my_project/` | `cd my_project → uvicorn main:app --reload` | 내 프로젝트 뼈대 + 기획서.md |
