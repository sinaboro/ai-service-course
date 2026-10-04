# 문제 1. ex01_first_model.py에서 n_neighbors를 1, 3, 5, 15, 50 으로 바꿔 테스트 정확도를 출력하세요.

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=42, stratify=iris.target)
for k in [1, 3, 5, 15, 50]:
    model = KNeighborsClassifier(n_neighbors=k).fit(X_train, y_train)
    print(f"k={k:2d}  정확도 {model.score(X_test, y_test):.3f}")
