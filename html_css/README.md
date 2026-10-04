# HTML · CSS (시맨틱 화면 구도)

AI 서비스 화면을 직접 만들기. HTML 기초 · 폼, ⭐ 시맨틱 태그로 화면 구도 잡기(4개 장: 이해 · 기본 패턴 · 실전 페이지 5종 · Grid areas), CSS 박스 모델 · Flexbox · Grid, 종합 프로젝트 페이지, FastAPI 서버와 연결까지. 모든 예제 W3C 검사 통과, 브라우저 렌더링 화면 포함.

> 🧭 [저장소 처음으로](../README.md)

## 📚 목차

| 장 | 주제 | 예제 폴더 | 교안 (Word) | 핵심 키워드 |
|:---:|---|---|---|---|
| 01 | HTML 시작하기 | [01_HTML_시작하기](01_HTML_%EC%8B%9C%EC%9E%91%ED%95%98%EA%B8%B0/) | [📘 교안](01_HTML_%EC%8B%9C%EC%9E%91%ED%95%98%EA%B8%B0/01_HTML_%EC%8B%9C%EC%9E%91%ED%95%98%EA%B8%B0_%EA%B5%90%EC%95%88.docx) | `<!DOCTYPE>` `<html>` `<head>` |
| 02 | 목록 · 표 · 폼 | [02_목록_표_폼](02_%EB%AA%A9%EB%A1%9D_%ED%91%9C_%ED%8F%BC/) | [📘 교안](02_%EB%AA%A9%EB%A1%9D_%ED%91%9C_%ED%8F%BC/02_%EB%AA%A9%EB%A1%9D_%ED%91%9C_%ED%8F%BC_%EA%B5%90%EC%95%88.docx) | `ul` `ol` `dl` `table` `caption` `thead` `form` `label` `input` |
| 03 | 시맨틱 태그 이해하기 | [03_시맨틱_태그_이해](03_%EC%8B%9C%EB%A7%A8%ED%8B%B1_%ED%83%9C%EA%B7%B8_%EC%9D%B4%ED%95%B4/) | [📘 교안](03_%EC%8B%9C%EB%A7%A8%ED%8B%B1_%ED%83%9C%EA%B7%B8_%EC%9D%B4%ED%95%B4/03_%EC%8B%9C%EB%A7%A8%ED%8B%B1_%ED%83%9C%EA%B7%B8_%EC%9D%B4%ED%95%B4_%EA%B5%90%EC%95%88.docx) | `header` `nav` `main` `section` `article` `div` |
| 04 | 시맨틱 태그로 화면 구도 잡기 ① — 기본 패턴 | [04_시맨틱_화면구도_기본패턴](04_%EC%8B%9C%EB%A7%A8%ED%8B%B1_%ED%99%94%EB%A9%B4%EA%B5%AC%EB%8F%84_%EA%B8%B0%EB%B3%B8%ED%8C%A8%ED%84%B4/) | [📘 교안](04_%EC%8B%9C%EB%A7%A8%ED%8B%B1_%ED%99%94%EB%A9%B4%EA%B5%AC%EB%8F%84_%EA%B8%B0%EB%B3%B8%ED%8C%A8%ED%84%B4/04_%EC%8B%9C%EB%A7%A8%ED%8B%B1_%ED%99%94%EB%A9%B4%EA%B5%AC%EB%8F%84_%EA%B8%B0%EB%B3%B8%ED%8C%A8%ED%84%B4_%EA%B5%90%EC%95%88.docx) |  |
| 05 | 시맨틱 태그로 화면 구도 잡기 ② — 실전 페이지 5종 | [05_시맨틱_화면구도_실전페이지](05_%EC%8B%9C%EB%A7%A8%ED%8B%B1_%ED%99%94%EB%A9%B4%EA%B5%AC%EB%8F%84_%EC%8B%A4%EC%A0%84%ED%8E%98%EC%9D%B4%EC%A7%80/) | [📘 교안](05_%EC%8B%9C%EB%A7%A8%ED%8B%B1_%ED%99%94%EB%A9%B4%EA%B5%AC%EB%8F%84_%EC%8B%A4%EC%A0%84%ED%8E%98%EC%9D%B4%EC%A7%80/05_%EC%8B%9C%EB%A7%A8%ED%8B%B1_%ED%99%94%EB%A9%B4%EA%B5%AC%EB%8F%84_%EC%8B%A4%EC%A0%84%ED%8E%98%EC%9D%B4%EC%A7%80_%EA%B5%90%EC%95%88.docx) | `aria-label` `aria-labelledby` |
| 06 | CSS 기초와 박스 모델 | [06_CSS기초_박스모델](06_CSS%EA%B8%B0%EC%B4%88_%EB%B0%95%EC%8A%A4%EB%AA%A8%EB%8D%B8/) | [📘 교안](06_CSS%EA%B8%B0%EC%B4%88_%EB%B0%95%EC%8A%A4%EB%AA%A8%EB%8D%B8/06_CSS%EA%B8%B0%EC%B4%88_%EB%B0%95%EC%8A%A4%EB%AA%A8%EB%8D%B8_%EA%B5%90%EC%95%88.docx) |  |
| 07 | Flexbox — 한 줄로 늘어놓고 정렬하기 | [07_Flexbox](07_Flexbox/) | [📘 교안](07_Flexbox/07_Flexbox_%EA%B5%90%EC%95%88.docx) | `flex-direction` `justify-content` `align-items` `gap` `flex-wrap` `flex: 1` |
| 08 | CSS Grid — 시맨틱 태그로 화면 구도 완성하기 | [08_Grid_시맨틱레이아웃](08_Grid_%EC%8B%9C%EB%A7%A8%ED%8B%B1%EB%A0%88%EC%9D%B4%EC%95%84%EC%9B%83/) | [📘 교안](08_Grid_%EC%8B%9C%EB%A7%A8%ED%8B%B1%EB%A0%88%EC%9D%B4%EC%95%84%EC%9B%83/08_Grid_%EC%8B%9C%EB%A7%A8%ED%8B%B1%EB%A0%88%EC%9D%B4%EC%95%84%EC%9B%83_%EA%B5%90%EC%95%88.docx) | `fr` `repeat()` `span` |
| 09 | 종합 프로젝트 — AI 탐지 서비스 페이지 만들기 | [09_종합프로젝트](09_%EC%A2%85%ED%95%A9%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8/) | [📘 교안](09_%EC%A2%85%ED%95%A9%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8/09_%EC%A2%85%ED%95%A9%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8_%EA%B5%90%EC%95%88.docx) |  |
| 10 | HTML · CSS 페이지를 FastAPI 서버와 연결하기 | [10_FastAPI연결](10_FastAPI%EC%97%B0%EA%B2%B0/) | [📘 교안](10_FastAPI%EC%97%B0%EA%B2%B0/10_FastAPI%EC%97%B0%EA%B2%B0_%EA%B5%90%EC%95%88.docx) | `fetch` |

