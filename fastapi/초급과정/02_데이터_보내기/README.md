# 02. 데이터 보내기 — POST

본문(JSON)에 값을 담아 보내고, Pydantic 이 검사하게 해요. POST 는 `/docs` 의 Try it out 으로 시험해요.

> 🧭 [초급 과정 처음으로](../README.md) · 교안: [FastAPI_초급교안.pdf](../../FastAPI_%EC%B4%88%EA%B8%89%EA%B5%90%EC%95%88.pdf)

| 파일 | 실행 (이 폴더에서) | 내용 |
|---|---|---|
| `ex01_post.py` | `uvicorn ex01_post:app --reload` | 회원 가입 `POST /join` |
| `ex02_field.py` | `uvicorn ex02_field:app --reload` | `Field` 로 범위 · 글자 수 규칙 → 422 |
| `ex03_coffee.py` | `uvicorn ex03_coffee:app --reload` | 커피 주문 — 받은 값으로 가격 계산 |

연습문제 정답은 `연습문제_정답` 폴더에 있어요.
