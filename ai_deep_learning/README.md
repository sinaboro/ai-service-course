# AI 딥러닝 (Keras · OpenCV · YOLO)

AI 개념부터 객체 탐지 프로젝트까지. 머신러닝 기초(scikit-learn), Keras 딥러닝 · CNN · 전이 학습, OpenCV 영상 처리, 객체 탐지 개념(IoU · NMS · mAP), 윈도우 labelImg 레이블링과 YOLO 데이터셋, YOLO 학습 · 추론, FastAPI + HTML/CSS 서빙과 팀 프로젝트 가이드까지.

> 🧭 [저장소 처음으로](../README.md)

```bash
pip install scikit-learn tensorflow opencv-python ultralytics
```

## 📚 목차

| 장 | 주제 | 예제 폴더 | 교안 (Word) | 핵심 키워드 |
|:---:|---|---|---|---|
| 01 | AI 기술 개요 — 인공지능 · 머신러닝 · 딥러닝 · 객체 탐지 | [01_AI개요](01_AI%EA%B0%9C%EC%9A%94/) | [📘 교안](01_AI%EA%B0%9C%EC%9A%94/01_AI%EA%B0%9C%EC%9A%94_%EA%B5%90%EC%95%88.docx) |  |
| 02 | 머신러닝 기초 — 학습 · 평가 · 과대적합 | [02_머신러닝기초](02_%EB%A8%B8%EC%8B%A0%EB%9F%AC%EB%8B%9D%EA%B8%B0%EC%B4%88/) | [📘 교안](02_%EB%A8%B8%EC%8B%A0%EB%9F%AC%EB%8B%9D%EA%B8%B0%EC%B4%88/02_%EB%A8%B8%EC%8B%A0%EB%9F%AC%EB%8B%9D%EA%B8%B0%EC%B4%88_%EA%B5%90%EC%95%88.docx) | `fit → predict → score` |
| 03 | Keras 로 배우는 딥러닝 기초 | [03_Keras딥러닝기초](03_Keras%EB%94%A5%EB%9F%AC%EB%8B%9D%EA%B8%B0%EC%B4%88/) | [📘 교안](03_Keras%EB%94%A5%EB%9F%AC%EB%8B%9D%EA%B8%B0%EC%B4%88/03_Keras%EB%94%A5%EB%9F%AC%EB%8B%9D%EA%B8%B0%EC%B4%88_%EA%B5%90%EC%95%88.docx) | `Sequential` `compile` `fit` |
| 04 | CNN — 이미지를 보는 신경망 | [04_CNN이미지분류](04_CNN%EC%9D%B4%EB%AF%B8%EC%A7%80%EB%B6%84%EB%A5%98/) | [📘 교안](04_CNN%EC%9D%B4%EB%AF%B8%EC%A7%80%EB%B6%84%EB%A5%98/04_CNN%EC%9D%B4%EB%AF%B8%EC%A7%80%EB%B6%84%EB%A5%98_%EA%B5%90%EC%95%88.docx) |  |
| 05 | OpenCV 로 영상 다루기 | [05_OpenCV영상처리](05_OpenCV%EC%98%81%EC%83%81%EC%B2%98%EB%A6%AC/) | [📘 교안](05_OpenCV%EC%98%81%EC%83%81%EC%B2%98%EB%A6%AC/05_OpenCV%EC%98%81%EC%83%81%EC%B2%98%EB%A6%AC_%EA%B5%90%EC%95%88.docx) |  |
| 06 | 객체 탐지 개념과 레이블링 (labelImg · YOLO 데이터셋) | [06_객체탐지와_레이블링](06_%EA%B0%9D%EC%B2%B4%ED%83%90%EC%A7%80%EC%99%80_%EB%A0%88%EC%9D%B4%EB%B8%94%EB%A7%81/) | [📘 교안](06_%EA%B0%9D%EC%B2%B4%ED%83%90%EC%A7%80%EC%99%80_%EB%A0%88%EC%9D%B4%EB%B8%94%EB%A7%81/06_%EA%B0%9D%EC%B2%B4%ED%83%90%EC%A7%80%EC%99%80_%EB%A0%88%EC%9D%B4%EB%B8%94%EB%A7%81_%EA%B5%90%EC%95%88.docx) |  |
| 07 | YOLO 학습과 추론 | [07_YOLO학습과추론](07_YOLO%ED%95%99%EC%8A%B5%EA%B3%BC%EC%B6%94%EB%A1%A0/) | [📘 교안](07_YOLO%ED%95%99%EC%8A%B5%EA%B3%BC%EC%B6%94%EB%A1%A0/07_YOLO%ED%95%99%EC%8A%B5%EA%B3%BC%EC%B6%94%EB%A1%A0_%EA%B5%90%EC%95%88.docx) | `model.train()` |
| 08 | AI 시스템 구축 — YOLO 서빙과 팀 프로젝트 | [08_YOLO서빙과_프로젝트](08_YOLO%EC%84%9C%EB%B9%99%EA%B3%BC_%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8/) | [📘 교안](08_YOLO%EC%84%9C%EB%B9%99%EA%B3%BC_%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8/08_YOLO%EC%84%9C%EB%B9%99%EA%B3%BC_%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8_%EA%B5%90%EC%95%88.docx) |  |

