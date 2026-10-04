# 데이터 시각화 (matplotlib · seaborn)

데이터를 그래프로. matplotlib 기초와 꾸미기, pandas 연동, seaborn 통계 그래프, 탐색적 데이터 분석(EDA) 보고서까지. 모든 교안에 실행 결과 그래프 이미지 포함.

> 🧭 [저장소 처음으로](../README.md)

```bash
pip install matplotlib seaborn
```

## 📚 목차

| 장 | 주제 | 예제 폴더 | 교안 (Word) | 핵심 키워드 |
|:---:|---|---|---|---|
| 01 | matplotlib 시작하기 — 선 그래프 | [01_matplotlib_시작하기](01_matplotlib_%EC%8B%9C%EC%9E%91%ED%95%98%EA%B8%B0/) | [📘 교안](01_matplotlib_%EC%8B%9C%EC%9E%91%ED%95%98%EA%B8%B0/01_matplotlib_%EC%8B%9C%EC%9E%91%ED%95%98%EA%B8%B0_%EA%B5%90%EC%95%88.docx) | `plt.plot()` |
| 02 | 여러 가지 그래프 | [02_여러가지_그래프](02_%EC%97%AC%EB%9F%AC%EA%B0%80%EC%A7%80_%EA%B7%B8%EB%9E%98%ED%94%84/) | [📘 교안](02_%EC%97%AC%EB%9F%AC%EA%B0%80%EC%A7%80_%EA%B7%B8%EB%9E%98%ED%94%84/02_%EC%97%AC%EB%9F%AC%EA%B0%80%EC%A7%80_%EA%B7%B8%EB%9E%98%ED%94%84_%EA%B5%90%EC%95%88.docx) |  |
| 03 | 여러 그래프 나눠 그리기와 꾸미기 | [03_여러그래프와_꾸미기](03_%EC%97%AC%EB%9F%AC%EA%B7%B8%EB%9E%98%ED%94%84%EC%99%80_%EA%BE%B8%EB%AF%B8%EA%B8%B0/) | [📘 교안](03_%EC%97%AC%EB%9F%AC%EA%B7%B8%EB%9E%98%ED%94%84%EC%99%80_%EA%BE%B8%EB%AF%B8%EA%B8%B0/03_%EC%97%AC%EB%9F%AC%EA%B7%B8%EB%9E%98%ED%94%84%EC%99%80_%EA%BE%B8%EB%AF%B8%EA%B8%B0_%EA%B5%90%EC%95%88.docx) | `plt.subplots(행, 열)` `sharex` `sharey` `tight_layout` `plt.style.use` |
| 04 | pandas 와 함께 시각화 | [04_pandas와_시각화](04_pandas%EC%99%80_%EC%8B%9C%EA%B0%81%ED%99%94/) | [📘 교안](04_pandas%EC%99%80_%EC%8B%9C%EA%B0%81%ED%99%94/04_pandas%EC%99%80_%EC%8B%9C%EA%B0%81%ED%99%94_%EA%B5%90%EC%95%88.docx) | `df.plot()` `df.plot.bar()` |
| 05 | seaborn 기초 | [05_seaborn_기초](05_seaborn_%EA%B8%B0%EC%B4%88/) | [📘 교안](05_seaborn_%EA%B8%B0%EC%B4%88/05_seaborn_%EA%B8%B0%EC%B4%88_%EA%B5%90%EC%95%88.docx) | `sns.set_theme()` `data=` `x=` `y=` |
| 06 | seaborn 심화와 실전 분석 | [06_seaborn_심화와_실전](06_seaborn_%EC%8B%AC%ED%99%94%EC%99%80_%EC%8B%A4%EC%A0%84/) | [📘 교안](06_seaborn_%EC%8B%AC%ED%99%94%EC%99%80_%EC%8B%A4%EC%A0%84/06_seaborn_%EC%8B%AC%ED%99%94%EC%99%80_%EC%8B%A4%EC%A0%84_%EA%B5%90%EC%95%88.docx) | `heatmap` `regplot` `lmplot` `pairplot` `jointplot` |

## 📂 각 장 폴더 구성

```
01_matplotlib_시작하기/
├── NN_..._교안.docx     ← 학생용 Word 교안 (실행 결과 그래프 포함)
├── ex01_....py         ← 예제 코드 (실행하면 images/ 에 그래프 저장)
├── images/             ← 예제가 만든 그래프 이미지 (정답 비교용)
├── data/               ← 실습 데이터 (해당 장만)
└── 연습문제_정답/
```

## 📝 장별 학습 목표

### 01. matplotlib 시작하기 — 선 그래프

숫자 데이터를 그림으로 바꾸는 첫걸음, 그리고 한글 폰트 설정

- 데이터 시각화가 왜 필요한지 설명할 수 있어요.
- `plt.plot()`으로 선 그래프를 그리고 제목·축 이름·범례를 붙일 수 있어요.
- **한글 폰트**를 설정해 한글이 깨지지 않게 할 수 있어요.
- 선 색·모양·점 표시를 바꿀 수 있어요.
- `savefig()`로 그래프를 이미지 파일로 저장할 수 있어요.
- `plt.` 방식과 `fig, ax` 방식의 차이를 알아요.

