# FastAPI 모델 서빙

학습한 모델을 웹 API로 서비스하기. API 기초, Pydantic 검사, CRUD, 의존성·lifespan, 이미지 업로드·전처리, 모델 서빙(/predict), pytest 테스트와 Docker 배포까지.

> 🧭 [저장소 처음으로](../README.md)

```bash
pip install fastapi uvicorn python-multipart pillow httpx2 pytest
```

## 📚 목차

| 장 | 주제 | 예제 폴더 | 교안 (Word) | 핵심 키워드 |
|:---:|---|---|---|---|
| 01 | FastAPI 시작하기 | [01_FastAPI_시작하기](01_FastAPI_%EC%8B%9C%EC%9E%91%ED%95%98%EA%B8%B0/) | [📘 교안](01_FastAPI_%EC%8B%9C%EC%9E%91%ED%95%98%EA%B8%B0/01_FastAPI_%EC%8B%9C%EC%9E%91%ED%95%98%EA%B8%B0_%EA%B5%90%EC%95%88.docx) | `uvicorn` `/docs` |
| 02 | Pydantic 으로 요청과 응답 다루기 | [02_Pydantic_요청과_응답](02_Pydantic_%EC%9A%94%EC%B2%AD%EA%B3%BC_%EC%9D%91%EB%8B%B5/) | [📘 교안](02_Pydantic_%EC%9A%94%EC%B2%AD%EA%B3%BC_%EC%9D%91%EB%8B%B5/02_Pydantic_%EC%9A%94%EC%B2%AD%EA%B3%BC_%EC%9D%91%EB%8B%B5_%EA%B5%90%EC%95%88.docx) | `Field` `Literal` `Optional` |
| 03 | CRUD API 만들기 | [03_CRUD_API_만들기](03_CRUD_API_%EB%A7%8C%EB%93%A4%EA%B8%B0/) | [📘 교안](03_CRUD_API_%EB%A7%8C%EB%93%A4%EA%B8%B0/03_CRUD_API_%EB%A7%8C%EB%93%A4%EA%B8%B0_%EA%B5%90%EC%95%88.docx) | `HTTPException` |
| 04 | 의존성 · 비동기 · 수명주기 · 미들웨어 | [04_의존성_비동기_수명주기](04_%EC%9D%98%EC%A1%B4%EC%84%B1_%EB%B9%84%EB%8F%99%EA%B8%B0_%EC%88%98%EB%AA%85%EC%A3%BC%EA%B8%B0/) | [📘 교안](04_%EC%9D%98%EC%A1%B4%EC%84%B1_%EB%B9%84%EB%8F%99%EA%B8%B0_%EC%88%98%EB%AA%85%EC%A3%BC%EA%B8%B0/04_%EC%9D%98%EC%A1%B4%EC%84%B1_%EB%B9%84%EB%8F%99%EA%B8%B0_%EC%88%98%EB%AA%85%EC%A3%BC%EA%B8%B0_%EA%B5%90%EC%95%88.docx) | `Depends` `async def` `await` |
| 05 | 파일 업로드와 이미지 처리 | [05_파일업로드와_이미지](05_%ED%8C%8C%EC%9D%BC%EC%97%85%EB%A1%9C%EB%93%9C%EC%99%80_%EC%9D%B4%EB%AF%B8%EC%A7%80/) | [📘 교안](05_%ED%8C%8C%EC%9D%BC%EC%97%85%EB%A1%9C%EB%93%9C%EC%99%80_%EC%9D%B4%EB%AF%B8%EC%A7%80/05_%ED%8C%8C%EC%9D%BC%EC%97%85%EB%A1%9C%EB%93%9C%EC%99%80_%EC%9D%B4%EB%AF%B8%EC%A7%80_%EA%B5%90%EC%95%88.docx) | `UploadFile` |
| 06 | 머신러닝 모델 서빙 | [06_머신러닝_모델_서빙](06_%EB%A8%B8%EC%8B%A0%EB%9F%AC%EB%8B%9D_%EB%AA%A8%EB%8D%B8_%EC%84%9C%EB%B9%99/) | [📘 교안](06_%EB%A8%B8%EC%8B%A0%EB%9F%AC%EB%8B%9D_%EB%AA%A8%EB%8D%B8_%EC%84%9C%EB%B9%99/06_%EB%A8%B8%EC%8B%A0%EB%9F%AC%EB%8B%9D_%EB%AA%A8%EB%8D%B8_%EC%84%9C%EB%B9%99_%EA%B5%90%EC%95%88.docx) | `lifespan` `Depends` |
| 07 | 프로젝트 구조 · 테스트 · 배포 | [07_테스트와_배포](07_%ED%85%8C%EC%8A%A4%ED%8A%B8%EC%99%80_%EB%B0%B0%ED%8F%AC/) | [📘 교안](07_%ED%85%8C%EC%8A%A4%ED%8A%B8%EC%99%80_%EB%B0%B0%ED%8F%AC/07_%ED%85%8C%EC%8A%A4%ED%8A%B8%EC%99%80_%EB%B0%B0%ED%8F%AC_%EA%B5%90%EC%95%88.docx) |  |

