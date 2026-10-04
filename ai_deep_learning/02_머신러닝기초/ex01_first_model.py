# 붓꽃(iris) 꽃잎 · 꽃받침 크기로 품종 맞히기
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

iris = load_iris()                       # scikit-learn 에 들어 있는 작은 데이터 (150송이)
X, y = iris.data, iris.target            # X: 특성 4개, y: 정답 (0, 1, 2)
print("X 모양:", X.shape, "| y 모양:", y.shape)
print("특성 이름:", iris.feature_names)
print("품종 이름:", iris.target_names.tolist())
print("첫 번째 꽃:", X[0], "→ 정답", y[0])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
print("학습:", len(X_train), "송이 / 테스트:", len(X_test), "송이")

model = KNeighborsClassifier(n_neighbors=5)   # 가장 가까운 이웃 5개의 다수결
model.fit(X_train, y_train)                   # ⭐ 학습
pred = model.predict(X_test)                  # ⭐ 예측
print("예측:", pred[:10])
print("정답:", y_test[:10])
print("테스트 정확도:", model.score(X_test, y_test))

new_flower = [[5.0, 3.4, 1.5, 0.2]]
print("새 꽃의 품종:", iris.target_names[model.predict(new_flower)[0]])
