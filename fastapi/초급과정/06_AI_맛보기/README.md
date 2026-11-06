# 06. AI 맛보기

학습해 둔 AI 모델을 `predict()` 함수 하나로 불러 예측 웹 서비스를 만들어요. (넘파이 없이 동작해요)

> 🧭 [초급 과정 처음으로](../README.md) · 교안: [FastAPI_초급교안.pdf](../../FastAPI_%EC%B4%88%EA%B8%89%EA%B5%90%EC%95%88.pdf)

| 파일 | 실행 (이 폴더에서) | 내용 |
|---|---|---|
| `ai_model.py` | (직접 실행하지 않아요) | `from ai_model import predict` 로 쓰는 AI 함수 |
| `ex01_try_model.py` | `python ex01_try_model.py` | AI 함수를 서버 없이 불러 보기 |
| `ex02_predict_app.py + predict_page.html` | `uvicorn ex02_predict_app:app --reload` | 예측 API + 예측 화면 |
| `연습문제_정답/문제1.py` | (장 폴더에서) uvicorn 연습문제_정답.문제1:app --reload | 공부 시간별 확률표 `/table` |

연습문제 정답은 `연습문제_정답` 폴더에 있어요.