## 📂 각 장 폴더 구성

```
01_AI개요/
├── NN_..._교안.docx     ← 학생용 Word 교안 (실행 결과 · 그래프 · 탐지 결과 그림 포함)
├── ex01_....py         ← 예제 코드 (번호 순서대로 실행)
├── cvutil.py · scene.py ← 한글 경로용 OpenCV 읽기/쓰기 · 연습용 해변 사진 생성 (5 ~ 8장)
├── images/             ← 예제가 만든 그림 (정답 비교용)
└── 연습문제_정답/
    (실행하면 생기는 datasets/ · runs/ · models/ · *.keras 는 저장소에 올리지 않아요)
```

## 📝 장별 학습 목표

### 01. AI 기술 개요 — 인공지능 · 머신러닝 · 딥러닝 · 객체 탐지

AI가 무엇이고, 우리 프로젝트(객체 탐지)는 어떤 순서로 만드는지 큰 그림 잡기

- 인공지능 · 머신러닝 · 딥러닝의 관계를 설명할 수 있어요.
- "규칙을 직접 짜는 프로그래밍"과 "데이터로 규칙을 배우는 머신러닝"의 차이를 알아요.
- 컴퓨터에게 이미지가 숫자 배열이라는 것을 이해해요.
- 분류 · 객체 탐지 · 분할의 차이를 그림으로 구분할 수 있어요.
- 데이터 → 레이블링 → 학습 → 평가 → 서빙으로 이어지는 프로젝트 흐름을 알아요.
- 부유물 탐지 사례를 보고 우리 팀 주제를 떠올릴 수 있어요.

예제: `ex00_check_env.py`, `ex01_rule_vs_learning.py`, `ex02_image_is_numbers.py`, `ex03_real_photo.py`, `ex04_ai_tasks.py`

### 02. 머신러닝 기초 — 학습 · 평가 · 과대적합

scikit-learn 으로 "데이터 나누기 → 학습 → 예측 → 평가" 한 바퀴 돌기

- 특성(X)과 레이블(y), 학습 데이터와 테스트 데이터를 구분할 수 있어요.
- scikit-learn 의 `fit → predict → score` 흐름을 쓸 수 있어요.
- 과대적합 · 과소적합을 그래프로 알아볼 수 있어요.
- 정확도 · 정밀도 · 재현율 · 혼동 행렬을 읽을 수 있어요 (객체 탐지 평가의 기초).
- 분류와 회귀의 차이를 알아요.

예제: `ex01_first_model.py`, `ex02_why_split.py`, `ex03_overfitting.py`, `ex04_metrics.py`, `ex05_regression.py`