## 📂 각 장 폴더 구성

```
01_FastAPI_시작하기/
├── NN_..._교안.docx     ← 학생용 Word 교안
├── ex01_hello.py       ← 앱 파일 (uvicorn ex01_hello:app 으로 서버 실행)
├── ex01_hello_client.py ← 앱에 실제로 요청을 보내 결과를 출력 (python 으로 실행)
└── 연습문제_정답/
```

## 📝 장별 학습 목표

### 01. FastAPI 시작하기

웹 API가 무엇인지 알고, 첫 API 서버를 만들어 실행해 봅니다

- API, HTTP 요청·응답, JSON이 무엇인지 설명할 수 있어요.
- FastAPI로 첫 API를 만들고 `uvicorn`으로 서버를 실행할 수 있어요.
- 브라우저와 자동 문서(`/docs`)로 API를 시험할 수 있어요.
- 경로 매개변수(`/items/{id}`)와 쿼리 매개변수(`?q=`)를 쓸 수 있어요.
- 타입 힌트로 값이 자동 변환·검사되는 것을 확인할 수 있어요.
- `TestClient`로 서버 없이 API를 호출해 볼 수 있어요.

예제: `ex01_hello.py`, `ex01_hello_client.py`, `ex02_path_query.py`, `ex02_path_query_client.py`

### 02. Pydantic 으로 요청과 응답 다루기

들어오는 데이터의 모양과 범위를 정하고, 자동으로 검사합니다

- POST 요청의 본문(body)을 Pydantic 모델로 받을 수 있어요.
- `Field`로 값의 범위·길이·예시를 정할 수 있어요.
- 리스트·중첩 모델·`Literal`·`Optional` 필드를 쓸 수 있어요.
- `response_model`로 응답 모양을 정하고 민감한 값을 숨길 수 있어요.
- `status_code`와 422 오류 응답의 구조를 이해해요.
- `field_validator`로 나만의 검사 규칙을 만들 수 있어요.

예제: `ex01_body.py`, `ex01_body_client.py`, `ex02_field.py`, `ex02_field_client.py`, `ex03_nested_response.py`, `ex03_nested_response_client.py`, `ex04_custom_validator.py`, `ex04_custom_validator_client.py`

### 03. CRUD API 만들기

만들기 · 읽기 · 수정 · 삭제를 갖춘 할 일(Todo) API와 라우터로 파일 나누기

- CRUD(Create · Read · Update · Delete)와 HTTP 메서드를 짝지을 수 있어요.
- `HTTPException`으로 404 같은 오류 응답을 보낼 수 있어요.
- PUT(전체 수정)과 PATCH(일부 수정)를 구분해 만들 수 있어요.
- 쿼리로 필터·페이지 나누기를 할 수 있어요.
- `APIRouter`로 API를 여러 파일로 나눌 수 있어요.
- `tags`, `summary`, `prefix`로 `/docs` 문서를 정리할 수 있어요.

예제: `ex01_todo_crud.py`, `ex01_todo_crud_client.py`, `routers/items.py`, `routers/models.py`, `ex02_main.py`, `ex02_main_client.py`

### 04. 의존성 · 비동기 · 수명주기 · 미들웨어

공통 기능을 재사용하고, 서버가 켜질 때 모델을 한 번만 불러오는 구조 만들기

- `Depends`로 공통 매개변수·검사 로직을 재사용할 수 있어요.
- 헤더의 API 키로 간단한 인증을 만들 수 있어요.
- `async def`와 `await`의 차이, 언제 쓰는지 알아요.
- `lifespan`으로 서버 시작 시 **모델을 한 번만** 불러오고 종료 시 정리할 수 있어요.
- 미들웨어로 모든 요청의 처리 시간을 기록할 수 있어요.
- 환경 변수로 설정을 바꿀 수 있고, CORS가 무엇인지 알아요.

