# 01. 첫 API 만들기

주소(창구)를 여러 개 만들고, 경로 · 쿼리로 값을 받아요. 결과는 브라우저와 `/docs` 로 확인해요.

> 🧭 [초급 과정 처음으로](../README.md) · 교안: [FastAPI_초급교안.pdf](../../FastAPI_%EC%B4%88%EA%B8%89%EA%B5%90%EC%95%88.pdf)

| 파일 | 실행 (이 폴더에서) | 내용 |
|---|---|---|
| `ex01_hello.py` | `uvicorn ex01_hello:app --reload` | 주소 여러 개: `/`, `/hello`, `/about` |
| `ex02_path.py` | `uvicorn ex02_path:app --reload` | 경로 매개변수: `/menu/3`, `/square/7` |
| `ex03_query.py` | `uvicorn ex03_query:app --reload` | 쿼리 매개변수: `/add?a=3&b=5`, `/greet?name=철수` |
| `ex04_testclient.py` | `python ex04_testclient.py` | (선택, 한 번만) 코드로 요청 보내기 — `pip install httpx2` 필요 |

연습문제 정답은 `연습문제_정답` 폴더에 있어요.
