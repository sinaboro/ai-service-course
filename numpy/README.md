# NumPy 기초

숫자 데이터를 빠르게 계산하는 배열 라이브러리. 배열 만들기부터 인덱싱, 브로드캐스팅, 통계, 난수까지.

> 🧭 [저장소 처음으로](../README.md)

## 📚 목차

| 장 | 주제 | 예제 폴더 | 교안 (Word) | 핵심 키워드 |
|:---:|---|---|---|---|
| 01 | NumPy 시작과 배열 만들기 | [01_넘파이_시작과_배열만들기](01_%EB%84%98%ED%8C%8C%EC%9D%B4_%EC%8B%9C%EC%9E%91%EA%B3%BC_%EB%B0%B0%EC%97%B4%EB%A7%8C%EB%93%A4%EA%B8%B0/) | [📘 교안](01_%EB%84%98%ED%8C%8C%EC%9D%B4_%EC%8B%9C%EC%9E%91%EA%B3%BC_%EB%B0%B0%EC%97%B4%EB%A7%8C%EB%93%A4%EA%B8%B0/01_%EB%84%98%ED%8C%8C%EC%9D%B4_%EC%8B%9C%EC%9E%91%EA%B3%BC_%EB%B0%B0%EC%97%B4%EB%A7%8C%EB%93%A4%EA%B8%B0_%EA%B5%90%EC%95%88.docx) | `np.array()` `arange` `zeros` `ones` |
| 02 | 인덱싱과 슬라이싱 | [02_인덱싱과_슬라이싱](02_%EC%9D%B8%EB%8D%B1%EC%8B%B1%EA%B3%BC_%EC%8A%AC%EB%9D%BC%EC%9D%B4%EC%8B%B1/) | [📘 교안](02_%EC%9D%B8%EB%8D%B1%EC%8B%B1%EA%B3%BC_%EC%8A%AC%EB%9D%BC%EC%9D%B4%EC%8B%B1/02_%EC%9D%B8%EB%8D%B1%EC%8B%B1%EA%B3%BC_%EC%8A%AC%EB%9D%BC%EC%9D%B4%EC%8B%B1_%EA%B5%90%EC%95%88.docx) | `m[행, 열]` |
| 03 | 배열 연산과 브로드캐스팅 | [03_배열연산과_브로드캐스팅](03_%EB%B0%B0%EC%97%B4%EC%97%B0%EC%82%B0%EA%B3%BC_%EB%B8%8C%EB%A1%9C%EB%93%9C%EC%BA%90%EC%8A%A4%ED%8C%85/) | [📘 교안](03_%EB%B0%B0%EC%97%B4%EC%97%B0%EC%82%B0%EA%B3%BC_%EB%B8%8C%EB%A1%9C%EB%93%9C%EC%BA%90%EC%8A%A4%ED%8C%85/03_%EB%B0%B0%EC%97%B4%EC%97%B0%EC%82%B0%EA%B3%BC_%EB%B8%8C%EB%A1%9C%EB%93%9C%EC%BA%90%EC%8A%A4%ED%8C%85_%EA%B5%90%EC%95%88.docx) | `np.sqrt` `np.round` `np.abs` |
| 04 | 배열 형태 바꾸기 · 합치기 · 나누기 | [04_배열_형태_바꾸기](04_%EB%B0%B0%EC%97%B4_%ED%98%95%ED%83%9C_%EB%B0%94%EA%BE%B8%EA%B8%B0/) | [📘 교안](04_%EB%B0%B0%EC%97%B4_%ED%98%95%ED%83%9C_%EB%B0%94%EA%BE%B8%EA%B8%B0/04_%EB%B0%B0%EC%97%B4_%ED%98%95%ED%83%9C_%EB%B0%94%EA%BE%B8%EA%B8%B0_%EA%B5%90%EC%95%88.docx) | `reshape()` `-1` `flatten()` `ravel()` `.T` |
| 05 | 통계와 집계 | [05_통계와_집계](05_%ED%86%B5%EA%B3%84%EC%99%80_%EC%A7%91%EA%B3%84/) | [📘 교안](05_%ED%86%B5%EA%B3%84%EC%99%80_%EC%A7%91%EA%B3%84/05_%ED%86%B5%EA%B3%84%EC%99%80_%EC%A7%91%EA%B3%84_%EA%B5%90%EC%95%88.docx) | `sum` `mean` `max` `axis=0` `axis=1` `argmax` `argmin` |
| 06 | 난수와 실전 예제 | [06_난수와_실전예제](06_%EB%82%9C%EC%88%98%EC%99%80_%EC%8B%A4%EC%A0%84%EC%98%88%EC%A0%9C/) | [📘 교안](06_%EB%82%9C%EC%88%98%EC%99%80_%EC%8B%A4%EC%A0%84%EC%98%88%EC%A0%9C/06_%EB%82%9C%EC%88%98%EC%99%80_%EC%8B%A4%EC%A0%84%EC%98%88%EC%A0%9C_%EA%B5%90%EC%95%88.docx) | `np.random.default_rng(seed)` `integers` `random` `normal` |

