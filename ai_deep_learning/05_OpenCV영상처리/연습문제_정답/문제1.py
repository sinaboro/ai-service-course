# 문제 1. samples/beach_02.png 를 읽어 왼쪽 위 1/4 만 잘라 2배로 키우고 images/q1_zoom.png 로 저장한 뒤 모양을 출력하세요.

from pathlib import Path
import cv2
from cvutil import imread, imwrite
img = imread(Path("samples/beach_02.png"))
h, w = img.shape[:2]
part = img[:h // 2, :w // 2]
big = cv2.resize(part, (part.shape[1] * 2, part.shape[0] * 2))
imwrite(Path("images/q1_zoom.png"), big)
print("잘라 낸 모양:", part.shape, "→ 키운 모양:", big.shape)