### 03. Keras 로 배우는 딥러닝 기초

뉴런 · 활성화 함수 · 손실 · 옵티마이저 — MNIST 손글씨 숫자 분류

- 뉴런이 "가중합 + 활성화 함수"라는 것을 설명할 수 있어요.
- ReLU · sigmoid · softmax 가 어디에 쓰이는지 알아요.
- Keras 로 모델을 만들고(`Sequential`) 컴파일(`compile`) · 학습(`fit`) · 평가(`evaluate`)할 수 있어요.
- 학습 곡선(loss · accuracy)을 그려 과대적합을 알아볼 수 있어요.
- 드롭아웃 · 조기 종료로 과대적합을 줄일 수 있어요.
- 모델을 저장하고 불러와 새 이미지를 예측할 수 있어요.

예제: `cvutil.py`, `ex01_neuron.py`, `ex02_activations.py`, `ex03_keras_line.py`, `ex04_mnist_dense.py`, `ex05_overfit_dropout.py`, `ex06_predict_my_digit.py`

### 04. CNN — 이미지를 보는 신경망

합성곱 · 풀링 · 특징 맵 · 데이터 증강 · 전이 학습 (YOLO 의 뼈대 이해하기)

- 합성곱(convolution) 필터가 이미지에서 특징을 찾는 원리를 알아요.
- 풀링이 크기를 줄이는 이유를 알아요.
- Keras 로 CNN 을 만들어 Dense 모델과 비교할 수 있어요.
- 특징 맵을 그려 CNN 이 무엇을 보는지 확인할 수 있어요.
- 폴더 구조 이미지 데이터셋을 불러오고 데이터 증강을 쓸 수 있어요.
- 사전 학습 모델로 전이 학습을 할 수 있어요 (YOLO 학습도 같은 원리).

예제: `cvutil.py`, `ex01_convolution.py`, `ex02_conv_pool_numbers.py`, `ex03_mnist_cnn.py`, `ex04_feature_maps.py`, `ex05_make_shapes.py`, `ex06_shapes_augment.py`, `ex07_transfer_learning.py`

### 05. OpenCV 로 영상 다루기

읽기 · 저장 · 크기 · 색 · 그리기 · 경계 · 색으로 찾기 · 동영상 · 모델 입력 만들기

- 이미지를 읽고 저장하고, 한글 경로 문제를 피할 수 있어요.
- OpenCV 의 BGR 순서와 (높이, 너비, 채널) 모양을 알아요.
- 크기 바꾸기 · 자르기 · 뒤집기 · 회전을 할 수 있어요.
- 색 공간(흑백 · HSV)을 바꾸고, 흐림 · 경계 검출을 할 수 있어요.
- 탐지 결과처럼 상자와 글자를 그릴 수 있어요.
- 색과 윤곽선으로 물체를 찾는 "규칙 기반 탐지"의 한계를 알아요.
- 동영상을 한 장면씩 읽고 저장할 수 있어요.
- 딥러닝 모델 입력(letterbox, 정규화, 배치 차원)을 만들 수 있어요.

예제: `cvutil.py`, `scene.py`, `ex00_make_samples.py`, `ex01_read_write.py`, `ex02_resize_crop.py`, `ex03_color.py`, `ex04_draw.py`, `ex05_blur_edge.py`, `ex06_color_detect.py`, `ex07_video.py`, `ex08_preprocess.py`

### 06. 객체 탐지 개념과 레이블링 (labelImg · YOLO 데이터셋)

IoU · NMS · mAP 이해하기 → 윈도우 labelImg 로 레이블링 → YOLO 데이터셋 만들고 점검하기

