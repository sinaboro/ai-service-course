# JavaScript (기초 문법 → DOM · 이벤트 → FastAPI 비동기 통신)

웹 페이지를 움직이는 언어. 변수 · 조건 · 반복 · 함수 · 객체와 JSON 같은 기초 문법부터, DOM 으로 화면 바꾸기, 이벤트, `async / await` 와 `fetch` 로 FastAPI 서버와 데이터 주고받기(GET · POST · PATCH · DELETE), 서버에 저장되는 할 일 앱 미니 프로젝트까지. 모든 예제는 실제 브라우저(Edge)에서 실행해 콘솔 출력과 화면을 교안에 실었어요.

> 🧭 [저장소 처음으로](../README.md)

> 📕 **[통합 교안 PDF (자기주도 학습용, 160쪽)](JavaScript_%ED%86%B5%ED%95%A9%EA%B5%90%EC%95%88.pdf)** — 1 ~ 10장 + 학습 안내(공부 순서 · 진도표) + 부록(쉬운 용어 사전 · 막힐 때 점검표)

## 📚 목차

| 장 | 주제 | 예제 폴더 | 교안 (Word) | 핵심 키워드 |
|:---:|---|---|---|---|
| 01 | JavaScript 시작하기 | [01_JS_시작하기](01_JS_%EC%8B%9C%EC%9E%91%ED%95%98%EA%B8%B0/) | [📘 교안](01_JS_%EC%8B%9C%EC%9E%91%ED%95%98%EA%B8%B0/01_JS_%EC%8B%9C%EC%9E%91%ED%95%98%EA%B8%B0_%EA%B5%90%EC%95%88.docx) | `console.log` `let` `const` 템플릿 문자열 |
| 02 | 비교와 조건문 | [02_조건문](02_%EC%A1%B0%EA%B1%B4%EB%AC%B8/) | [📘 교안](02_%EC%A1%B0%EA%B1%B4%EB%AC%B8/02_%EC%A1%B0%EA%B1%B4%EB%AC%B8_%EA%B5%90%EC%95%88.docx) | `===` `if` `&&` `||` |
| 03 | 배열과 반복문 | [03_반복문과_배열](03_%EB%B0%98%EB%B3%B5%EB%AC%B8%EA%B3%BC_%EB%B0%B0%EC%97%B4/) | [📘 교안](03_%EB%B0%98%EB%B3%B5%EB%AC%B8%EA%B3%BC_%EB%B0%B0%EC%97%B4/03_%EB%B0%98%EB%B3%B5%EB%AC%B8%EA%B3%BC_%EB%B0%B0%EC%97%B4_%EA%B5%90%EC%95%88.docx) | `[]` `push` `for...of` |
| 04 | 함수 | [04_함수](04_%ED%95%A8%EC%88%98/) | [📘 교안](04_%ED%95%A8%EC%88%98/04_%ED%95%A8%EC%88%98_%EA%B5%90%EC%95%88.docx) | `function` `=>` `map` `filter` |
| 05 | 객체와 JSON | [05_객체와_JSON](05_%EA%B0%9D%EC%B2%B4%EC%99%80_JSON/) | [📘 교안](05_%EA%B0%9D%EC%B2%B4%EC%99%80_JSON/05_%EA%B0%9D%EC%B2%B4%EC%99%80_JSON_%EA%B5%90%EC%95%88.docx) | `{}` `JSON.stringify` `JSON.parse` |
| 06 | DOM — JavaScript 로 화면 바꾸기 | [06_DOM_다루기](06_DOM_%EB%8B%A4%EB%A3%A8%EA%B8%B0/) | [📘 교안](06_DOM_%EB%8B%A4%EB%A3%A8%EA%B8%B0/06_DOM_%EB%8B%A4%EB%A3%A8%EA%B8%B0_%EA%B5%90%EC%95%88.docx) | `querySelector` `textContent` `classList` `createElement` |
| 07 | 이벤트 — 사용자 행동에 반응하기 | [07_이벤트](07_%EC%9D%B4%EB%B2%A4%ED%8A%B8/) | [📘 교안](07_%EC%9D%B4%EB%B2%A4%ED%8A%B8/07_%EC%9D%B4%EB%B2%A4%ED%8A%B8_%EA%B5%90%EC%95%88.docx) | `addEventListener` `preventDefault` |
| 08 | 비동기와 fetch | [08_비동기와_fetch](08_%EB%B9%84%EB%8F%99%EA%B8%B0%EC%99%80_fetch/) | [📘 교안](08_%EB%B9%84%EB%8F%99%EA%B8%B0%EC%99%80_fetch/08_%EB%B9%84%EB%8F%99%EA%B8%B0%EC%99%80_fetch_%EA%B5%90%EC%95%88.docx) | `async` `await` `fetch` `try/catch` |
| 09 | FastAPI 서버와 통신하기 | [09_FastAPI와_통신](09_FastAPI%EC%99%80_%ED%86%B5%EC%8B%A0/) | [📘 교안](09_FastAPI%EC%99%80_%ED%86%B5%EC%8B%A0/09_FastAPI%EC%99%80_%ED%86%B5%EC%8B%A0_%EA%B5%90%EC%95%88.docx) | `GET` `POST` `DELETE` CORS |
| 10 | 미니 프로젝트 — 할 일 앱 | [10_미니프로젝트_할일앱](10_%EB%AF%B8%EB%8B%88%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8_%ED%95%A0%EC%9D%BC%EC%95%B1/) | [📘 교안](10_%EB%AF%B8%EB%8B%88%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8_%ED%95%A0%EC%9D%BC%EC%95%B1/10_%EB%AF%B8%EB%8B%88%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8_%ED%95%A0%EC%9D%BC%EC%95%B1_%EA%B5%90%EC%95%88.docx) | `PATCH` CRUD 미니 프로젝트 |

