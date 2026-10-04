# 문제 2. ex06_color_detect.py 를 바꿔 흰색 비닐봉지를 찾아 보세요. (힌트: 흰색은 HSV 에서 S 가 낮고 V 가 높아요. [0, 0, 220] ~ [179, 40, 255])

from pathlib import Path
import cv2
import numpy as np
from cvutil import imread
img = imread(Path("samples/beach_01.png"))
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv, np.array([0, 0, 220]), np.array([179, 40, 255]))
mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
big = [cv2.boundingRect(c) for c in contours if cv2.contourArea(c) >= 100]
print("흰 물체 수:", len(big))
for b in big:
    print("상자 (x, y, w, h):", b)