- 객체 탐지의 출력(클래스 · 상자 · 신뢰도)을 설명할 수 있어요.
- IoU 를 계산하고, NMS 가 겹친 상자를 지우는 원리를 알아요.
- 정밀도-재현율 곡선과 AP · mAP50 의 뜻을 알아요.
- ⭐ 윈도우에서 labelImg 로 사진에 상자를 그리고 YOLO 형식으로 저장할 수 있어요.
- YOLO 레이블 파일(.txt) 한 줄을 읽고 픽셀 좌표로 바꿀 수 있어요.
- Pascal VOC(xml) 를 YOLO 형식으로 바꿀 수 있어요.
- images/labels · train/val · data.yaml 구조의 데이터셋을 만들고 점검할 수 있어요.

예제: `cvutil.py`, `scene.py`, `ex01_iou.py`, `ex02_nms.py`, `ex03_map.py`, `ex04_read_yolo_label.py`, `ex05_voc_to_yolo.py`, `ex06_make_dataset.py`, `ex07_check_dataset.py`, `ex08_split_dataset.py`

### 07. YOLO 학습과 추론

사전 학습 모델로 탐지해 보기 → 우리 데이터로 학습 → 결과 읽기 → 사진 · 동영상 탐지

- 사전 학습된 YOLO 로 사진 속 물체를 찾을 수 있어요.
- `model.train()` 으로 우리 데이터셋을 학습할 수 있어요 (전이 학습).
- results.csv · 혼동 행렬 · mAP 를 읽고 모델을 평가할 수 있어요.
- `model.predict()` 결과(boxes)에서 좌표 · 신뢰도 · 클래스를 꺼내 OpenCV 로 그릴 수 있어요.
- 동영상을 장면마다 탐지하고 저장할 수 있어요.
- 신뢰도 기준(conf)을 바꾸며 정밀도 · 재현율의 변화를 확인할 수 있어요.
- GPU(Colab) 학습 · 이어서 학습하기 · 문제 해결 방법을 알아요.

예제: `cvutil.py`, `scene.py`, `ex00_make_dataset.py`, `ex01_pretrained.py`, `ex02_train.py`, `ex03_results.py`, `ex04_val.py`, `ex05_predict_draw.py`, `ex06_video.py`, `ex07_conf_threshold.py`

### 08. AI 시스템 구축 — YOLO 서빙과 팀 프로젝트

학습한 YOLO 를 FastAPI + HTML/CSS 웹 서비스로 만들고, 팀 프로젝트를 기획 · 진행 · 발표하기

- 학습한 YOLO 모델을 FastAPI 서버에 올릴 수 있어요.
- HTML/CSS 10장의 데모 탐지기를 YOLO 탐지기로 바꿀 수 있어요 (약속 지키기).
- TestClient 와 브라우저로 서비스 전체를 점검할 수 있어요.
- 팀 프로젝트의 주제 · 역할 · 일정 · 평가 기준을 정할 수 있어요.
- 결과를 발표하고 한계와 개선점을 설명할 수 있어요.

예제: `cvutil.py`, `scene.py`, `ex00_get_model.py`, `detector.py`, `app.py`, `static/index.html`, `static/css/style.css`, `static/js/app.js`, `static/images/sample_result.svg`, `check_api.py`

## ▶ 실행 방법

```bash
cd ai_deep_learning/07_YOLO학습과추론
python ex00_make_dataset.py   # 연습용 데이터셋
python ex02_train.py          # YOLO 학습 (CPU 약 5분)
cd ../08_YOLO서빙과_프로젝트
python ex00_get_model.py
uvicorn app:app --reload      # → http://127.0.0.1:8000
```

> Windows 에서 `cv2.imread` · `cv2.imwrite` 는 경로에 한글이 있으면 조용히 실패해요. 예제는 `cvutil.py` 로 이 문제를 피했고, 팀 프로젝트는 영어 경로(예: `C:/ai_project`)에 두는 것을 추천해요.

> 각 장 폴더로 이동(`cd`)한 뒤 실행하세요. 파일을 읽고 쓰는 예제는 실행한 폴더 또는 예제 파일 위치를 기준으로 동작해요.

➡ 다음 과정: [HTML · CSS (시맨틱 화면 구도)](../html_css/README.md)
