# 설치된 라이브러리 버전 확인
import sys  # 파이썬 실행 환경 (import 경로 sys.path 등)

# 이 과정에서 쓰는 라이브러리를 모두 불러와 봐요. 오류가 나면 그 라이브러리 설치가 안 된 것
import cv2  # OpenCV: 영상 처리 도구
import keras  # 딥러닝 도구 Keras
import numpy as np  # 넘파이 (관례적으로 np 라는 별명)
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