## 📂 각 장 폴더 구성

```
01_HTML_시작하기/
├── NN_..._교안.docx     ← 학생용 Word 교안 (코드 해설 + 브라우저 화면)
├── ex01_....html       ← 예제 페이지 (더블클릭해서 브라우저로 열기)
├── regions.css         ← 시맨틱 영역에 색 · 태그 이름표를 붙여 "구도"를 보여 주는 CSS (3 ~ 5 · 8 · 9장)
├── outline.py          ← 시맨틱 구조를 트리로 보여 주는 도구 (python outline.py)
├── images/             ← 브라우저로 찍은 화면
└── 연습문제_정답/
```

## 📝 장별 학습 목표

### 01. HTML 시작하기

웹 페이지의 뼈대를 만드는 언어 — 문서 구조와 기본 태그

- 웹 페이지가 HTML · CSS · JavaScript로 나뉘어 만들어진다는 것을 알아요.
- HTML 문서의 기본 구조(`<!DOCTYPE>`, `<html>`, `<head>`, `<body>`)를 쓸 수 있어요.
- 요소 · 태그 · 속성의 뜻을 구분할 수 있어요.
- 제목(`h1`~`h6`), 문단(`p`), 강조, 링크(`a`), 이미지(`img`)를 쓸 수 있어요.
- 브라우저 개발자 도구(F12)로 HTML을 살펴볼 수 있어요.

예제: `images/logo.svg`, `ex01_first_page.html`, `ex02_text.html`, `ex03_link_image.html`, `ex04_comment_devtools.html`, `연습문제_정답/문제1.html`, `연습문제_정답/문제2.html`

### 02. 목록 · 표 · 폼

정보를 정리해 보여 주고(목록·표), 사용자에게 입력을 받는(폼) 방법

- 순서 없는 목록(`ul`), 순서 있는 목록(`ol`), 설명 목록(`dl`)을 쓸 수 있어요.
- `table`, `caption`, `thead`, `tbody`, `th scope`로 접근성 있는 표를 만들 수 있어요.
- `form`, `label`, `input`의 여러 type, `select`, `textarea`, `button`을 쓸 수 있어요.
- `fieldset`, `legend`, `required`, `placeholder`로 친절한 폼을 만들 수 있어요.
- **이미지 업로드 폼**(`enctype="multipart/form-data"`, `accept`)을 만들 수 있어요.

