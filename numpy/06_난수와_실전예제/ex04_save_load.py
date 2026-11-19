# ex04_save_load.py : 배열을 파일로 저장하고 다시 읽기: CSV(savetxt/loadtxt) · .npy(save/load)
import numpy as np                                        # 넘파이 (관례적으로 np 라는 별명)

data = np.array([[1.5, 2.0, 3.25],
                 [4.0, 5.5, 6.75]])

np.savetxt("data.csv", data, delimiter=",", fmt="%.2f")   # CSV 로 저장
loaded = np.loadtxt("data.csv", delimiter=",")             # 다시 읽기
print(loaded)
print(loaded.shape, loaded.sum())

np.save("data.npy", data)          # NumPy 전용 형식 (빠르고 정확)
print(np.load("data.npy"))
