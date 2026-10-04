# 한글 · 공백이 들어간 경로에서도 동작하는 이미지 읽기 · 쓰기
# (Windows 에서 cv2.imread / cv2.imwrite 는 경로에 한글이 있으면 오류 없이 실패해요)
from pathlib import Path

import cv2
import numpy as np


def imread(path, flags=cv2.IMREAD_COLOR):
    data = np.fromfile(str(path), dtype=np.uint8)          # 파일을 바이트로 읽기
    return cv2.imdecode(data, flags)                       # 바이트 → 이미지


def imwrite(path, img):
    ok, buf = cv2.imencode(Path(path).suffix, img)         # 이미지 → 바이트 (.png / .jpg)
    if ok:
        buf.tofile(str(path))
    return ok
