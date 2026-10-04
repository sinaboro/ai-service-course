import platform
from pathlib import Path
import matplotlib.pyplot as plt

# 그래프 한글 글꼴: 운영체제에 따라 알맞은 글꼴 고르기 (Windows = 맑은 고딕)
plt.rcParams["font.family"] = {"Windows": "Malgun Gothic", "Darwin": "AppleGothic"}.get(platform.system(), "NanumGothic")
# 마이너스(-) 기호가 네모로 깨지지 않게
plt.rcParams["axes.unicode_minus"] = False
IMG = Path(__file__).parent / "images"            # 그림을 저장할 폴더
IMG.mkdir(exist_ok=True)

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
