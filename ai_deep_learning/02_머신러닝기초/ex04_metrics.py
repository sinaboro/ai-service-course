import platform
from pathlib import Path
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = {"Windows": "Malgun Gothic", "Darwin": "AppleGothic"}.get(platform.system(), "NanumGothic")
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
X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.25, random_state=1, stratify=data.target)

model = make_pipeline(StandardScaler(), LogisticRegression())   # 크기 맞추기 + 로지스틱 회귀
model.fit(X_train, y_train)
pred = model.predict(X_test)

cm = confusion_matrix(y_test, pred)
print("혼동 행렬 (행 = 정답, 열 = 예측):")
print(cm)
print(classification_report(y_test, pred, target_names=["악성", "양성"], digits=3))

fig, ax = plt.subplots(figsize=(4.5, 4))
ConfusionMatrixDisplay(cm, display_labels=["악성", "양성"]).plot(ax=ax, colorbar=False)
ax.set_xlabel("예측")
ax.set_ylabel("정답")
fig.savefig(IMG / "ex04_confusion.png", dpi=100, bbox_inches="tight")
