# 학습한 데이터로 시험 보면? → 실력이 부풀려져요
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

digits = load_digits()                    # 8×8 손글씨 숫자 1797장
X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.25, random_state=0)

# 결정 트리: "꽃잎 길이가 2.5 보다 작나?" 같은 질문을 이어 가며 분류하는 모델
tree = DecisionTreeClassifier(random_state=0)
tree.fit(X_train, y_train)
print("학습 데이터로 본 정확도 :", round(tree.score(X_train, y_train), 3))
print("테스트 데이터로 본 정확도:", round(tree.score(X_test, y_test), 3))
