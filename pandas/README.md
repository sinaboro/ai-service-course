# pandas 기초

표(행과 열) 데이터를 분석하는 라이브러리. Series, DataFrame부터 필터, 그룹 집계, 합치기, 외부 CSV 파일(한글 엑셀·여러 파일·큰 파일·URL) 처리까지.

> 🧭 [저장소 처음으로](../README.md)

```bash
pip install pandas
```

## 📚 목차

| 장 | 주제 | 예제 폴더 | 교안 (Word) | 핵심 키워드 |
|:---:|---|---|---|---|
| 01 | pandas 시작과 Series | [01_시리즈](01_%EC%8B%9C%EB%A6%AC%EC%A6%88/) | [📘 교안](01_%EC%8B%9C%EB%A6%AC%EC%A6%88/01_%EC%8B%9C%EB%A6%AC%EC%A6%88_Series_%EA%B5%90%EC%95%88.docx) | `index` |
| 02 | DataFrame 만들기와 살펴보기 | [02_데이터프레임_만들기](02_%EB%8D%B0%EC%9D%B4%ED%84%B0%ED%94%84%EB%A0%88%EC%9E%84_%EB%A7%8C%EB%93%A4%EA%B8%B0/) | [📘 교안](02_%EB%8D%B0%EC%9D%B4%ED%84%B0%ED%94%84%EB%A0%88%EC%9E%84_%EB%A7%8C%EB%93%A4%EA%B8%B0/02_%EB%8D%B0%EC%9D%B4%ED%84%B0%ED%94%84%EB%A0%88%EC%9E%84_%EB%A7%8C%EB%93%A4%EA%B8%B0%EC%99%80_%EC%82%B4%ED%8E%B4%EB%B3%B4%EA%B8%B0_%EA%B5%90%EC%95%88.docx) | `head` `tail` `shape` `columns` `index` `dtypes` |
| 03 | 데이터 선택과 필터 | [03_데이터_선택과_필터](03_%EB%8D%B0%EC%9D%B4%ED%84%B0_%EC%84%A0%ED%83%9D%EA%B3%BC_%ED%95%84%ED%84%B0/) | [📘 교안](03_%EB%8D%B0%EC%9D%B4%ED%84%B0_%EC%84%A0%ED%83%9D%EA%B3%BC_%ED%95%84%ED%84%B0/03_%EB%8D%B0%EC%9D%B4%ED%84%B0_%EC%84%A0%ED%83%9D%EA%B3%BC_%ED%95%84%ED%84%B0_%EA%B5%90%EC%95%88.docx) | `loc` `iloc` |
| 04 | 데이터 수정 · 정렬 · 결측치 | [04_데이터_수정과_결측치](04_%EB%8D%B0%EC%9D%B4%ED%84%B0_%EC%88%98%EC%A0%95%EA%B3%BC_%EA%B2%B0%EC%B8%A1%EC%B9%98/) | [📘 교안](04_%EB%8D%B0%EC%9D%B4%ED%84%B0_%EC%88%98%EC%A0%95%EA%B3%BC_%EA%B2%B0%EC%B8%A1%EC%B9%98/04_%EB%8D%B0%EC%9D%B4%ED%84%B0_%EC%88%98%EC%A0%95%EA%B3%BC_%EA%B2%B0%EC%B8%A1%EC%B9%98_%EA%B5%90%EC%95%88.docx) | `sort_values` `apply` `map` `np.where` |
| 05 | 그룹과 집계 | [05_그룹과_집계](05_%EA%B7%B8%EB%A3%B9%EA%B3%BC_%EC%A7%91%EA%B3%84/) | [📘 교안](05_%EA%B7%B8%EB%A3%B9%EA%B3%BC_%EC%A7%91%EA%B3%84/05_%EA%B7%B8%EB%A3%B9%EA%B3%BC_%EC%A7%91%EA%B3%84_%EA%B5%90%EC%95%88.docx) | `groupby` `agg` |
| 06 | 데이터 합치기 — concat · merge | [06_데이터_합치기](06_%EB%8D%B0%EC%9D%B4%ED%84%B0_%ED%95%A9%EC%B9%98%EA%B8%B0/) | [📘 교안](06_%EB%8D%B0%EC%9D%B4%ED%84%B0_%ED%95%A9%EC%B9%98%EA%B8%B0/06_%EB%8D%B0%EC%9D%B4%ED%84%B0_%ED%95%A9%EC%B9%98%EA%B8%B0_%EA%B5%90%EC%95%88.docx) | `concat` `merge` `how="inner" / "left" / "right" / "outer"` |
| 07 | 파일 입출력과 실전 분석 | [07_파일입출력과_실전분석](07_%ED%8C%8C%EC%9D%BC%EC%9E%85%EC%B6%9C%EB%A0%A5%EA%B3%BC_%EC%8B%A4%EC%A0%84%EB%B6%84%EC%84%9D/) | [📘 교안](07_%ED%8C%8C%EC%9D%BC%EC%9E%85%EC%B6%9C%EB%A0%A5%EA%B3%BC_%EC%8B%A4%EC%A0%84%EB%B6%84%EC%84%9D/07_%ED%8C%8C%EC%9D%BC%EC%9E%85%EC%B6%9C%EB%A0%A5%EA%B3%BC_%EC%8B%A4%EC%A0%84%EB%B6%84%EC%84%9D_%EA%B5%90%EC%95%88.docx) | `read_csv` `to_csv` |
| 08 | 외부 CSV 파일 불러와 처리하기 | [08_외부CSV_불러와_처리하기](08_%EC%99%B8%EB%B6%80CSV_%EB%B6%88%EB%9F%AC%EC%99%80_%EC%B2%98%EB%A6%AC%ED%95%98%EA%B8%B0/) | [📘 교안](08_%EC%99%B8%EB%B6%80CSV_%EB%B6%88%EB%9F%AC%EC%99%80_%EC%B2%98%EB%A6%AC%ED%95%98%EA%B8%B0/08_%EC%99%B8%EB%B6%80CSV_%EB%B6%88%EB%9F%AC%EC%99%80_%EC%B2%98%EB%A6%AC%ED%95%98%EA%B8%B0_%EA%B5%90%EC%95%88.docx) | `pathlib` `encoding="cp949"` `sep` `comment` `skipfooter` |

