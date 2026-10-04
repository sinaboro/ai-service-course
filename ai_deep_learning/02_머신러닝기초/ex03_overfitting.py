import platform
from pathlib import Path
import matplotlib.pyplot as plt

# 그래프 한글 글꼴: 운영체제에 따라 알맞은 글꼴 고르기 (Windows = 맑은 고딕)
plt.rcParams["font.family"] = {"Windows": "Malgun Gothic", "Darwin": "AppleGothic"}.get(platform.system(), "NanumGothic")
# 마이너스(-) 기호가 네모로 깨지지 않게
plt.rcParams["axes.unicode_minus"] = False
IMG = Path(__file__).parent / "images"            # 그림을 저장할 폴더
IMG.mkdir(exist_ok=True)

from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

digits = load_digits()
X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.25, random_state=0)

# 깊이 1 ~ 20 의 트리를 하나씩 만들어 학습 · 테스트 정확도를 기록
depths = range(1, 21)
train_acc, test_acc = [], []
for d in depths:
    tree = DecisionTreeClassifier(max_depth=d, random_state=0).fit(X_train, y_train)
    train_acc.append(tree.score(X_train, y_train))
    test_acc.append(tree.score(X_test, y_test))

best = max(depths, key=lambda d: test_acc[d - 1])
# 결과 출력: 너무 얕으면 둘 다 낮고(과소적합), 너무 깊으면 학습만 높아요(과대적합)
print("깊이 1 → 학습", round(train_acc[0], 2), "/ 테스트", round(test_acc[0], 2), " (과소적합)")
print(f"깊이 {best} → 학습", round(train_acc[best - 1], 2), "/ 테스트", round(test_acc[best - 1], 2), " (가장 좋음)")
print("깊이 20 → 학습", round(train_acc[-1], 2), "/ 테스트", round(test_acc[-1], 2), " (학습만 완벽)")

# 두 정확도를 한 그래프에: 회색 점선 = 테스트가 가장 좋은 깊이
fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(depths, train_acc, "o-", label="학습 정확도")
ax.plot(depths, test_acc, "s-", label="테스트 정확도")
ax.axvline(best, color="gray", linestyle="--")
ax.set_xlabel("트리 깊이 (모델 복잡도)")
ax.set_ylabel("정확도")
ax.set_title("복잡할수록 학습 점수는 오르지만, 테스트 점수는 멈춰요")
ax.legend()
fig.savefig(IMG / "ex03_overfitting.png", dpi=100, bbox_inches="tight")