예제: `ex01_lists.html`, `ex02_table.html`, `ex03_form_basic.html`, `ex04_inputs.html`, `ex05_upload_form.html`, `연습문제_정답/문제1.html`, `연습문제_정답/문제2.html`

### 03. 시맨틱 태그 이해하기

"여기는 머리글, 여기는 본문" — 의미를 담은 태그로 화면을 나누는 이유와 규칙

- 시맨틱(semantic) 태그가 무엇이고 왜 쓰는지 설명할 수 있어요.
- `header`, `nav`, `main`, `section`, `article`, `aside`, `footer`의 뜻과 쓰임을 구분할 수 있어요.
- `section`과 `article`, `div`를 언제 쓰는지 판단할 수 있어요.
- `figure`, `figcaption`, `time`, `address`, `blockquote`, `details` 같은 의미 태그를 쓸 수 있어요.
- 랜드마크와 제목 구조로 **접근성** 좋은 페이지를 만들 수 있어요.
- `outline.py`로 내 페이지의 구조를 트리로 확인할 수 있어요.

예제: `ex00_layout_map.html`, `ex01_div_soup.html`, `ex02_semantic.html`, `ex03_article_section.html`, `ex04_text_semantics.html`, `images/detect_example.svg`, `ex05_landmarks_a11y.html`, `outline.py`, `연습문제_정답/문제1.html`

### 04. 시맨틱 태그로 화면 구도 잡기 ① — 기본 패턴

와이어프레임을 그리고, 시맨틱 태그로 영역을 나누는 6가지 대표 구도

- 화면을 만들기 전에 **와이어프레임**(뼈대 그림)을 그리고 영역을 나눌 수 있어요.
- 와이어프레임을 시맨틱 태그로 옮기는 6단계 순서를 따라 할 수 있어요.
- 1단 · 2단(사이드바) · 3단 · 랜딩 · 카드 그리드 · 중첩 구도를 마크업할 수 있어요.
- 각 영역에 알맞은 제목(h1 ~ h3)을 붙여 문서 구조를 완성할 수 있어요.
- `regions.css`와 `outline.py`로 내가 만든 구도를 눈과 트리로 점검할 수 있어요.

예제: `regions.css`, `ex01_one_column.html`, `ex02_sidebar.html`, `ex03_holy_grail.html`, `ex04_landing.html`, `ex05_card_grid.html`, `ex06_nested_regions.html`, `images/result.svg`, `outline.py`, `연습문제_정답/문제1.html`, `연습문제_정답/regions.css`

### 05. 시맨틱 태그로 화면 구도 잡기 ② — 실전 페이지 5종

블로그 · 뉴스 · 쇼핑몰 · 대시보드 · AI 탐지 서비스를 시맨틱 태그로 설계하기

- 실제 서비스 화면을 보고 시맨틱 영역으로 나눌 수 있어요 ("구도 읽기").
- 블로그 글·뉴스·상품 상세·대시보드·AI 서비스 페이지의 구조 차이를 설명할 수 있어요.
- `aria-label`, `aria-labelledby`로 여러 nav·aside·section에 이름을 붙일 수 있어요.
- 같은 HTML에 CSS만 바꿔 "디자인 화면"과 "구도 화면"을 비교할 수 있어요.
- 팀 프로젝트의 AI 서비스 페이지 구조를 설계할 수 있어요.

예제: `site.css`, `regions.css`, `xray.css`, `images/curve.svg`, `images/camera.svg`, `images/detect.svg`, `outline.py`, `ex01_blog_post.html`, `구도보기/ex01_blog_post.html`, `ex02_news_main.html`, `구도보기/ex02_news_main.html`, `ex03_shop_product.html`, `구도보기/ex03_shop_product.html`, `ex04_dashboard.html`, `구도보기/ex04_dashboard.html`, `ex05_ai_service.html`, `구도보기/ex05_ai_service.html`

### 06. CSS 기초와 박스 모델

선택자 · 우선순위 · 색과 글꼴 · 단위 · 박스 모델 · display

- CSS를 HTML에 연결하는 세 가지 방법을 알고, 외부 파일 방식을 쓸 수 있어요.
- 태그 · class · id · 자손 · 가상 클래스 선택자를 구분해 쓸 수 있어요.
- 여러 규칙이 겹칠 때 어느 것이 이기는지(우선순위) 설명할 수 있어요.
- 박스 모델(content · padding · border · margin)과 `box-sizing`을 이해해요.
- block · inline · inline-block · none 의 차이를 알아요.
- 시맨틱 태그 자체를 선택자로 써서 페이지를 꾸밀 수 있어요.

예제: `style.css`, `ex01_three_ways.html`, `ex02_selectors.html`, `ex03_cascade.html`, `ex04_color_font_unit.html`, `ex05_box_model.html`, `ex06_display.html`, `ex07_style_semantic.html`, `연습문제_정답/문제1.html`

