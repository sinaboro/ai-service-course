# FastAPI 초급 과정

웹을 처음 배우는 학생을 위한 과정이에요. 작은 예제를 하나씩 쌓아 올려 마지막에 **나만의 웹 서비스**를 만들어 발표해요.
교안: 📕 [FastAPI_초급교안.pdf](../FastAPI_%EC%B4%88%EA%B8%89%EA%B5%90%EC%95%88.pdf)

> 🧭 [FastAPI 처음으로](../README.md) · 다 마쳤다면 [심화 과정](../%EC%8B%AC%ED%99%94%EA%B3%BC%EC%A0%95/README.md)으로

## 준비

```bash
python -m venv .venv
.venv\Scripts\activate             # Windows (macOS · Linux: source .venv/bin/activate)
pip install fastapi uvicorn
python 00_웹과_API_첫걸음/check_setup.py
```

## 장별 예제

| 장 | 폴더 | 서버로 실행 (그 폴더에서) | 확인 |
|:---:|---|---|---|
| 00 | [00_웹과_API_첫걸음](00_%EC%9B%B9%EA%B3%BC_API_%EC%B2%AB%EA%B1%B8%EC%9D%8C/) | `uvicorn ex03_first_server:app --reload` | 브라우저 `/`, `/time` |
| 01 | [01_첫_API_만들기](01_%EC%B2%AB_API_%EB%A7%8C%EB%93%A4%EA%B8%B0/) | `uvicorn ex01_hello:app --reload` (ex02_path, ex03_query 도) | 브라우저, `/docs` |
| 02 | [02_데이터_보내기](02_%EB%8D%B0%EC%9D%B4%ED%84%B0_%EB%B3%B4%EB%82%B4%EA%B8%B0/) | `uvicorn ex01_post:app --reload` (ex02_field, ex03_coffee 도) | `/docs` Try it out |
| 03 | [03_메모장_API](03_%EB%A9%94%EB%AA%A8%EC%9E%A5_API/) | `uvicorn ex01_memo:app --reload` | `/docs` |
| 04 | [04_웹페이지와_API](04_%EC%9B%B9%ED%8E%98%EC%9D%B4%EC%A7%80%EC%99%80_API/) | `uvicorn ex01_html:app --reload` → ex02_fetch → ex03_post | 브라우저 `/` |
| 05 | [05_메모장_웹앱](05_%EB%A9%94%EB%AA%A8%EC%9E%A5_%EC%9B%B9%EC%95%B1/) | `uvicorn memo_app:app --reload` | 브라우저 `/` |
| 06 | [06_AI_맛보기](06_AI_%EB%A7%9B%EB%B3%B4%EA%B8%B0/) | `python ex01_try_model.py` → `uvicorn ex02_predict_app:app --reload` | 브라우저 `/` |
| 07 | [07_미니_프로젝트](07_%EB%AF%B8%EB%8B%88_%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8/) | `cd guestbook` → `uvicorn main:app --reload` | 브라우저 `/`, 친구 폰 |

- 연습문제 정답은 각 장의 `연습문제_정답` 폴더에 있어요.
- 서버는 반드시 **그 예제가 있는 폴더에서** 켜요. 다른 폴더에서 켜면 `Could not import module` 오류가 나요.
- 서버 끄기는 `Ctrl + C`.