## 📂 각 장 폴더 구성

```
01_JS_시작하기/
├── NN_..._교안.docx     ← 학생용 Word 교안 (코드 해설 + 실제 실행 결과 · 화면)
├── ex01_....html       ← 예제 페이지 (Live Server 로 열기)
├── ex01_....js         ← 예제 JavaScript (HTML 과 짝)
├── images/             ← 브라우저로 찍은 화면 (6 ~ 10장)
└── 연습문제_정답/
09_FastAPI와_통신/ · 10_미니프로젝트_할일앱/
├── main.py · app.py    ← FastAPI 서버 (uvicorn 으로 실행)
├── check_api.py        ← 서버 API 점검 (python check_api.py)
└── static/             ← 서버가 보내 주는 HTML · CSS · JS
```

## 📝 장별 학습 목표

### 01. JavaScript 시작하기

웹 페이지를 움직이는 언어 — 실행 방법 · 콘솔 · 변수 · 문자열 · 숫자

- JavaScript 가 웹 페이지에서 무슨 일을 하는지 설명할 수 있어요.
- HTML 에 JavaScript 를 넣는 두 가지 방법(script 태그 · 외부 파일)을 쓸 수 있어요.
- 개발자 도구의 Console 탭에서 실행 결과와 오류를 확인할 수 있어요.
- `let` 과 `const` 로 변수를 만들고, 자료형(문자열 · 숫자 · 불리언)을 구분할 수 있어요.
- 템플릿 문자열로 글자와 변수를 섞어 쓸 수 있어요.
- 문자열을 숫자로 바꿔 계산할 수 있어요.

예제: `ex01_hello.html`, `ex02_external.html`, `ex02_external.js`, `ex03_variables.html`, `ex03_variables.js`, `ex04_strings.html`, `ex04_strings.js`, `ex05_numbers.html`, `ex05_numbers.js`, `연습문제_정답/문제1.html`, `연습문제_정답/문제1.js`, `연습문제_정답/문제2.html`, `연습문제_정답/문제2.js`

### 02. 비교와 조건문

상황에 따라 다르게 움직이기 — 비교 연산자 · if · 논리 연산자 · 빈 값 검사

- 두 값을 비교해 true / false 를 얻을 수 있어요.
- 같은지 비교할 때 `===` 를 쓰는 이유를 설명할 수 있어요.
- `if` · `else if` · `else` 로 조건에 따라 다른 일을 할 수 있어요.
- `&&` · `||` · `!` 로 조건 여러 개를 합칠 수 있어요.
- 입력값이 비었는지 검사할 수 있어요 (폼 검사의 기초).

예제: `ex01_compare.html`, `ex01_compare.js`, `ex02_if.html`, `ex02_if.js`, `ex03_logic.html`, `ex03_logic.js`, `ex04_empty_check.html`, `ex04_empty_check.js`, `연습문제_정답/문제1.html`, `연습문제_정답/문제1.js`, `연습문제_정답/문제2.html`, `연습문제_정답/문제2.js`

### 03. 배열과 반복문

여러 값을 한 줄로 담고, 하나씩 꺼내 같은 일 반복하기