### 07. Flexbox — 한 줄로 늘어놓고 정렬하기

메뉴 바 · 카드 줄 · 2단 구도를 flex 로 만들기

- flex 컨테이너와 아이템의 관계를 이해해요.
- `flex-direction`, `justify-content`, `align-items`로 방향과 정렬을 바꿀 수 있어요.
- `gap`, `flex-wrap`, `flex: 1`로 간격과 크기를 나눌 수 있어요.
- flex로 header 메뉴 바, 카드 줄, 바닥에 붙는 footer를 만들 수 있어요.
- flex로 시맨틱 2단 구도(main + aside)를 배치할 수 있어요.

예제: `ex01_flex_basics.html`, `ex02_justify_align.html`, `ex03_gap_wrap_grow.html`, `ex04_nav_bar.html`, `ex05_card_row.html`, `ex06_sticky_footer.html`, `ex07_semantic_flex.html`, `연습문제_정답/문제1.html`

### 08. CSS Grid — 시맨틱 태그로 화면 구도 완성하기

grid-template-areas 로 header · nav · main · aside · footer 를 그림처럼 배치하기

- grid 컨테이너에 열(column)과 행(row)을 만들 수 있어요.
- `fr`, `repeat()`로 같은 너비 · 비율로 나눈 칸을 만들 수 있어요.
- 아이템이 여러 칸을 차지하게(`span`) 할 수 있어요.
- ⭐ `grid-template-areas`로 시맨틱 영역 이름을 **그림처럼** 배치할 수 있어요.
- 같은 HTML에 CSS만 바꿔 여러 화면 구도를 만들 수 있어요.

예제: `regions.css`, `ex01_grid_basics.html`, `ex02_span.html`, `ex03_gallery.html`, `images/thumb.svg`, `ex04_areas_holy_grail.html`, `ex05_areas_dashboard.html`, `ex06_areas_ai_service.html`, `ex07a_layout.html`, `ex07b_layout.html`, `ex07c_layout.html`, `연습문제_정답/regions.css`, `연습문제_정답/문제1.html`

### 09. 종합 프로젝트 — AI 탐지 서비스 페이지 만들기

와이어프레임 → 시맨틱 구조(HTML) → 꾸미기(CSS) → 점검, 1 ~ 8장을 모두 모아 한 페이지 완성하기

- 완성 화면을 보고 와이어프레임과 영역(시맨틱 태그)을 정할 수 있어요.
- HTML 파일과 CSS 파일을 폴더로 나눠 프로젝트를 만들 수 있어요.
- 시맨틱 태그로 머리글 · 히어로 · 작업 영역 · 카드 · 바닥글 구조를 짤 수 있어요.
- 6 ~ 8장의 CSS(박스 모델 · flex · grid-template-areas)를 한 페이지에 함께 쓸 수 있어요.
- 완성한 페이지를 점검 목록으로 확인할 수 있어요.

예제: `project/index.html`, `project/css/style.css`, `project/css/regions.css`, `project/structure.html`, `project/images/sample_result.svg`, `연습문제_정답/문제1.html`

### 10. HTML · CSS 페이지를 FastAPI 서버와 연결하기

정적 파일 서빙 · fetch 로 사진 보내기 · 결과로 화면 바꾸기

- FastAPI로 HTML · CSS · JS 파일을 서비스(StaticFiles)할 수 있어요.
- 폼 제출을 JavaScript `fetch`로 바꿔 페이지 이동 없이 결과를 받을 수 있어요.
- 서버가 돌려준 JSON으로 이미지 · 표 · 안내 문구를 바꿀 수 있어요.
- 오류(잘못된 파일, 서버 꺼짐)를 화면에 친절하게 보여 줄 수 있어요.
- 탐지기 부분만 바꾸면 YOLO 모델과 연결된다는 구조를 이해해요.

예제: `make_sample.py`, `detector.py`, `app.py`, `static/index.html`, `static/css/style.css`, `static/js/app.js`, `static/images/sample_result.svg`, `check_api.py`

## ▶ 실행 방법

예제 `.html` 파일을 더블클릭하면 브라우저에서 열려요. 10장은 서버가 필요해요.

```bash
cd html_css/10_FastAPI연결
python make_sample.py
uvicorn app:app --reload      # → http://127.0.0.1:8000
```

> 각 장 폴더로 이동(`cd`)한 뒤 실행하세요. 파일을 읽고 쓰는 예제는 실행한 폴더 또는 예제 파일 위치를 기준으로 동작해요.

➡ 다음 과정: [FastAPI 모델 서빙](../fastapi/README.md)