예제: `ex01_depends.py`, `ex01_depends_client.py`, `ex02_api_key.py`, `ex02_api_key_client.py`, `ex03_async.py`, `ex03_async_client.py`, `ex04_lifespan.py`, `ex04_lifespan_client.py`, `ex05_middleware_settings.py`, `ex05_middleware_settings_client.py`

### 05. 파일 업로드와 이미지 처리

이미지를 받아 검사하고, 딥러닝 모델이 먹을 수 있는 배열로 바꿉니다

- `UploadFile`로 파일 하나·여러 개를 받을 수 있어요.
- 파일 종류(content type)와 크기를 검사하고 알맞은 오류를 돌려줄 수 있어요.
- Pillow로 업로드한 이미지의 크기·모드를 확인하고 바꿀 수 있어요.
- 처리한 이미지를 응답으로 돌려줄 수 있어요.
- 이미지를 **딥러닝 입력 배열**(크기 조정 → 정규화 → `(1, H, W, C)`)로 바꿀 수 있어요.
- TestClient로 파일 업로드 요청을 보낼 수 있어요.

예제: `ex00_make_samples.py`, `ex01_upload.py`, `ex01_upload_client.py`, `ex02_image.py`, `ex02_image_client.py`, `ex03_preprocess.py`, `ex03_preprocess_client.py`

### 06. 머신러닝 모델 서빙

학습한 모델을 저장하고, 서버 시작 때 불러와, /predict API로 예측을 제공합니다

- 모델 서빙의 전체 흐름(학습 → 저장 → 불러오기 → 예측 API)을 설명할 수 있어요.
- 학습한 모델의 가중치와 **전처리 정보**를 함께 저장할 수 있어요.
- `lifespan`에서 모델을 한 번만 불러오고, `Depends`로 꺼내 쓸 수 있어요.
- 입력·출력 스키마를 Pydantic으로 정의한 `/predict`, `/predict/batch`를 만들 수 있어요.
- `/health`, `/model/info`로 서버·모델 상태를 알려 줄 수 있어요.
- 모델이 없을 때 503을 돌려주는 등 실패 상황을 처리할 수 있어요.
- 이미지 분류 API를 만들고, PyTorch/Keras 모델로 바꿔 끼우는 방법을 알아요.

예제: `ex00_train_model.py`, `model_core.py`, `ex01_serving_app.py`, `ex01_serving_client.py`, `ex02_missing_model_client.py`, `ex03_image_app.py`, `ex03_image_client.py`

### 07. 프로젝트 구조 · 테스트 · 배포

실무형 폴더 구조로 정리하고, pytest로 자동 검사하고, 다른 컴퓨터에서도 실행되게 만듭니다

- 서빙 프로젝트를 설정·스키마·모델·라우터로 나눠 구성할 수 있어요.
- 환경 변수 기반 설정 객체를 만들 수 있어요.
- pytest + TestClient로 API 자동 테스트를 작성하고 실행할 수 있어요.
- `requirements.txt`로 필요한 패키지를 정리할 수 있어요.
- uvicorn 실행 옵션(포트, 호스트, 워커)을 알아요.
- Dockerfile이 무엇이고 어떻게 쓰는지 알아요.

예제: `serving_project/app/config.py`, `serving_project/app/schemas.py`, `serving_project/app/model.py`, `serving_project/app/deps.py`, `serving_project/app/routers/health.py`, `serving_project/app/routers/predict.py`, `serving_project/app/main.py`, `serving_project/train.py`, `serving_project/pytest.ini`, `serving_project/tests/test_api.py`, `serving_project/requirements.txt`, `serving_project/Dockerfile`, `serving_project/.dockerignore`, `ex01_run_tests.py`

## ▶ 실행 방법

```bash
cd fastapi/01_FastAPI_시작하기
uvicorn ex01_hello:app --reload      # 서버 실행 → http://127.0.0.1:8000/docs
python ex01_hello_client.py         # 서버 없이 요청 보내 보기 (TestClient)
```

> 각 장 폴더로 이동(`cd`)한 뒤 실행하세요. 파일을 읽고 쓰는 예제는 실행한 폴더 또는 예제 파일 위치를 기준으로 동작해요.
