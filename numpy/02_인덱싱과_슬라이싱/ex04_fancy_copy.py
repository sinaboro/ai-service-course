# ex04_fancy_copy.py : 팬시 인덱싱(번호 리스트로 꺼내기)과 뷰 · copy() 의 차이
import numpy as np             # 넘파이 (관례적으로 np 라는 별명)

a = np.array([10, 20, 30, 40, 50])
print(a[[0, 2, 4]])            # 팬시 인덱싱: 여러 위치를 리스트로

m = np.arange(1, 13).reshape(3, 4)
print(m[[0, 2]])               # 0행과 2행

# 슬라이싱은 원본을 "공유"해요 (뷰)
b = a[1:4]
b[0] = 999
print("a:", a)                 # 원본도 바뀜!

# copy() 로 복사하면 따로
c = a[1:4].copy()
c[0] = -1
print("a:", a, "/ c:", c)
