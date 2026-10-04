from pathlib import Path

import cv2

from cvutil import imread, imwrite

HERE = Path(__file__).parent
path = HERE / "samples" / "beach_01.png"
print("폴더 이름에 한글이 있나요?", any(ord(ch) > 127 for ch in str(path)))

img = cv2.imread(str(path))                      # ① 그냥 cv2.imread
print("cv2.imread 결과:", None if img is None else img.shape)

img = imread(path)                               # ② cvutil.imread (한글 경로 OK)
print("cvutil.imread 결과:", img.shape, img.dtype)

h, w, c = img.shape
print(f"높이 {h} · 너비 {w} · 채널 {c}")
print("가운데 픽셀 (B, G, R):", img[h // 2, w // 2])
print("맨 위 줄 첫 픽셀 (바다):", img[0, 0], "← 파랑(B) 값이 가장 커요")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print("흑백 모양:", gray.shape)
print("저장 성공?", imwrite(HERE / "images" / "beach_gray.png", gray))