## 📂 각 장 폴더 구성

```
01_시리즈/
├── NN_..._교안.docx     ← 학생용 Word 교안 (개념 설명 + 예제 해설 + 연습문제)
├── ex01_....py         ← 예제 코드 (교안에서 한 줄씩 설명)
├── ex02_....py
└── 연습문제_정답/
    ├── 문제1.py
    └── ...
```

## 📝 장별 학습 목표

### 01. pandas 시작과 Series

라벨이 붙은 1차원 데이터, Series를 만나 봅니다

- pandas가 무엇이고 NumPy와 어떻게 다른지 설명할 수 있어요.
- 리스트·딕셔너리로 Series를 만들 수 있어요.
- `index`(라벨)로 값을 꺼내고 바꿀 수 있어요.
- Series끼리 계산하고 조건으로 걸러낼 수 있어요.
- `sum`, `mean`, `sort_values`, `value_counts` 등을 쓸 수 있어요.

예제: `ex01_series_create.py`, `ex02_series_access.py`, `ex03_series_calc.py`, `ex04_series_methods.py`

### 02. DataFrame 만들기와 살펴보기

행과 열로 된 표, DataFrame을 만들고 데이터를 훑어봅니다

- 딕셔너리·리스트로 DataFrame을 만들 수 있어요.
- `head`, `tail`, `shape`, `info`, `describe`로 데이터를 훑어볼 수 있어요.
- `columns`, `index`, `dtypes`를 확인하고 바꿀 수 있어요.
- `set_index`, `reset_index`로 인덱스를 다룰 수 있어요.

예제: `ex01_df_create.py`, `ex02_df_explore.py`, `ex03_df_index.py`

### 03. 데이터 선택과 필터

원하는 열, 원하는 행, 조건에 맞는 데이터만 골라냅니다

- 열 하나(Series)와 여러 열(DataFrame)을 고를 수 있어요.
- `loc`(라벨)와 `iloc`(위치)로 행과 열을 고를 수 있어요.
- 조건식으로 원하는 행만 걸러낼 수 있어요.
- `&`, `|`, `isin`, `between`, `str.contains`로 복잡한 조건을 만들 수 있어요.

예제: `ex01_select_column.py`, `ex02_loc_iloc.py`, `ex03_filter.py`, `ex04_query_isin.py`

### 04. 데이터 수정 · 정렬 · 결측치

열을 추가·삭제하고, 정렬하고, 값을 바꾸고, 빈 값을 처리합니다

- 새 열을 계산해서 추가하고, 행·열을 삭제할 수 있어요.
- `sort_values`로 한 열·여러 열 기준 정렬을 할 수 있어요.
- `apply`, `map`, `np.where`로 값을 변환할 수 있어요.
- `isna`, `dropna`, `fillna`로 결측치(빈 값)를 처리할 수 있어요.