- 배열을 만들고 번호(인덱스)로 값을 꺼낼 수 있어요.
- `push` · `pop` 으로 값을 넣고 뺄 수 있어요.
- `for` 와 `for...of` 로 같은 일을 반복할 수 있어요.
- `includes` · `indexOf` · `join` · `slice` 를 쓸 수 있어요.
- 반복문으로 합계 · 평균 · 최댓값을 구할 수 있어요.

예제: `ex01_array.html`, `ex01_array.js`, `ex02_for.html`, `ex02_for.js`, `ex03_array_methods.html`, `ex03_array_methods.js`, `ex04_score_stats.html`, `ex04_score_stats.js`, `연습문제_정답/문제1.html`, `연습문제_정답/문제1.js`, `연습문제_정답/문제2.html`, `연습문제_정답/문제2.js`

### 04. 함수

자주 하는 일에 이름 붙여 두기 — 함수 · 화살표 함수 · 범위 · 콜백

- `function` 으로 함수를 만들고, 매개변수와 `return` 을 쓸 수 있어요.
- 화살표 함수 `() => {}` 를 읽고 쓸 수 있어요.
- 변수가 어디서부터 어디까지 쓰이는지(범위)를 설명할 수 있어요.
- 함수를 다른 함수에 넘기는 **콜백**의 뜻을 알아요.
- `forEach` · `map` · `filter` · `find` 로 배열을 다룰 수 있어요.

예제: `ex01_function.html`, `ex01_function.js`, `ex02_arrow.html`, `ex02_arrow.js`, `ex03_scope.html`, `ex03_scope.js`, `ex04_callback.html`, `ex04_callback.js`, `연습문제_정답/문제1.html`, `연습문제_정답/문제1.js`, `연습문제_정답/문제2.html`, `연습문제_정답/문제2.js`

### 05. 객체와 JSON

이름표 붙은 데이터 묶음 — 객체 · 객체 배열 · 서버와 주고받는 JSON

- 객체를 만들고 점(.)으로 값을 꺼내고 바꿀 수 있어요.
- 객체 여러 개를 배열에 담아 다룰 수 있어요 (서버 데이터의 기본 모양).
- `filter` · `find` · `map` 으로 객체 배열에서 원하는 것을 고를 수 있어요.
- `JSON.stringify` 와 `JSON.parse` 로 객체 ↔ JSON 글자를 바꿀 수 있어요.
- JSON 이 서버와 브라우저 사이의 "공통 언어" 라는 것을 알아요.

예제: `ex01_object.html`, `ex01_object.js`, `ex02_object_array.html`, `ex02_object_array.js`, `ex03_json.html`, `ex03_json.js`, `연습문제_정답/문제1.html`, `연습문제_정답/문제1.js`, `연습문제_정답/문제2.html`, `연습문제_정답/문제2.js`

### 06. DOM — JavaScript 로 화면 바꾸기

태그 찾기 · 글자 바꾸기 · class 로 모양 바꾸기 · 태그 새로 만들기

- DOM 이 "JavaScript 가 보는 HTML" 이라는 것을 설명할 수 있어요.
- `querySelector` · `querySelectorAll` 로 태그를 찾을 수 있어요.
- `textContent` 로 글자를 읽고 바꿀 수 있어요.
- `classList` 로 class 를 붙이고 떼어 모양을 바꿀 수 있어요.
- `createElement` · `append` 로 배열 데이터를 화면 목록 · 카드로 그릴 수 있어요.

예제: `ex01_select.html`, `ex01_select.js`, `ex02_class.html`, `ex02_class.js`, `ex03_create.html`, `ex03_create.js`, `ex04_cards.html`, `ex04_cards.js`, `style.css`, `연습문제_정답/문제1.html`, `연습문제_정답/문제1.js`

### 07. 이벤트 — 사용자 행동에 반응하기

클릭 · 입력 · 폼 제출에 반응하고, 데이터 → 화면 흐름으로 할 일 목록 만들기

- 이벤트가 무엇인지, `addEventListener` 로 어떻게 연결하는지 설명할 수 있어요.
- 클릭(click) · 입력(input) · 제출(submit) 이벤트를 다룰 수 있어요.
- 입력칸의 값을 `.value` 로 읽을 수 있어요.
- `event.preventDefault()` 로 폼 제출 때 페이지가 바뀌는 것을 막을 수 있어요.
- "데이터 바꾸기 → render() 로 다시 그리기" 흐름으로 할 일 목록을 만들 수 있어요.

