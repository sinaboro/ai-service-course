# ex01_read_write.py : OpenCV 로 사진 읽기 · 저장하기 — 한글 경로에서도 되는 cvutil 사용
from pathlib import Path                         # 파일 · 폴더 경로를 다루는 도구

import cv2                                       # OpenCV: 영상 처리 도구

from cvutil import imread, imwrite

HERE = Path(__file__).parent                     # 이 .py 파일이 있는 폴더 (어디서 실행해도 같은 곳)
# 읽을 사진 경로 (폴더 이름에 한글이 들어 있어요)
path = HERE / "samples" / "beach_01.png"
# any(...): 하나라도 True 면 True. ord(ch) > 127 은 "영어 · 숫자가 아닌 글자(한글 등)"라는 뜻
print("폴더 이름에 한글이 있나요?", any(ord(ch) > 127 for ch in str(path)))

img = cv2.imread(str(path))                      # ① 그냥 cv2.imread
print("cv2.imread 결과:", None if img is None else img.shape)  # 실패하면 None, 성공하면 모양 출력

img = imread(path)                               # ② cvutil.imread (한글 경로 OK)
print("cvutil.imread 결과:", img.shape, img.dtype)

# shape 는 (높이, 너비, 채널) 순서
h, w, c = img.shape
print(f"높이 {h} · 너비 {w} · 채널 {c}")
print("가운데 픽셀 (B, G, R):", img[h // 2, w // 2])
print("맨 위 줄 첫 픽셀 (바다):", img[0, 0], "← 파랑(B) 값이 가장 커요")

# 흑백으로 바꿔서 cvutil.imwrite 로 저장 (성공하면 True)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print("흑백 모양:", gray.shape)
print("저장 성공?", imwrite(HERE / "images" / "beach_gray.png", gray))
