# 설치된 라이브러리 버전 확인
import sys

import cv2
import keras
import numpy as np
import sklearn
import tensorflow as tf
import torch
import ultralytics

print("파이썬      ", sys.version.split()[0])
print("numpy       ", np.__version__)
print("scikit-learn", sklearn.__version__)
print("tensorflow  ", tf.__version__)
print("keras       ", keras.__version__)
print("opencv      ", cv2.__version__)
print("torch       ", torch.__version__, "| GPU 사용 가능:", torch.cuda.is_available())
print("ultralytics ", ultralytics.__version__)
