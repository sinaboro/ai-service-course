import numpy as np

data = np.array([[1.5, 2.0, 3.25],
                 [4.0, 5.5, 6.75]])

np.savetxt("data.csv", data, delimiter=",", fmt="%.2f")   # CSV 로 저장
loaded = np.loadtxt("data.csv", delimiter=",")             # 다시 읽기
print(loaded)
print(loaded.shape, loaded.sum())

np.save("data.npy", data)          # NumPy 전용 형식 (빠르고 정확)
print(np.load("data.npy"))