예제: `ex01_click.html`, `ex01_click.js`, `ex02_input.html`, `ex02_input.js`, `ex03_form.html`, `ex03_form.js`, `ex04_todo.html`, `ex04_todo.js`, `style.css`, `연습문제_정답/문제1.html`, `연습문제_정답/문제1.js`, `연습문제_정답/문제2.html`, `연습문제_정답/문제2.js`

### 08. 비동기와 fetch

기다리는 일을 맡겨 두기 — setTimeout · async / await · fetch · 로딩과 오류 처리

- 동기와 비동기의 차이를 생활 속 예로 설명할 수 있어요.
- `setTimeout` 의 실행 순서를 예측할 수 있어요.
- `async` 함수 안에서 `await` 로 결과를 기다릴 수 있어요.
- `fetch` 로 JSON 파일을 가져와 화면에 그릴 수 있어요.
- `try / catch` 와 `response.ok` 로 실패를 처리하고, 로딩 문구를 보여 줄 수 있어요.

예제: `data/members.json`, `data/quotes.json`, `ex01_timeout.html`, `ex01_timeout.js`, `ex02_await.html`, `ex02_await.js`, `ex03_fetch_json.html`, `ex03_fetch_json.js`, `ex04_loading_error.html`, `ex04_loading_error.js`, `style.css`, `연습문제_정답/문제1.html`, `연습문제_정답/문제1.js`

### 09. FastAPI 서버와 통신하기

fetch 로 GET · POST · DELETE 요청 보내기 — 방명록 만들기

- 브라우저(JavaScript)와 서버(FastAPI)가 주고받는 흐름을 그림으로 설명할 수 있어요.
- FastAPI 서버를 켜고, 서버가 보내 준 페이지를 열 수 있어요.
- `fetch` 로 GET 요청을 보내 JSON 을 받아 화면에 그릴 수 있어요.
- `fetch` 의 옵션(method · headers · body)으로 JSON 을 POST 할 수 있어요.
- 주소에 번호를 넣어 DELETE 요청을 보낼 수 있어요.
- 상태 코드(201 · 404 · 422)와 서버가 꺼진 경우를 화면에 알맞게 보여 줄 수 있어요.

예제: `check_api.py`, `main.py`, `static/ex01_get.html`, `static/ex01_get.js`, `static/ex02_post.html`, `static/ex02_post.js`, `static/ex03_guestbook.html`, `static/ex03_guestbook.js`, `static/index.html`, `static/style.css`, `static/연습문제_정답/문제1.html`, `static/연습문제_정답/문제1.js`, `static/연습문제_정답/문제2.html`, `static/연습문제_정답/문제2.js`

### 10. 미니 프로젝트 — 할 일 앱

1 ~ 9장을 모아 서버에 저장되는 할 일 앱 완성하기 (GET · POST · PATCH · DELETE)

- 할 일 앱의 화면 · 서버 · 데이터 흐름을 설명할 수 있어요.
- 서버 API 4개(목록 · 추가 · 고치기 · 삭제)를 표로 정리하고 시험할 수 있어요.
- 반복되는 fetch 코드를 `request()` 함수로 묶어 쓸 수 있어요.
- PATCH 로 데이터의 일부(완료 여부)만 바꿀 수 있어요.
- 기능을 하나씩 더하며 앱을 확장할 수 있어요.

예제: `app.py`, `check_api.py`, `static/css/style.css`, `static/index.html`, `static/js/app.js`, `연습문제_정답/문제1_app.js`, `연습문제_정답/문제2_app.js`

## ▶ 실행 방법

1 ~ 8장은 VS Code 의 **Live Server** 로 `.html` 파일을 열고, **F12 → Console** 탭에서 결과를 확인해요. (8장 fetch 예제는 파일을 더블클릭하면 동작하지 않아요.) 9 ~ 10장은 FastAPI 서버가 필요해요.

```bash
pip install fastapi uvicorn
cd javascript/09_FastAPI와_통신
uvicorn main:app --reload      # → http://127.0.0.1:8000
cd ../10_미니프로젝트_할일앱
uvicorn app:app --reload       # → http://127.0.0.1:8000
```

> 서버는 한 번에 하나만 켜요(둘 다 8000 번 포트). 다른 장으로 갈 때는 터미널에서 Ctrl + C 로 끄고 켜세요.

⬅ 이전 과정: [HTML · CSS](../html_css/README.md) · ➡ 다음 과정: [FastAPI 웹 서비스](../fastapi/README.md)
