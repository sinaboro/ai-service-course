# 00. 웹과 API 첫걸음

웹이 움직이는 원리(요청 · 응답)를 알고, 실습 환경을 준비해 첫 서버를 켜 봅니다.
교안은 [통합 교안 PDF](../FastAPI_%ED%86%B5%ED%95%A9%EA%B5%90%EC%95%88.pdf) 의 **0장**이에요.

> 🧭 [FastAPI 과정 처음으로](../README.md)

## 예제 파일

| 파일 | 실행 방법 | 내용 |
|---|---|---|
| `ex01_json_basics.py` | `python ex01_json_basics.py` | JSON 글자 ↔ 파이썬 딕셔너리 |
| `ex02_python_warmup.py` | `python ex02_python_warmup.py` | 타입 힌트 · 기본값 · `str \| None` · 데코레이터 · import 미리보기 |
| `check_setup.py` | `python check_setup.py` | 파이썬 버전 · 가상환경 · 패키지 · 8000번 포트 점검 |
| `ex03_first_server.py` | `uvicorn ex03_first_server:app --reload` | 첫 서버 → 브라우저로 `http://127.0.0.1:8000` 접속 |
| `ex03_first_server_client.py` | `python ex03_first_server_client.py` | 같은 요청을 코드(TestClient)로 보내 보기 |
| `연습문제_정답/` | `python 연습문제_정답/문제1.py` | 연습문제 1 · 2 정답 |

## 준비 (처음 한 번)

```bash
python -m venv .venv
.venv\Scripts\activate          # Windows (macOS · Linux: source .venv/bin/activate)
pip install fastapi uvicorn python-multipart pillow numpy httpx2 pytest
python check_setup.py
```