예제: `ex01_add_drop.py`, `ex02_sort.py`, `ex03_apply_map.py`, `ex04_missing.py`

### 05. 그룹과 집계

"부서별 평균", "매장별 매출"처럼 그룹으로 나눠 요약합니다

- `groupby`로 그룹별 합계·평균·개수를 구할 수 있어요.
- 여러 열로 그룹을 나눌 수 있어요.
- `agg`로 여러 통계를 한 번에 구할 수 있어요.
- `pivot_table`로 엑셀 피벗 테이블 같은 표를 만들 수 있어요.
- `value_counts`, `crosstab`으로 개수를 셀 수 있어요.

예제: `ex01_groupby.py`, `ex02_agg.py`, `ex03_pivot.py`, `ex04_value_counts_crosstab.py`

### 06. 데이터 합치기 — concat · merge

여러 표를 위아래로 이어 붙이고, 공통 열로 연결합니다

- `concat`으로 표를 위아래·좌우로 이어 붙일 수 있어요.
- `merge`로 공통 열(키)을 기준으로 두 표를 연결할 수 있어요.
- `how="inner" / "left" / "right" / "outer"`의 차이를 설명할 수 있어요.
- 합친 데이터를 groupby로 분석할 수 있어요.

예제: `ex01_concat.py`, `ex02_merge_inner.py`, `ex03_merge_how.py`, `ex04_merge_analysis.py`

### 07. 파일 입출력과 실전 분석

CSV 파일을 읽고, 정리하고, 분석하고, 결과를 저장합니다

- `read_csv`로 CSV 파일을 읽고 옵션을 쓸 수 있어요.
- `to_csv`로 결과를 저장할 수 있어요 (한글 엑셀 호환 포함).
- 읽은 데이터를 점검하고 결측치를 처리할 수 있어요.
- `to_datetime`과 `.dt`로 날짜를 다룰 수 있어요.
- 1 ~ 6장을 종합해 매출 보고서를 만들 수 있어요.

예제: `cafe_sales.csv`, `ex01_read_csv.py`, `ex02_clean.py`, `ex03_datetime.py`, `ex04_report.py`

### 08. 외부 CSV 파일 불러와 처리하기

엑셀·공공데이터·인터넷에서 받은 진짜 CSV 파일을 읽고, 정리하고, 분석합니다

- 실행 위치와 상관없이 CSV 파일 경로를 정확히 지정할 수 있어요 (`pathlib`).
- 한글이 깨지는 CSV를 `encoding="cp949"` 등으로 읽을 수 있어요.
- `sep`, `comment`, `skipfooter`, `thousands`, `na_values`, `usecols`, `dtype` 옵션을 상황에 맞게 쓸 수 있어요.
- 공백·단위·빈 값 표시가 섞인 **지저분한 CSV**를 깨끗하게 정리할 수 있어요.
- `2026.09.01` 같은 날짜 문자열을 날짜로 바꿔 월별·요일별로 분석할 수 있어요.
- 폴더 안의 **여러 CSV 파일**을 한 번에 읽어 합칠 수 있어요 (`glob`).
- 두 CSV를 `merge`로 연결하고, **큰 CSV**를 `chunksize`로 나눠 처리할 수 있어요.
- 인터넷 주소(URL)의 CSV를 읽고, 결과를 엑셀에서 열리는 CSV로 저장할 수 있어요.

예제: `data/students.csv`, `data/population.txt`, `data/survey_messy.csv`, `data/monthly/sales_2026-07.csv`, `data/monthly/sales_2026-08.csv`, `data/monthly/sales_2026-09.csv`, `data/products.csv`, `data/orders.csv`, `data/tips_backup.csv`, `ex00_make_data.py`, `ex01_read_basic.py`, `ex02_encoding.py`, `ex03_read_options.py`, `ex04_clean_messy.py`, `ex05_dates.py`, `ex06_multi_files.py`, `ex07_merge_files.py`, `ex08_big_file.py`, `ex09_read_url.py`, `ex10_project_report.py`

## ▶ 실행 방법

```bash
cd pandas/01_시리즈
python ex01_series_create.py
```

> 각 장 폴더로 이동(`cd`)한 뒤 실행하세요. 파일을 읽고 쓰는 예제는 실행한 폴더 또는 예제 파일 위치를 기준으로 동작해요.

➡ 다음 과정: [데이터 시각화 (matplotlib · seaborn)](../visualization/README.md)
