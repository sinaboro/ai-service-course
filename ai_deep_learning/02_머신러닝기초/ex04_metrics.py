# ex04_metrics.py : 평가 지표: 정확도 · 정밀도 · 재현율 · F1 · 혼동 행렬
import platform                                   # 운영체제 이름 알아내기 (한글 글꼴 고를 때 사용)
from pathlib import Path                          # 파일 · 폴더 경로를 다루는 도구
import matplotlib.pyplot as plt                   # 그래프 도구 (관례적으로 plt 라는 별명)

# 그래프 한글 글꼴: 운영체제에 따라 알맞은 글꼴 고르기 (Windows = 맑은 고딕)
plt.rcParams["font.family"] = {"Windows": "Malgun Gothic", "Darwin": "AppleGothic"}.get(platform.system(), "NanumGothic")
# 마이너스(-) 기호가 네모로 깨지지 않게
plt.rcParams["axes.unicode_minus"] = False        # 마이너스(-) 기호가 네모로 깨지지 않게
IMG = Path(__file__).parent / "images"            # 그림을 저장할 폴더
IMG.mkdir(exist_ok=True)                          # images 폴더 만들기 (이미 있으면 그냥 넘어가요)

from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import ConfusionMatrixDisplay, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

data = load_breast_cancer()               # 종양 데이터: 0 = 악성, 1 = 양성
# 학습 75% · 테스트 25%, stratify 로 악성 · 양성 비율을 똑같이 나누기
X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.25, random_state=1, stratify=data.target)

model = make_pipeline(StandardScaler(), LogisticRegression())   # 크기 맞추기 + 로지스틱 회귀
# 학습 → 테스트 데이터 예측
model.fit(X_train, y_train)
pred = model.predict(X_test)

cm = confusion_matrix(y_test, pred)
print("혼동 행렬 (행 = 정답, 열 = 예측):")
print(cm)
print(classification_report(y_test, pred, target_names=["악성", "양성"], digits=3))

# 혼동 행렬을 그림으로 저장
fig, ax = plt.subplots(figsize=(4.5, 4))
ConfusionMatrixDisplay(cm, display_labels=["악성", "양성"]).plot(ax=ax, colorbar=False)
ax.set_xlabel("예측")
ax.set_ylabel("정답")
fig.savefig(IMG / "ex04_confusion.png", dpi=100, bbox_inches="tight")
