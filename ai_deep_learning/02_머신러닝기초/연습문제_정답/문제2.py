# 문제 2. load_digits 데이터를 KNeighborsClassifier로 학습하고, 혼동 행렬에서 가장 많이 헷갈린 숫자 쌍을 찾아 출력하세요.

import numpy as np
from sklearn.datasets import load_digits
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
d = load_digits()
X_train, X_test, y_train, y_test = train_test_split(d.data, d.target, test_size=0.25, random_state=0)
pred = KNeighborsClassifier().fit(X_train, y_train).predict(X_test)
cm = confusion_matrix(y_test, pred)
np.fill_diagonal(cm, 0)                       # 맞힌 칸(대각선)은 지우기
i, j = np.unravel_index(cm.argmax(), cm.shape)
print(f"정답 {i} 을(를) {j} (으)로 {cm[i, j]}번 헷갈림")
print("전체 정확도:", round((pred == y_test).mean(), 3))
