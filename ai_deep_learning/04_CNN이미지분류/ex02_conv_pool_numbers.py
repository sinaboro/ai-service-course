import numpy as np

img = np.array([                                    # 5 × 6 이미지: 가운데 세로 막대
    [0, 0, 9, 9, 0, 0],
    [0, 0, 9, 9, 0, 0],
    [0, 0, 9, 9, 0, 0],
    [0, 0, 9, 9, 0, 0],
    [0, 0, 9, 9, 0, 0],
], dtype=float)
k = np.array([[-1, 1], [-1, 1]], dtype=float)       # 왼쪽 → 오른쪽으로 밝아지는 곳을 찾는 2×2 필터

# 합성곱: 필터를 한 칸씩 옮기며 (겹친 칸끼리 곱해서 모두 더하기)
# 결과 크기 = (높이 - 필터 + 1, 너비 - 필터 + 1) → (4, 5)
out = np.zeros((img.shape[0] - 1, img.shape[1] - 1))
# 필터를 한 칸씩 오른쪽 · 아래로 옮기며 계산
for i in range(out.shape[0]):
    for j in range(out.shape[1]):
        out[i, j] = (img[i:i + 2, j:j + 2] * k).sum()
print("합성곱 결과 (밝아지는 경계 = 큰 양수, 어두워지는 경계 = 큰 음수):")
print(out)

# 최대 풀링 2×2: 4칸 중 가장 큰 값만 남기기 → 크기가 절반
# ReLU: 음수는 0 으로 (CNN 은 합성곱 뒤에 보통 ReLU 를 써요)
relu = np.maximum(out[:, :4], 0)
pool = relu.reshape(relu.shape[0] // 2, 2, relu.shape[1] // 2, 2).max(axis=(1, 3))
print("ReLU 후 왼쪽 4칸:\n", relu)
print("2×2 최대 풀링:\n", pool)
