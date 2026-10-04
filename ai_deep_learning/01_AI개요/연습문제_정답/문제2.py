# 문제 2. zidane.jpg(ultralytics ASSETS)를 읽어 모양(shape)과 가운데 픽셀 값을 출력하세요.

import cv2
from ultralytics.utils import ASSETS
img = cv2.imread(str(ASSETS / "zidane.jpg"))
h, w = img.shape[:2]
print("모양:", img.shape)
print("가운데 픽셀 (B, G, R):", img[h // 2, w // 2])
