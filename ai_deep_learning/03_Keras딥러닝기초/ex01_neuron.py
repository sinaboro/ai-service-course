import numpy as np

# 뉴런 하나: 입력 × 가중치를 더하고(가중합) + 편향 → 활성화 함수
x = np.array([0.8, 0.2, 0.5])        # 입력 3개 (예: 초록색 정도, 반짝임, 세로 길이)
w = np.array([1.5, -2.0, 1.0])       # 가중치: 각 입력이 얼마나 중요한지
b = -0.6                             # 편향: 기준선 조절

z = np.dot(x, w) + b                 # 가중합 = 0.8×1.5 + 0.2×(-2.0) + 0.5×1.0 - 0.6
print("가중합 z =", round(z, 3))


def relu(v):
    return np.maximum(0, v)


def sigmoid(v):
    return 1 / (1 + np.exp(-v))


print("ReLU(z)    =", round(float(relu(z)), 3))
print("sigmoid(z) =", round(float(sigmoid(z)), 3), "← '병일 확률' 처럼 0 ~ 1 로")

# 층(layer) = 뉴런 여러 개. 가중치가 행렬이 돼요
W = np.array([[1.5, -1.0], [-2.0, 0.5], [1.0, 1.0]])   # 입력 3 → 뉴런 2
print("층 출력 =", relu(x @ W + np.array([-0.6, 0.1])))
