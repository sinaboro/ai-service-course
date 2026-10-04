# 설치된 라이브러리 버전 확인
import sys

# 이 과정에서 쓰는 라이브러리를 모두 불러와 봐요. 오류가 나면 그 라이브러리 설치가 안 된 것
import cv2
import keras
import numpy as np
import sklearn
import tensorflow as tf
import torch
import ultralytics

# 각 라이브러리의 __version__ 에 버전 번호가 들어 있어요
print("파이썬      ", sys.version.split()[0])
print("numpy       ", np.__version__)
print("scikit-learn", sklearn.__version__)
print("tensorflow  ", tf.__version__)
print("keras       ", keras.__version__)
print("opencv      ", cv2.__version__)
print("torch       ", torch.__version__, "| GPU 사용 가능:", torch.cuda.is_available())
print("ultralytics ", ultralytics.__version__)