예제: `ex01_first_plot.py`, `ex02_korean_font.py`, `ex03_title_label_legend.py`, `ex04_line_style.py`, `ex05_axis_range_text.py`, `ex06_two_styles.py`

### 02. 여러 가지 그래프

막대 · 히스토그램 · 산점도 · 원 · 상자 그래프 — 데이터에 맞는 그래프 고르기

- 막대 그래프(세로·가로·묶음·누적)를 그릴 수 있어요.
- 히스토그램으로 데이터의 분포를 볼 수 있어요.
- 산점도로 두 값의 관계를 볼 수 있어요.
- 원 그래프로 비율을 나타낼 수 있어요.
- 상자 그래프로 중앙값·이상치를 볼 수 있어요.
- 데이터의 성격에 맞는 그래프를 고를 수 있어요.

예제: `ex01_bar.py`, `ex02_grouped_stacked.py`, `ex03_hist.py`, `ex04_scatter.py`, `ex05_pie.py`, `ex06_box.py`, `ex07_choose_chart.py`

### 03. 여러 그래프 나눠 그리기와 꾸미기

subplots로 한 그림에 여러 그래프를, 스타일과 색으로 보기 좋게

- `plt.subplots(행, 열)`로 여러 그래프를 나눠 그릴 수 있어요.
- `sharex`, `sharey`, `tight_layout`, `suptitle`을 쓸 수 있어요.
- 스타일(`plt.style.use`)과 색 지도(colormap)를 바꿀 수 있어요.
- 축 눈금 형식(천 단위 콤마, %)과 테두리를 다듬을 수 있어요.
- 왼쪽·오른쪽 두 개의 y축(`twinx`)을 쓸 수 있어요.
- 여러 그래프를 모아 한 장짜리 대시보드를 만들 수 있어요.

예제: `ex01_subplots.py`, `ex02_share_loop.py`, `ex03_style_color.py`, `ex04_ticks_spines.py`, `ex05_twinx.py`, `ex06_dashboard.py`

### 04. pandas 와 함께 시각화

DataFrame을 바로 그래프로 — groupby·pivot 결과를 한 줄로 시각화

- `df.plot()`, `df.plot.bar()` 등으로 DataFrame을 바로 그래프로 그릴 수 있어요.
- groupby·pivot_table 결과를 시각화할 수 있어요.
- 날짜(시계열) 데이터를 선 그래프로 그리고 이동평균을 겹칠 수 있어요.
- `kind="hist"`, `"box"`, `"scatter"`, `"area"`, `"pie"`를 쓸 수 있어요.
- pandas 그래프와 matplotlib 꾸미기를 함께 쓸 수 있어요.

예제: `data/store_sales.csv`, `ex01_df_plot.py`, `ex02_group_pivot.py`, `ex03_timeseries.py`, `ex04_kinds.py`, `ex05_pandas_plus_mpl.py`, `ex06_report.py`

### 05. seaborn 기초

짧은 코드로 보기 좋은 통계 그래프 — 분포 · 범주 · 관계

- seaborn이 matplotlib과 어떻게 다른지 설명할 수 있어요.
- `sns.set_theme()`과 한글 글꼴을 함께 설정할 수 있어요.
- `data=`, `x=`, `y=`, `hue=` 로 DataFrame 열을 바로 그래프에 쓸 수 있어요.
- 분포 그래프(`histplot`, `kdeplot`, `boxplot`, `violinplot`)를 그릴 수 있어요.
- 범주 그래프(`countplot`, `barplot`)와 관계 그래프(`scatterplot`, `lineplot`)를 그릴 수 있어요.
- seaborn 그래프를 matplotlib `ax`로 꾸미고 저장할 수 있어요.

예제: `data/tips.csv`, `ex01_first_seaborn.py`, `ex02_hist_kde.py`, `ex03_box_violin.py`, `ex04_count_bar.py`, `ex05_scatter_hue_size.py`, `ex06_palette.py`, `ex07_lineplot.py`

### 06. seaborn 심화와 실전 분석

히트맵 · 회귀선 · 여러 칸 그래프, 그리고 탐색적 데이터 분석(EDA) 보고서

- `heatmap`으로 상관관계와 피벗 표를 색으로 보여 줄 수 있어요.
- `regplot`, `lmplot`으로 회귀선(추세선)을 그릴 수 있어요.
- `pairplot`, `jointplot`으로 여러 변수의 관계를 한 번에 볼 수 있어요.
- `catplot`, `relplot`, `FacetGrid`로 그룹별로 칸을 나눠 그릴 수 있어요.
- 여러 그래프를 모아 **탐색적 데이터 분석(EDA) 보고서**를 만들 수 있어요.

예제: `data/tips.csv`, `ex01_heatmap_corr.py`, `ex02_regplot.py`, `ex03_pair_joint.py`, `ex04_catplot_relplot.py`, `ex05_facetgrid.py`, `ex06_make_students.py`, `ex07_eda_report.py`

## ▶ 실행 방법

```bash
cd visualization/01_matplotlib_시작하기
python ex01_first_plot.py
```

> 각 장 폴더로 이동(`cd`)한 뒤 실행하세요. 파일을 읽고 쓰는 예제는 실행한 폴더 또는 예제 파일 위치를 기준으로 동작해요.

➡ 다음 과정: [AI 딥러닝 (Keras · OpenCV · YOLO)](../ai_deep_learning/README.md)