## 📂 각 장 폴더 구성

```
01_넘파이_시작과_배열만들기/
├── NN_..._교안.docx     ← 학생용 Word 교안 (개념 설명 + 예제 해설 + 연습문제)
├── ex01_....py         ← 예제 코드 (교안에서 한 줄씩 설명)
├── ex02_....py
└── 연습문제_정답/
    ├── 문제1.py
    └── ...
```

## 📝 장별 학습 목표

### 01. NumPy 시작과 배열 만들기

파이썬 리스트보다 빠르고 편한 숫자 배열, ndarray를 만나 봅니다

- NumPy가 무엇이고 왜 쓰는지 설명할 수 있어요.
- `np.array()`로 리스트를 배열로 바꿀 수 있어요.
- `arange`, `zeros`, `ones`, `full`, `linspace`, `eye`로 배열을 만들 수 있어요.
- `shape`, `ndim`, `size`, `dtype`으로 배열 정보를 확인할 수 있어요.
- `astype()`으로 자료형을 바꿀 수 있어요.

예제: `ex01_why_numpy.py`, `ex02_array_create.py`, `ex03_array_attr.py`, `ex04_dtype.py`

### 02. 인덱싱과 슬라이싱

배열에서 원하는 값, 원하는 행과 열, 조건에 맞는 값만 꺼냅니다

- 1차원 배열을 인덱싱·슬라이싱할 수 있어요.
- 2차원 배열에서 `m[행, 열]`로 값·행·열을 꺼낼 수 있어요.
- **불리언 인덱싱**으로 조건에 맞는 값만 골라낼 수 있어요.
- 팬시 인덱싱으로 여러 위치를 한 번에 꺼낼 수 있어요.
- 슬라이싱은 원본을 공유한다는 것(뷰)과 `copy()`를 알아요.

예제: `ex01_index_1d.py`, `ex02_index_2d.py`, `ex03_boolean.py`, `ex04_fancy_copy.py`

### 03. 배열 연산과 브로드캐스팅

반복문 없이 배열 전체를 한 번에 계산합니다

- 같은 모양 배열끼리 원소별 연산을 할 수 있어요.
- **브로드캐스팅** 규칙으로 모양이 다른 배열을 계산할 수 있어요.
- `np.sqrt`, `np.round`, `np.abs` 같은 유니버설 함수를 쓸 수 있어요.
- 원소별 곱(`*`)과 행렬 곱(`@`)을 구분할 수 있어요.

예제: `ex01_elementwise.py`, `ex02_broadcasting.py`, `ex03_ufunc.py`, `ex04_matrix.py`

### 04. 배열 형태 바꾸기 · 합치기 · 나누기

같은 데이터를 다른 모양으로 바꾸고, 여러 배열을 붙이고 나눕니다

- `reshape()`로 배열의 모양을 바꿀 수 있어요 (`-1` 사용 포함).
- `flatten()`, `ravel()`로 1차원으로 펼칠 수 있어요.
- `.T`로 행과 열을 바꿀 수 있어요.
- `concatenate`, `vstack`, `hstack`으로 배열을 합칠 수 있어요.
- `split`으로 배열을 나눌 수 있어요.

예제: `ex01_reshape.py`, `ex02_transpose_flatten.py`, `ex03_concat_stack.py`, `ex04_split.py`

### 05. 통계와 집계

합계·평균·최댓값을 구하고, 행별·열별로 요약합니다

- `sum`, `mean`, `max`, `min`, `std`, `median`으로 통계를 구할 수 있어요.
- `axis=0`, `axis=1`로 열별·행별 통계를 구할 수 있어요.
- `argmax`, `argmin`으로 가장 큰/작은 값의 위치를 찾을 수 있어요.
- `sort`, `argsort`로 정렬할 수 있어요.
- `unique`, `cumsum`을 쓸 수 있어요.

예제: `ex01_basic_stats.py`, `ex02_axis.py`, `ex03_arg_sort.py`, `ex04_unique_cumsum.py`

### 06. 난수와 실전 예제

무작위 데이터를 만들고, 지금까지 배운 것으로 성적을 분석합니다

- `np.random.default_rng(seed)`로 재현 가능한 난수를 만들 수 있어요.
- `integers`, `random`, `normal`, `choice`, `shuffle`을 쓸 수 있어요.
- 주사위·로또 시뮬레이션을 만들 수 있어요.
- 1 ~ 5장의 내용을 종합해 성적 데이터를 분석할 수 있어요.
- `np.savetxt`, `np.loadtxt`로 배열을 파일에 저장하고 읽을 수 있어요.

예제: `ex01_random.py`, `ex02_lotto_dice.py`, `ex03_score_analysis.py`, `ex04_save_load.py`

## ▶ 실행 방법

```bash
cd numpy/01_넘파이_시작과_배열만들기
python ex01_why_numpy.py
```

> 각 장 폴더로 이동(`cd`)한 뒤 실행하세요. 파일을 읽고 쓰는 예제는 실행한 폴더를 기준으로 동작해요.

➡ 다음 과정: [pandas](../pandas/README.md)
