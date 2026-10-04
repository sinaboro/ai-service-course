import platform
from pathlib import Path
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = {"Windows": "Malgun Gothic", "Darwin": "AppleGothic"}.get(platform.system(), "NanumGothic")
plt.rcParams["axes.unicode_minus"] = False
IMG = Path(__file__).parent / "images"            # 그림을 저장할 폴더
IMG.mkdir(exist_ok=True)

from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

digits = load_digits()
X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.25, random_state=0)

depths = range(1, 21)
train_acc, test_acc = [], []
for d in depths:
    tree = DecisionTreeClassifier(max_depth=d, random_state=0).fit(X_train, y_train)
    train_acc.append(tree.score(X_train, y_train))
    test_acc.append(tree.score(X_test, y_test))

best = max(depths, key=lambda d: test_acc[d - 1])
print("깊이 1 → 학습", round(train_acc[0], 2), "/ 테스트", round(test_acc[0], 2), " (과소적합)")
print(f"깊이 {best} → 학습", round(train_acc[best - 1], 2), "/ 테스트", round(test_acc[best - 1], 2), " (가장 좋음)")
print("깊이 20 → 학습", round(train_acc[-1], 2), "/ 테스트", round(test_acc[-1], 2), " (학습만 완벽)")

fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(depths, train_acc, "o-", label="학습 정확도")
ax.plot(depths, test_acc, "s-", label="테스트 정확도")
ax.axvline(best, color="gray", linestyle="--")
ax.set_xlabel("트리 깊이 (모델 복잡도)")
ax.set_ylabel("정확도")
ax.set_title("복잡할수록 학습 점수는 오르지만, 테스트 점수는 멈춰요")
ax.legend()
fig.savefig(IMG / "ex03_overfitting.png", dpi=100, bbox_inches="tight")
